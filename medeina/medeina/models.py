from django.contrib.auth.models import User
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from medeina.managers import IssueManager
from medeina.states import IssueStates

from django_states.fields import StateField


@python_2_unicode_compatible
class IssueCategory(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Issue categories'


@python_2_unicode_compatible
class Issue(models.Model):
    objects = IssueManager()

    solved = models.BooleanField(default=False)
    title = models.CharField(max_length=50)
    submitter = models.ForeignKey(User, related_name='submitted_issues')
    solver = models.ForeignKey(User, related_name='solved_issues', null=True)
    text_description = models.TextField()
    state = StateField(machine=IssueStates)
    category = models.ForeignKey(IssueCategory)
    created_on = models.DateTimeField(auto_now_add=True)
    solved_on = models.DateTimeField(null=True)

    def __str__(self):
        return self.title
