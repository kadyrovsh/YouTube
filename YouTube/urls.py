from django.contrib import admin
from django.urls import path
from .asosiyapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('kanal/', KanalsView.as_view()),
    path('video/', VideosView.as_view()),
    path('playlist/', PlaylistsView.as_view()),
    path('playlist/<int:pk>/', PlaylistView.as_view()),
    path('video/<int:pk>/', VideosView.as_view()),
    path('kanal/<int:pk>/', KanalView.as_view()),
]
