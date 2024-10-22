from django.db import models

class Post(models.Model):
    author = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='posts/')
    mood = models.CharField(max_length=100, blank=True, null=True)
    pinned = models.BooleanField(default=False)
    company_name = models.CharField(max_length=100, blank=True, null=True)  # For custom posts

    def clean(self):
        if self.pinned:
            Post.objects.filter(pinned=True).update(pinned=False)

    def __str__(self):
        return self.title
