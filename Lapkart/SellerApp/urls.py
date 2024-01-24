from django.urls import path
from . import views

urlpatterns=[
    path("add/",views.add_laptop),
    path("show/",views.show_laptops),
    path("update/<i>/",views.update_laptop),
    path("delete/<j>/",views.delete_laptop),
]