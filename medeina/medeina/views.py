from django.shortcuts import render

from medeina.models import Issue
from medeina.permissions import UserIsAuthenticated
from medeina.serializers import IssueSerializer

from rest_framework import generics
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
    # authentication_classes = (authentication.TokenAuthentication,)
    # permission_classes = (IsAdminUser,)

    queryset = Issue.objects.all()
    serializer_class = IssueSerializer

    # ony allow GET request:
    http_method_names = ['get', ]


class UpdateIssueView(generics.UpdateAPIView):
    """
    View to mark issue as solved.

    * Requires no authentication
    * Requires no special permissions
    """
    # authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (UserIsAuthenticated, )

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
            serializer.save()
            return Response(status=200, data=serializer.data)
        else:
            return Response({pk: serializer.errors}, status=400)
