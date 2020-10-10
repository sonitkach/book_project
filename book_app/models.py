from django.db import models

class Book (models.Model):
  title = models.CharField(max_length=100)
  author_name = models.CharField(max_length=100)
  description = models.TextField(blank=True)
  #id = models.AutoField(primary_key=True)

  def __str__(self):
    return (self.title)
