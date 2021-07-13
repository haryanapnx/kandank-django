from django.db.models import fields
from rest_framework import serializers
from tutorials.models import Tutorial


class TutorialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutorial
        fields = (
          'id',
          'title',
          'description',
          'published'
        )
