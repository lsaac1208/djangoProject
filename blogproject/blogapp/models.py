from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor.fields import RichTextField

class Post(models.Model):
    title = models.CharField(max_length=200)
    # content = models.TextField()
    content = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def post_detail(request, pk):
        post = get_object_or_404(Post, pk=pk)
        comments = post.comments.all()
        return render(request, 'blog/post_detail.html', {'post': post, 'comments': comments})

    def __str__(self):
        return self.title

class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(null=True)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text[:50] + '...'

class UserSettings(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    theme_color = models.CharField(max_length=7, default='#007bff')  # Default Bootstrap primary color
    font_size = models.IntegerField(default=14)