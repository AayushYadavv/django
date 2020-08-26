

from django.contrib import admin
from .models import Incidence,County,CountryB,rails,roads,water

class IncidenceAdmin(admin.ModelAdmin):
        list_display = ('title','date_reported','location')
        search_fields = ('title',)
        filter_fields = ('title','date_reported')


class CountyAdmin(admin.ModelAdmin):
	list_display = 	('name_engli','name_0')
	search_fields = ('name_engli',)
	filter_fields=('name_engli','name_0')
	
class CountryBAdmin(admin.ModelAdmin):
	list_display = 	('name_long','name')
	search_fields = ('name_long',)
	filter_fields=('name_long','name')

class railsAdmin(admin.ModelAdmin):
	list_display = 	('fid_rail_d','f_code_des')
	
	filter_fields=	('fid_rail_d','f_code_des')
	
class waterAdmin(admin.ModelAdmin):
	list_display = 	('country','f_code_des')
	
	filter_fields=	('country','f_code_des')

admin.site.register(County, CountyAdmin)
admin.site.register(Incidence, IncidenceAdmin)
admin.site.register(CountryB, CountryBAdmin)
admin.site.register(rails, railsAdmin)
admin.site.register(water, waterAdmin)
