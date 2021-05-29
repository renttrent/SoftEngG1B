from .models import DietPlan, Event, Exercise, Routine
from django.contrib import admin

# Register your models here.
admin.site.register(Event)
admin.site.register(DietPlan)
admin.site.register(Exercise)
admin.site.register(Routine)
