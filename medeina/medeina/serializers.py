from django.contrib.auth.models import User

from rest_framework import serializers

from medeina.models import IssueCategory, Issue


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', )


class IssueCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = IssueCategory
        fields = ('name', )


class IssueSerializer(serializers.ModelSerializer):
    submitter = UserSerializer()
    solver = UserSerializer()
    category = IssueCategorySerializer()

    class Meta:
        model = Issue
        fields = (
            'pk',
            'title',
            'solved',
            'submitter',
            'solver',
            'text_description',
            'state',
            'category',
        )
