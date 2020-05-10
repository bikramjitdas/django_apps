from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('spaceremove/', views.spaceremover, name='spaceremove'),
    path('capitalisefirst/', views.capitalisefirst, name='capitalisefirst'),
    path('charactercount/', views.charactercount, name='charactercount'),

]
