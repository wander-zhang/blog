"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from blogapp import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'index.html$', views.index),
    url(r'article.html$', views.article),
    url(r'personaldata.html$', views.personaldata),
    url(r'^content/', views.content),
    url(r'id=5$', views.id5),
    url(r'id=1$', views.id1),
    url(r'id=2$', views.id2),
    url(r'id=3$', views.id3),
    url(r'id=4$', views.id4),
]
