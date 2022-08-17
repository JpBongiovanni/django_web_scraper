from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('smrpg_stats', views.smrpg_stats, name="smrpg_stats")
]