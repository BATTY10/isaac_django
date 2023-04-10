from django.shortcuts import render, redirect
from .models import Post, Comment
from .form import Create_Comment_Form
# Create your views here.


def home(request):
    all_post = Post.objects.all()
    context = {'all_post': all_post}
    return render(request, 'instagram_app/home.html', context)


def read_post(request, pk):
    single_post = Post.objects.get(id=pk)
    comment = Comment.objects.get(id=pk)
    # comment = Comment.objects.filter(story=single_post)

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
