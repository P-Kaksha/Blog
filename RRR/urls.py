from django.urls import path
from . import views

urlpatterns = [
    path('test/',views.kak,name='test'),
    path('story/',views.story,name='Goal'),
    path('goal/',views.Goal,name='Arc'),
]