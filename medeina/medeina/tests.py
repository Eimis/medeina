import json

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import TestCase

from medeina.models import Issue


class IssuesAPITestCase(TestCase):

    def test_main_view(self):
        """
        Tests if main app view returns proper status code
        """

        url = reverse('main')

        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_issue_view(self):
        """
        Tests if this API endpoint properly updates Issue model instance
        """
        # This Issue is created during data migration, but later on one might
        # want to use factory_boy or similar library:
        issue = Issue.objects.last()
        self.assertEquals(issue.solved, False)

        # This user is created during data migration, but later on one might
        # want to use factory_boy or similar library:
        superuser = User.objects.get(username='superuser')
        self.client.login(username=superuser.username, password='superuser')

        post_data = {'solved': True}
        response = self.client.patch(
            reverse('update_issue', kwargs={'pk': issue.pk}),
            json.dumps(post_data),
            content_type='application/json',
            format='json',
        )

        self.assertEqual(response.status_code, 200)
        issue.refresh_from_db()
        self.assertEquals(issue.solved, True)

        self.assertEquals(
            response.json(),  # see: https://stackoverflow.com/a/35255577
            {'category': {'name': issue.category.name},
             'pk': issue.pk,
             'solved': issue.solved,
             'solver': {'username': superuser.username},
             'state': issue.state,
             'submitter': {'username': superuser.username},
             'text_description': issue.text_description,
             'title': issue.title}
        )
