"""
URL configuration for employee_management project.

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
from myapp import views 


urlpatterns = [
    path('admin/', admin.site.urls),
     path('accounts/', include('django.contrib.auth.urls')),
     path('',views.home, name='home'),
     path('accounts/profile/', views.profile_view, name='employee_list'),
     path('employee/<int:id>/', views.employee_detail, name='employee_detail'),
     path('employee/add/', views.employee_add, name='employee_add'),
     path('employee/edit/<int:id>/', views.employee_edit, name='employee_edit'),
     path('employee/delete/<int:id>/', views.employee_delete, name='employee_delete'),
     path('users/', views.user_list, name='user_list'),
     path('user/edit/', views.edit_profile, name='edit_profile'),
     path('users/add/', views.add_user, name='add_user'),
     path('users/edit/<int:user_id>/', views.edit_user, name='edit_user'),
     path('users/detail/<int:user_id>/', views.user_detail, name='user_detail'),
     path('accounts/edit-profile/', views.edit_profile, name='edit_profile'),
     path('logout/', views.logout_view, name='logout'),
   
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

