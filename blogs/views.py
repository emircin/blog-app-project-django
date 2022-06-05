from django.shortcuts import render, redirect, get_object_or_404
from blogs.forms import PostForm, CommentForm
from blogs.models import Post
from users.models import UserProfile

def list(request):
    return render(request, "blogs/post_list.html")

def tag_list(request):

    posts = Post.objects.all()

    context = {
        "posts":posts
    }
    print(posts)

    return render(request, "blogs/post_list.html", context)

def new_tag(request):
    form = PostForm()

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("list")


    context = {

       "form":form
    }

    return render(request, "blogs/post_create.html", context)

def tag_detail(request,id):
    post = Post.objects.get(id=id)
    context = {
        "post":post
    }

    return render(request, "blogs/post_detail.html", context)


def add_comment_to_post(request, id):
    post = get_object_or_404(Post, id=id)
    author = UserProfile.objects.get(user=request.user)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form.instance.user = author
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('tag_detail', id=post.id)
    else:
        form = CommentForm()
    return render(request, 'blogs/add_comment_to_post.html', {'form': form})

