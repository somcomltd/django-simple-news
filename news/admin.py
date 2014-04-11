from django.contrib import admin

from news.models import NewsItem, NewsAuthor, NewsCategory

class NewsCategoryAdmin(admin.ModelAdmin):
        list_display = ['name',]
        
        def queryset(self, request):
                return NewsCategory.on_site.all()
        
        def save_model(self, request, obj, form, change):
                obj.save()
                from django.contrib.sites.models import Site
                current_site = Site.objects.get_current()
                if current_site not in obj.sites.all():
                        obj.sites.add(current_site)

admin.site.register(NewsCategory, NewsCategoryAdmin)

class NewsItemAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':('title',)}
	list_display = ['title', 'date', 'site']
	list_filter = ['date']
	search_fields = ['title', 'body']
	date_hierarchy = 'date'
	ordering = ['-date']
	fieldsets = (
		('Article info', {
			'fields': ('title', 'body', 'date')
		}),
		('Advanced', {
			'classes': ['collapse'],
			'fields': ('snippet', 'slug',)
		}),
	)
	
	def queryset(self, request):
		return NewsItem.on_site.all()
		
admin.site.register(NewsItem, NewsItemAdmin)
