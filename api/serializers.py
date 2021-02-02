from rest_framework import serializers
from api import models


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tag
        fields = "__all__"

class ProblemSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many = True, read_only = True)
    class Meta:
        model = models.Problem
        fields = "__all__"

class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Submission
        fields = '__all__'