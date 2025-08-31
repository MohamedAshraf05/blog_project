from django.shortcuts import render , redirect , HttpResponse
from .models import Post
# Create your views here.

def get_posts(request):
    posts = Post.objects.all()
    context = {"posts" : posts}
    return render(request , "posts/post_list.html" , context)

def add_post(request):
    if request.method == "POST":
        post_title = request.POST.get("post_title")
        post_content = request.POST.get("post_text")
        Post.objects.create(title=post_title , content=post_content)
        return redirect("all")
    return render(request , "posts/post_list.html")


def delete_post(request , post_id):
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        HttpResponse("Post is not exist")
    
    post.delete()
    return redirect("all")
    
def post_detail(request , post_id):
    
    post = Post.objects.get(id=post_id)

    if post:
        context = {"post" : post}
        return render(request , "posts/post_detail.html" , context)
    