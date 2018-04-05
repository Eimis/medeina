from django.contrib.auth.models import User
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from medeina.states import IssueStates

from django_states.fields import StateField


@python_2_unicode_compatible
class IssueCategory(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Issue(models.Model):
    title = models.CharField(max_length=50)
    submitter = models.ForeignKey(User, related_name='submitted_issues')
    solver = models.ForeignKey(User, related_name='solved_issues', null=True)
    text_description = models.TextField()
    status = StateField(machine=IssueStates)
    category = models.ForeignKey(IssueCategory)

    def __str__(self):
        return self.title
