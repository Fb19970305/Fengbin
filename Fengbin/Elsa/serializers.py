from models import *
from rest_framework import serializers

class ElsaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Elsa
        fields = ('id', 'comment', 'urls', 'price', 'cloth_type', 'cloth_num')
