"""student URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from bootstrap import settings
from django.conf.urls.static import static
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('<filename>.html', views.html),
    # path('', views.index),
    path('', views.welcome, name='welcome'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('firstPage', views.first_page, name='first_page'),
    path('ess', views.ess, name='ess'),
    path('pretest', views.pretest, name='pretest'),
    path('VoiceRecognition', views.VoiceRecognition, name='VoiceRecognition'),
    path('index', views.index, name='index'),
    path('index_2', views.index_2, name='index_2'),
    path('index_3', views.index_3, name='index_3'),
    path('importCsv', views.importCsv, name='importCsv'),
    path('KeyPoint', views.KeyPoint, name='key_point'),
    path('KeyPointResult', views.KeyPointResult, name='key_point_result'),
    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
