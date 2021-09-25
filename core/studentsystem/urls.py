from django.urls import path
from . import views

urlpatterns=[
    path("", views.home, name="home"),
    path("add/", views.add,name="add"),
    path("detail/<int:id>",views.detail,name="detail"),
    path("edit/<int:id>",views.edit,name="edit"),
    path("delete/<int:id>",views.delete,name="delete")
]