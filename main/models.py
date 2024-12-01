from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    contact = models.EmailField()

    def __str__(self):
        return self.name

class Material(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    link = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
