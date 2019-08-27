"""ArticleBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, re_path
from ArticleBlog import views

urlpatterns = [
    path('admin/', admin.site.urls),

    re_path(r'^$', views.index),
    path('index/', views.index),
    path('tv/', views.template_variable),
    path('tl/', views.template_label),
    
    path('page_list/', views.page_list),
    re_path(r'page/(?P<num>\d{1,2})/', views.page)
    
    # re_path(r'page/(?P<page>\d{1,2})', views.page_list),
    # path('login/', views.login),
    # path('show/', views.show),
    # re_path(r'^introduce/(\w+)/(\d{3})$', views.introduce),

]
