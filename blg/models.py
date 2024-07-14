from django.db import models

# Create your models here.
class blog(models.Model):
    blog_name=models.CharField(max_length=50)
    blog_discription=models.TextField()
    author=models.CharField(max_length=50)
    created_on=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.blog_name


