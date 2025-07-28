from django.contrib import admin
from django.utils.html import format_html
from .models import Tourist, Message, Place


@admin.register(Tourist)
class TouristAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'second_name', 'email', 'nationality', 'date', 'phone', 'amount')
    search_fields = ('first_name', 'second_name', 'email', 'phone')
    list_filter = ('nationality', 'date')
    ordering = ('-date',)
    fieldsets = (
        ('Personal Information', {
            'fields': ('first_name', 'second_name', 'email', 'phone')
        }),
        ('Booking Details', {
            'fields': ('nationality', 'date', 'amount')
        }),
    )


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'sent_at')
    search_fields = ('name', 'email', 'message')
    list_filter = ('sent_at',)
    readonly_fields = ('sent_at',)
    date_hierarchy = 'sent_at'
    fields = ('name', 'email', 'message', 'sent_at')


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'best_time_to_visit', 'entry_fee', 'created_at', 'preview_image')
    search_fields = ('name', 'description')
    list_filter = ('created_at', 'entry_fee')
    readonly_fields = ('created_at', 'preview_image')
    fieldsets = (
        (None, {
            'fields': ('name', 'description')
        }),
        ('Visitor Information', {
            'fields': ('best_time_to_visit', 'entry_fee')
        }),
        ('Media', {
            'fields': ('image', 'preview_image')
        }),
        ('Metadata', {
            'fields': ('created_at',)
        }),
    )

    def preview_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height: 200px; max-width: 300px;" />', obj.image.url)
        return "No Image Available"
    preview_image.short_description = 'Image Preview'
