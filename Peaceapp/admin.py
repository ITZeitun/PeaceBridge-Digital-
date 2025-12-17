from django.contrib import admin
from .models import Donation, ContactMessage

@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ('contact', 'amount', 'time')
    search_fields = ('contact',)

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'time_created')
    search_fields = ('name', 'email')
