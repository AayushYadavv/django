from django.urls import path
from .views import *
urlpatterns = [
    path('', HomePageView.as_view(), name= 'index'),
    path('incidences/', IncidenceData, name='incidence'),
    path('rails/', railsData, name='rails'),
    path('roads/', roadsData, name='roads'),
    path('waterways/', waterData, name='water'),
    path('county/', CountyData, name='counties'),
    path('country/', CountryBData, name='countries'),
    path('Agriculture/', Agriculture.as_view(), name='Agriculture'),
    path('Climate/', Climate.as_view(), name='Climate'),
    path('Resources/', Resources.as_view(), name='Resources'),
    path('Population/', Population.as_view(), name='Population'),
    path('Dams/', Dams.as_view(), name='Dams'),
    path('States/', States.as_view(), name='States'),
    path('Maharashtra/', Maharashtra.as_view(), name='Maharashtra'),
    path('MadhyaPradesh/', MadhyaPradesh.as_view(), name='MadhyaPradesh'),
    path('Punjab/', Punjab.as_view(), name='Punjab'),
    path('Gujrat/', Gujrat.as_view(), name='Gujrat'),
    path('Rajasthan/', Rajasthan.as_view(), name='Rajasthan'),
    ]
