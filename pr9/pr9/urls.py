"""
URL configuration for pr9 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from app9 import views

urlpatterns = [
    path('admin/', admin.site.urls),
   path('upload/', views.upload_document, name='upload_document'),
    path('', views.document_list, name='document_list'),
    path('ss/',views.set_session,name="set_session"),
    path('gs/',views.get_session,name='get_session'),
    path('sc/',views.set_cookie,name='set_cookie'),
    path('gc/',views.get_cookie,name='get_cookie'),
    path('login/',views.login,name='login')

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

