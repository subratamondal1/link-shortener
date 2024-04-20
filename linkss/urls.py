from django.urls import path

from .views import index

urlpatterns:list = [
    path(route="", view=index, name="index")
]
