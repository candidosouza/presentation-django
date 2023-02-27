from django.contrib import admin

from events.models import Event, LandingPages, UserRegistration

class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'landing_page', 'active', 'created_at', 'updated_at')
    prepopulated_fields = {"slug": ("name",)}
    list_filter = ('landing_page', 'active')
    search_fields = ('name', 'landing_page__title')


class LandingPagesAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created_at', 'updated_at')
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ('title',)


admin.site.register(UserRegistration)
class UserRegistrationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at', 'updated_at')
    search_fields = ('name', 'email')


admin.site.register(Event, EventAdmin)
admin.site.register(LandingPages, LandingPagesAdmin)
