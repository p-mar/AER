from django import forms

from .models import Image, Video


class UploadFileForm(forms.Form):
    file = forms.FileField()

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image

        fields = ('title','image',)

class VideoForm(forms.ModelForm):
    class Meta:
        model= Video
        fields= ['title','video',]



