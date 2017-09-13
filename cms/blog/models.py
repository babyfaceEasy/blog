from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
	STATUS_CHOICES = (
		('draft', 'Draft'),
		('published', 'Published'),
	)

	title = models.CharField(max_length=250)
	slug =  models.SlugField(max_length=250)
	content = models.TextField()
	seo_title = models.CharField(max_length=250)
	seo_description = models.CharField(max_length=160)
	author = models.ForeignKey(User, related_name='blog_posts')
	published = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	update = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=9, choices=STATUS_CHOICES, default='draft')

	def __str__(self):
		return self.title

