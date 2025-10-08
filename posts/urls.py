from django.urls import path
from .views import PostsList , PostDeleteView , PostCreateView , PostUpdate , PostDetail , AuthorView
urlpatterns = [
    path("post-list/" , PostsList.as_view() , name="list"),
    path("delete/<int:pk>/", PostDeleteView.as_view() , name="delete"),
    path("add/" , PostCreateView.as_view() , name="add"),
    path("update/<int:pk>/" , PostUpdate.as_view() , name="update"),
    path("detail/<int:pk>/" , PostDetail.as_view() , name="detail"),
    path("author/" , AuthorView.as_view() , name="author_list"),
    path("author/<int:pk>/" , AuthorView.as_view() , name="author"),
    path("author/new/" , AuthorView.as_view() , name="new_author")
]