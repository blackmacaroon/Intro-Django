from django.contrib import admin

from .models import CrapMapApp
from .models import PersonalNote
# Register your models here.

class NoteAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

admin.site.register(CrapMapApp, NoteAdmin)
admin.site.register(PersonalNote, NoteAdmin)
