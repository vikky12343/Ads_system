from django.db import models

# Create your models here.
class Ads(models.Model):

	Ads_Name=models.CharField(max_length=100)
	Title=models.CharField(max_length=100)
	detail=models.CharField(max_length=100)

