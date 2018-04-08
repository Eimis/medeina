from django.contrib import admin

from medeina.models import Issue, IssueCategory


class IssueAdmin(admin.ModelAdmin):
    readonly_fields = ('state',)


class IssueCategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Issue, IssueAdmin)
admin.site.register(IssueCategory, IssueCategoryAdmin)
