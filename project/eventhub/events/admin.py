from django.contrib import admin
from .models import Event, Reservation


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'venue',
        'date',
        'total_seats',
        'available_seats',
        'status',
        'created_at',
    )
    list_filter = ('status', 'date')
    search_fields = ('title', 'venue')
    ordering = ('date',)


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'attendee_name',
        'attendee_email',
        'event',
        'seats_reserved',
        'status',
        'created_at',
    )
    list_filter = ('status', 'created_at', 'event')
    search_fields = ('attendee_name', 'attendee_email', 'event__title')
    ordering = ('-created_at',)