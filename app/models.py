from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField  # type: ignore
# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextField(blank=True,null=True)
    imgbb_url = models.URLField(blank=True)
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('blog_detail', kwargs={'pk': self.pk}) 