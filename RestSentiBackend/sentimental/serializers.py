from django.db.models import fields
from rest_framework import serializers
from .models import Records
  
class RecordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Records
        fields = ('uid', 'sentance', 'result')