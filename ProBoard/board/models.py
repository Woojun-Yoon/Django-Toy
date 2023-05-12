from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class Topic(models.Model):
	subject = models.CharField(max_length=255)
	last_updated = models.DateTimeField(auto_now_add=True)
	message = models.TextField(max_length=4000, null=True)
	writter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='topics', null=True)

class Reply(models.Model):
	message = models.TextField(max_length=4000)
	created_at = models.DateTimeField(auto_now_add=True)
	created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts', null=True)
	updated_at = models.DateTimeField(null=True)
	updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+', null=True)