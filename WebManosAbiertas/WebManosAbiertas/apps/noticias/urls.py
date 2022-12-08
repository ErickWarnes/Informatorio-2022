from django.urls import path
from .views import *

urlpatterns = [
    path("noticias", NoticiaListview.as_view)
]
