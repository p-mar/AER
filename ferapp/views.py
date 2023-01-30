from django.shortcuts import render, loader
from .forms import UploadFileForm
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import HttpResponse

from .forms import ImageForm, VideoForm
from .ml_model.image_mode import dan_image
from .ml_model.video_mode import dan_video
import mimetypes
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Image, Video, File
from .serializer import ImageSerializer, VideoSerializer, FileSerializer
import shutil
FILE_TITLE=''

def changeTitle(new_title):
    return new_title


def index(request):
  template = loader.get_template('home.html')
  return HttpResponse(template.render())

@ensure_csrf_cookie

def upload_screen(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            print(file.name)
            handle_uploaded_file(file)
            return render(request, "upload_screen.html", {'filename': file.name})
    else:
        form = UploadFileForm()
    return render(request, 'upload_screen.html', {'form': form})


def handle_uploaded_file(f):
    with open(f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            img_obj = form.instance
            new_url = img_obj.image.url[1:]
            global FILE_TITLE
            FILE_TITLE=str(new_url[13:-4])
            dan_image.main(new_url)
            fp=open('ferapp\ml_model\image_mode\emotion.txt','r')
            emotion=str(fp.read())

            fp.close()
            return render(request, 'upload_image.html', {'form': form, 'img_obj': img_obj, 'emotion': emotion})
    else:
        form = ImageForm()
    return render(request, 'upload_image.html', {'form': form})

def upload_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            vid_obj = form.instance
            new_url = vid_obj.video.url[1:]
            vid_title = new_url[13:]
            dan_video.main(new_url, vid_title)
            fp=open('ferapp\ml_model\\video_mode\emotion.txt','r')
            emotion=str(fp.readlines())
            return render(request, 'upload_screen.html', {'form': form, 'vid_obj': vid_obj, 'emotion': emotion})
    else:
        form = VideoForm()
    
    return render(request, 'upload_screen.html', {'form': form})    

def download_file_image(request):
    filename = str(FILE_TITLE)+'.txt'
    fl_path = 'ferapp\ml_model\\image_mode\\results\\'+filename
    fl = 'ferapp\ml_model\\image_mode\emotion.txt'
    #txtfile = open('ferapp\ml_model\\image_mode\\results\\'+filename, 'w+')
    shutil.copyfile(fl,fl_path)
    txtfl=open(fl_path,'r')
    mime_type, _ = mimetypes.guess_type(fl_path)
    response = HttpResponse(txtfl, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response

def download_file_video(request):
    fl_path = 'ferapp\ml_model\\video_mode\emotion.txt'
    filename = 'emotion.txt'

    fl = open(fl_path, 'r')
    mime_type, _ = mimetypes.guess_type(fl_path)
    response = HttpResponse(fl, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response

def about(request_iter):
    return render(request_iter,'about_page.html')

def history(request_iter):
    return render(request_iter,'history.html')

def contact(request_iter):
    return render(request_iter,'contact_page.html')

# rest api requests
@api_view(['GET'])
def getImage(request):
    image = Image.objects.all()
    serializer = ImageSerializer(image, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def postImage(request):
    serializer = ImageSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def getVideo(request):
    video = Video.objects.all()
    serializer = VideoSerializer(video, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def postVideo(request):
    serializer = VideoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def getFile(request):
    file = File.objects.all()
    serializer = FileSerializer(file, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def postFile(request):
    serializer = FileSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
