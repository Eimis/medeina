from django.shortcuts import render

from medeina.models import Issue
from medeina.serializers import IssueSerializer

from rest_framework.response import Response
from rest_framework.views import APIView


def main(request):
    '''Main app view for SPA
    '''

    return render(request, 'main.html', {})


class ListIssuesView(APIView):
    """
    View to list current issues in the system.

    * Requires no authentication
    * Requires no special permissions
    """
    # authentication_classes = (authentication.TokenAuthentication,)
    # permission_classes = (permissions.IsAdminUser,)

    # ony allow GET request:
    http_method_names = ['get', ]

    def get(self, request, format=None):
        """
        Lists all ShoppingItem instances.
        """
        issues = Issue.objects.all()
        serializer = IssueSerializer(issues, many=True)

        return Response(serializer.data)
