from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import Post
from django.shortcuts import render, redirect
from .forms import PostForm, CommentForm, PostEditForm
from .models import Post, PostVersion, OriginalPostContent
from AccountApp.models import Rating, WebUser
from .forms import RatingForm




def HomeView(request):
    return render(request, 'HomeApp/HomePage.html')

@login_required
def CreatePostView(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()

            # Save the original content of the post
            post_content = form.cleaned_data['content']
            OriginalPostContent.objects.create(post=post, content=post_content)

            return redirect('HomeApp:ViewHome')
    else:
        form = PostForm()

    return render(request, 'HomeApp/PostPage.html', {'form': form})


def ViewPostView(request):
    get_posts = Post.objects.all()
    context = {'PostData':get_posts}
    return render(request, 'HomeApp/ViewPostPage.html', context)

@login_required
def ViewPostDetail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    # Get the original post content
    original_version = OriginalPostContent.objects.filter(post=post).first()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            return redirect('HomeApp:ViewPostDetail', post_id=post_id)
    else:
        form = CommentForm()
    comments = post.comments.all()
    context = {'post': post, 'comments': comments, 'form': form, 'original_version': original_version}
    return render(request, 'HomeApp/ViewPostDetail.html', context)

@login_required
def ViewEditPost(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.method == 'POST':
        form = PostEditForm(request.POST, instance=post)
        if form.is_valid():
            content = form.cleaned_data['content']
            # Save the original post content
            PostVersion.objects.create(post=post, user=request.user, content=post.content)
            # Update the post content
            post.content = content
            post.save()
            return redirect('HomeApp:ViewPostDetail', post_id=post.id)
    else:
        form = PostEditForm(instance=post)

    context = {'post': post, 'form': form}
    return render(request, 'HomeApp/ViewEditPost.html', context)

@login_required
def ViewChangesVersion(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    # Get all versions of the post
    versions = PostVersion.objects.filter(post=post)

    # Get the original post content
    original_version = OriginalPostContent.objects.filter(post=post).first()

    context = {
        'post': post,
        'versions': versions,
        'original_version': original_version,
    }

    return render(request, 'HomeApp/ViewChangeVersion.html', context)

@login_required
def ViewRateUser(request, user_id):
    rated_user = WebUser.objects.get(id=user_id)
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.rater = request.user
            rating.rated_user = rated_user
            rating.save()
            return redirect('HomeApp:ViewPostView')
    else:
        form = RatingForm()
    return render(request, 'HomeApp/ViewRateUser.html', {'form': form})

@login_required
def ViewUserProfile(request, user_id):
    profile = get_object_or_404(WebUser, id=user_id)
    context = {'profile': profile}
    return render(request, 'HomeApp/ViewUserProfile.html', context)


def ViewDeletePost(request, post_id):
    if request.method == "POST":
        get_post = get_object_or_404(Post, pk=post_id)
        get_post.delete()
        return redirect("HomeApp:ViewPostView")

    return render(request, 'HomeApp/ViewDeletePost.html')