from django.db import models


class News(models.Model):
	title = models.CharField(max_length=200)
	body = models.TextField()
	reporter_id = models.IntegerField()
	reporter_country_id = models.IntegerField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)



	def __str__(self):
		return self.title


