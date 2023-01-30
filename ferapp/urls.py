from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('help/', views.about, name='help'),
    path('contact/', views.contact, name='contact'),
    path('history/', views.history, name='history'),
    path('upload_video/', views.upload_video, name='upload_video'),
    path('upload_image/', views.upload_image, name='upload_image'),
    path('upload_image/download', views.download_file_image),
    path('upload_video/download', views.download_file_video),
    path('get/',views.getImage),
    path('post/',views.postImage),

]


