from rest_framework import serializers
from base.models import items

class itemserializers(serializers.ModelSerializer):
    class Meta:
        model = items
        fields = '__all__'
