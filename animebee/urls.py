#python manage.py runserver
#python manage.py makemigrations
#python manage.py migrate
#django-admin startapp
# admin's username :: riyuzaki
# admin's password :: DeathNote_Was_cool_!!
from django.contrib.auth import authenticate ,login , logout
from django.contrib.auth.models import User
from django.shortcuts import render , HttpResponse , redirect
from django.conf import settings
from django.conf.urls.static import  static
from django.contrib import admin
from django.shortcuts import render
from django.urls import path
from anime.models import  Favourite
from django.urls.conf import include
def signup(request):
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['password']
        username=request.POST['username']
        user = User.objects.create_user(username, email, password)
        user.save()
        Favourite.objects.create(user=user)
        return redirect('/login/')
    return render(request,"auth/signup.html")
def log(request):
    if request.method=="POST":
        user=request.POST['user']
        pword=request.POST['pword']
        user = authenticate(username=user ,password=pword)
        if user is not None:
            login(request,user)
            return redirect('/anime/')
          
        else:
            pass
    return render(request,'auth/login.html')
def lgout(request):
    logout(request)
    return HttpResponse("logged out")
def home(request):
    return render(request,"home/index.html")
urlpatterns = [

    path('admin/', admin.site.urls),
    path('', home),
    path('anime/', include("anime.urls")),
  
    path('login/', log),
    path('signup/', signup),
    path('logout/', lgout),
    # your name hindi
    #41:23
    #https://disk.yandex.ru/i/XUnAHyCBqVp6SA
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)