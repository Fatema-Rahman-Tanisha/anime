from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import  static
urlpatterns = [
    path('', views.ANIME , name="anime"),
    path('add/', views.add , name="add"),
    path('add/watch/<str:slug>/', views.watch , name="add"),
    path('watch/<str:slug>/', views.watch , name="animeFull"),
    path('watch/<str:slug>/comment/', views.com , name="animeFull"),
    path('watch/<str:slug>/add/', views.add , name="animeFull"),
    path('favourite/', views.add , name="animeFull"),

    ]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)