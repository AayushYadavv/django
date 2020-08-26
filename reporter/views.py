from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from django.http import HttpResponse
from .models import County,Incidence,CountryB,rails,roads,water
class HomePageView(TemplateView):
    template_name = 'index.html'
    
from django.core.serializers import serialize
def IncidenceData(request):
        points= serialize('geojson', Incidence.objects.all())
        return HttpResponse(points,content_type='json')
    
def CountyData(request):
        counties = serialize('geojson', County.objects.all())
        return HttpResponse(counties,content_type='json')
    
def CountryBData(request):
        countries = serialize('geojson', CountryB.objects.all())
        return HttpResponse(countries,content_type='json')
    
def railsData(request):
        railways= serialize('geojson', rails.objects.all())
        return HttpResponse(railways,content_type='json')
def roadsData(request):
        roadways= serialize('geojson', roads.objects.all())
        return HttpResponse(roadways,content_type='json')
def waterData(request):
        waterways= serialize('geojson', water.objects.all())
        return HttpResponse(waterways,content_type='json')
class Agriculture(TemplateView):
    template_name = 'Agriculture.html'
class Climate(TemplateView):
    template_name = 'Climate.html'
class Resources(TemplateView):
    template_name = 'Resources.html'
class Population(TemplateView):
    template_name = 'Population.html'
class Dams(TemplateView):
    template_name = 'Dams.html'
class States(TemplateView):
    template_name = 'States.html'
class Maharashtra(TemplateView):
    template_name = 'maharashtra.html'
class MadhyaPradesh(TemplateView):
    template_name = 'MadhyaPradesh.html'
class Punjab(TemplateView):
    template_name = 'Punjab.html'
class Gujrat(TemplateView):
    template_name = 'gujrat.html'
class Rajasthan(TemplateView):
    template_name = 'Rajasthan.html'
