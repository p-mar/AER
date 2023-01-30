from rest_framework import serializers
from .models import Image, Video, File

class ImageSerializer(serializers.ModelSerializer):
    image=serializers.ImageField()
    class Meta:
        model=Image
        fields='__all__'

class VideoSerializer(serializers.ModelSerializer):
    video=serializers.VideoField()
    class Meta:
        model=Video
        fields='__all__'

class FileSerializer(serializers.ModelSerializer):
    file=serializers.FileField()
    class Meta:
        model=File
        fields='__all__'
