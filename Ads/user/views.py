from django.shortcuts import render
from .models import Ads 
from  .serializer import AdsModelserializer
from rest_framework.viewsets import ModelViewSet
# Create your views here.


class AdsViewSets(ModelViewSet):
	model=Ads
	serializer_class=AdsModelserializer
	permission_classes=()
	queryset=Ads.objects.all()

	def get_queryset(self):
		if 'Ads_Name' in self.request.GET:
			return Ads.objects.filter(Ads_Name=self.request.GET['Ads_Name'])
		else:
			return Ads.objects.all()









