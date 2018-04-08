import datetime

from django.db import models


class IssueManager(models.Manager):
    """An Issue manager to define custom calculation methods for object
    istances
    """
    def get_solved_issue_durations(self):
        """A manager method that returns time durations for all solved issues
        """
        durations = []
        solved_issues = self.model.objects.filter(solved=True)

        for i in solved_issues:
            durations.append(i.solved_on - i.created_on)

        return durations

    def humanize_timedelta(self, td):
        """returns human readable representation of timedelta value
        """

        hours, remainder = divmod(td.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        return {
            'hours': hours,
            'minutes': minutes,
            'seconds': seconds,
        }

    def get_average_solving_time(self):
        # XXX: We could realy easily solve this with Django's Avg aggregations,
        # (see this code block that's commented out) but because sqlite3 is
        # saving datetime/time fields in databse as text, we need some custom
        # math

        # avg = self.model.objects.filter(solved=True).aggregate(
            # average_difference=models.Avg(
                # models.F('solved_on') - models.F('created_on')
            # )
        # )
        solved_issue_timedeltas = self.get_solved_issue_durations()

        if not solved_issue_timedeltas:
            return self.humanize_timedelta(datetime.timedelta(0))

        average_timedelta = sum(
            # giving datetime.timedelta(0) as the start value makes sum work
            # on timedeltas:
            solved_issue_timedeltas, datetime.timedelta(0)
        ) / len(solved_issue_timedeltas)

        return self.humanize_timedelta(average_timedelta)

    def get_longest_solving_time(self):
        solved_issue_timedeltas = self.get_solved_issue_durations()

        if not solved_issue_timedeltas:
            return self.humanize_timedelta(datetime.timedelta(0))

        return self.humanize_timedelta(max(solved_issue_timedeltas))

    def get_shortest_solving_time(self):
        solved_issue_timedeltas = self.get_solved_issue_durations()

        if not solved_issue_timedeltas:
            return self.humanize_timedelta(datetime.timedelta(0))

        return self.humanize_timedelta(min(solved_issue_timedeltas))
