from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('demand/', views.about, name='demand'),
    path('geography/', views.about, name='geography'),
    path('skills/', views.about, name='skills'),
    path('last_jobs/', views.about, name='last_jobs'),
]