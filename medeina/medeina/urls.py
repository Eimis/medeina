from django.conf.urls import url
from django.contrib import admin

from medeina.views import IssueStatsView, main, ListIssuesView, UpdateIssueView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', main, name='main'),
    url(r'^issues/list$', ListIssuesView.as_view(), name='list_issues'),
    url(
        r'^issues/(?P<pk>\d+)/update$',
        UpdateIssueView.as_view(),
        name='update_issue'
    ),
    url(r'^issues/stats$', IssueStatsView.as_view(), name='issue_stats'),
]
