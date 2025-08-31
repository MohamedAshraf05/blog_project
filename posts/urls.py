from django.urls import path
from . import views

urlpatterns = [
    path("all/" , views.get_posts , name="all"),
    path("all/<int:post_id>/" , views.post_detail , name="detail"),
    path("add/" , views.add_post , name="add"),
    path("delete/<int:post_id>/" , views.delete_post , name="delete"),
]