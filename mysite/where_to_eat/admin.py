from django.contrib import admin
from where_to_eat.models import Ballot, Restaurant

class RestaurantInline(admin.TabularInline):
    model = Restaurant
    extra = 2

class BallotAdmin(admin.ModelAdmin):
    fields = ['date']
    inlines = [RestaurantInline]
    list_filter = ['date']
    date_hierarchy = 'date'

admin.site.register(Ballot, BallotAdmin)
