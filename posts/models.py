from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=100)
    images = models.ImageField(upload_to="images/" , default="")
    def __str__(self):
        return f"{self.name}"

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE , default="")
    def __str__(self):
        return f"{self.title} - {self.author}"

