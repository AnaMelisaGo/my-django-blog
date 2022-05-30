from django.shortcuts import render
from django.views import generic
from .models import Post


class Postlist(generic.ListView):
    """
    Generic list view of Post model
    """
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    paginate_by = 6 # separate objects into 6 page
