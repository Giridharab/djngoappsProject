from rest_framework import serializers
from .models import *


class NuggetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nugget
        fields = '__all__'
