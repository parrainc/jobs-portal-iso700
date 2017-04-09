import uuid
from django.db import models
from django.template.defaultfilters import slugify


class Tag(models.Model):
	name = models.CharField(max_length=60)

	def __str__(self):
		return self.name


class Job(models.Model):
	user = models.CharField(max_length=200, null=True, blank=True, default='Confidential')
	description = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now_add=True)
	tag = models.ManyToManyField(Tag)
	email = models.EmailField(max_length=150)
	title = models.CharField(max_length=200)
	slug = models.SlugField(editable=False, default=uuid.uuid4, unique=True)

	def __str__(self):
		return '%s | %s'%(self.title, self.user)

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = slugify(self.title)
		super(Job, self).save(*args, **kwargs)