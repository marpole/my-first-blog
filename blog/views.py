from django.shortcuts import render
<<<<<<< HEAD
from .models import Post
from django.utils import timezone

def post_list(request):
    Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

=======

# Create your views here.
>>>>>>> fbf5de20e057304d1ffe9cddecccc8308cdb61ac
