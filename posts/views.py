from django.shortcuts import render , redirect , HttpResponse
from .models import Post , Author
from django.views.generic import ListView , CreateView , UpdateView , DetailView , DeleteView , View
from django.urls import reverse_lazy
# Create your views here.


# Function based views FBV
# Class based Views CBV

# ORM -> Object relational mapig

# post.object.all() -> Query Select * from post
class PostsList(ListView):
    model = Post
    template_name = "posts/post_list.html"
    context_object_name = "blogs"

class PostDeleteView(DeleteView):
    model = Post
    template_name = "posts/post_confirm_delete.html"
    success_url = reverse_lazy("list")

class PostCreateView(CreateView):
    model = Post
    template_name = "posts/post_create.html"
    fields = ["title" , "content"]
    success_url = reverse_lazy("list")

class PostUpdate(UpdateView):
    model = Post
    template_name = "posts/post_update.html"
    fields = ["title" , "content"]
    success_url = reverse_lazy("list")

class PostDetail(DetailView):
    model = Post
    template_name = "posts/post_detail.html"
    context_object_name = "post"

class AuthorView(View):
    def get(self , request , pk=None):
        if pk:
            author = Author.objects.get(pk=pk)
            context = {"author" : author}
            return render(request , "posts/author_detail.html" , context)
        authors = Author.objects.all()
        context = {"authors" : authors}
        return render(request , "posts/authors.html" , context)
    def post(self , request):
        if request.method == "POST":
            name = request.POST.get("name")
            image = request.POST.get("image")

            Author.objects.create(name=name , image=image)
            return redirect("author_list")
        return render(request , "posts/author_create.html")
    