from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS = ((0, 'Draft'), (1, 'Published'))


# Post model
class Post(models.Model):
    """
    Post model
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    featured_image = CloudinaryField('image', default='Placeholder')
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)

    class Meta:
        """
        Descendeing order according to date created
        """
        ordering = ['-created_on']

    def __str__(self):
        """
        To return title
        """
        return self.title

    def number_of_likes(self):
        """
        Return the total count of likes in a post
        """
        return self.likes.count()


# Comments model
class Comment(models.Model):
    """
    Model for the comment section
    """
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        """
        Descending order to show latest comment
        """
        ordering = ['created_on']
    
    def __str__(self):
        """
        To return a string about the comment
        """
        return f'Comment {self.body} by {self.name}'
