from rest_framework import serializers
from .models import Image

class ImageSerializer(serializers.ModelSerializer):
    image=serializers.ImageField()
    class Meta:
        model=Image
        fields='__all__'