from .models import Records
from rest_framework import serializers
  
class viewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Records
        fields = ['uid', 'sentance', 'result']

class postSerializer(serializers.ModelSerializer):
    class Meta:
        model = Records
        fields = ['uid', 'sentance']
