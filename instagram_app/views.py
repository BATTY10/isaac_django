from django.shortcuts import render, redirect
from .models import Post, Comment
from .form import Create_Comment_Form, Create_PostForm
# Create your views here.


def home(request):
    all_post = Post.objects.all()
    context = {'all_post': all_post}
    return render(request, 'instagram_app/home.html', context)


def read_post(request, pk):
    single_post = Post.objects.get(id=pk)
    # comment = Comment.objects.get(id=pk)
    comment = Comment.objects.filter(story=single_post)

    create_comment = Create_Comment_Form()
    if request.method == "POST":
        create_comment = Create_Comment_Form(request.POST)
        if create_comment.is_valid():
            create_comment.save()
            return redirect('home')
    context = {"single_post": single_post,
               "comment": comment, 
              'create_comment': create_comment
               }
    return render(request, 'instagram_app/read_post.html', context)


def create_post(request):
    post = Create_PostForm()
    if request.method == 'POST':
        post = Create_PostForm(request.POST)
        if post.is_valid():
            post.save()
            return redirect('home')
    context = {'post': post}
    return render(request, 'instagram_app/create_post.html', context)

def update_post(request, pk):
    update_post_id = Post.objects.get(id=pk)
    post_update = Create_PostForm(instance=update_post_id)
    if request.method == 'POST':
        post_update = Create_PostForm(request.POST, instance=update_post_id)
        if post_update.is_valid():
            post_update.save()
            return redirect('/')
    context ={'post_update':post_update}
    return render(request, 'instagram_app/update_post.html', context)
    
    
def delete_post(request, pk):
    delete_post_id = Post.objects.get(pk=pk)
    delete_post_id.delete()
    return redirect('/')