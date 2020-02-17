from django.contrib import admin

# Register your models here.
from .models import PersonExample, GenderExample

class PersonExampleAdmin(admin.ModelAdmin):
    pass

class GenderExampleAdmin(admin.ModelAdmin):
    pass

admin.site.register(PersonExample, PersonExampleAdmin)
admin.site.register(GenderExample, GenderExampleAdmin)