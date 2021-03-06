from django.shortcuts import render
from django.utils import timezone

from medeina.models import Issue
from medeina.permissions import UserIsAuthenticated, UserIsSuperuser
from medeina.serializers import IssueSerializer

from rest_framework import generics
from rest_framework import views
from rest_framework.response import Response


def main(request):
    '''Main app view for SPA
    '''

    return render(request, 'main.html', {})


class ListIssuesView(generics.ListAPIView):
    """
    View to list current issues in the system.

    * Requires no authentication
    * Requires no special permissions
    """
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer

    # ony allow GET request:
    http_method_names = ['get', ]


class UpdateIssueView(generics.UpdateAPIView):
    """
    View to mark issue as solved.

    * Requires to be authenticated
    * Requires superuser permission
    * Permission to update Issue state is checked not only on this API
      endpoint, but also on object level (see: medeina/states.py)
    """
    permission_classes = (UserIsAuthenticated, UserIsSuperuser)

    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    # ony allow PATCH request:
    http_method_names = ['patch', ]

    def patch(self, request, pk):
        issue = self.get_object()
        serializer = IssueSerializer(
            issue,
            data=request.data,
            # allow partial update (for future functionality):
            partial=True
        )

        if serializer.is_valid():
            # UserIsSuperuser permission class already cheched if user is
            # allowed to access the endpoint, so:
            issue.get_state_info().make_transition(
                'mark_as_solved',
                request.user
            )
            serializer.save()

            # TODO: one might want to implement another API endpoint for
            # getting current user info, then passing it to the serializer via
            # frontend
            # Set issue solver:
            issue.solver = request.user

            # Set issue solving TS:
            issue.solved_on = timezone.now()
            issue.save()

            return Response(status=200, data=serializer.data)
        else:
            return Response({pk: serializer.errors}, status=400)


class IssueStatsView(views.APIView):
    """
    View to return statistics about Issue solving time.

    * Requires no authentication
    * Requires no special permissions
    """

    # ony allow GET request:
    http_method_names = ['get', ]

    def get(self, request, format=None):

        stats = {
            'min': Issue.objects.get_shortest_solving_time(),
            'max': Issue.objects.get_longest_solving_time(),
            'avg': Issue.objects.get_average_solving_time(),
        }

        return Response(stats, status=200)
