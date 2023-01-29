from django import forms
<<<<<<< HEAD
<<<<<<< HEAD
from .models import Image, Video
=======
from .models import Image
>>>>>>> 9bb8654c0e1fa2d1238491e18278cf49604aa637
=======
from .models import Image
>>>>>>> ee9aea8311262ab1ae6a28270a51f7fa736894f5

class UploadFileForm(forms.Form):
    file = forms.FileField()

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
<<<<<<< HEAD
<<<<<<< HEAD
        fields = ('title','image',)

class VideoForm(forms.ModelForm):
    class Meta:
        model= Video
        fields= ['title','video',]
=======
        fields = ('image',)
>>>>>>> 9bb8654c0e1fa2d1238491e18278cf49604aa637
=======
        fields = ('image',)
>>>>>>> ee9aea8311262ab1ae6a28270a51f7fa736894f5
