from django.contrib import admin

from .models import CrapMapApp
from .models import PersonalNote
# Register your models here.

class NoteAdmin(admin.ModelAdmin):
    readonly_fields = ('id',) #comma because must be list or tuple

admin.site.register(CrapMapApp, NoteAdmin)
admin.site.register(PersonalNote, NoteAdmin)
