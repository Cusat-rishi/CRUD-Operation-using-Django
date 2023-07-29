from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("insert", views.insertData, name="insertSata"),
    # If it will not insert the data then close url manage.py ctrl+c or x and then run command python manage.py migrate and again runserver then it will give accurate result
    # and check the inserted data in terminal and focus every time on cmd warnings
    path("insert", views.insertData, name="insertData"),
    path("update/<id>", views.updateData, name="updateData"),
    path("delete/<id>", views.deleteData, name="deleteData"),
]
