from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post

# Create your views here.

def HomeView(request):
    return render(request, 'HomeApp/HomePage.html')

def CreatePostView(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('HomeApp:ViewHome')
    else:
        form = PostForm()

    return render(request, 'HomeApp/PostPage.html', {'form': form})

def ViewPostView(request):
    get_posts = Post.objects.all()
    context = {'PostData':get_posts}
    return render(request, 'HomeApp/ViewPostPage.html', context)