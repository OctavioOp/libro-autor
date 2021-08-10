from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('libro',views.libro),

]
