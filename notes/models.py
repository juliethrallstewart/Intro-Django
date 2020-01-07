from django.db import models
from uuid import uuid4


# id = Default calls a function to randomly generate a unique identifier.

#auto_now_add only sets on create, while auto_now will set on both create and update.

class Note(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

#You might notice that the new fields aren’t showing up in the admin interface. This is because when you use auto_now, the field gets set to read-only, and such fields aren’t shown in the panel.

#To get the read-only fields to show up in the interface add this into notes/admin.py:

# class NoteAdmin(admin.ModelAdmin):
#     	readonly_fields=('created_at', 'last_modified')

# admin.site.register(Note, NoteAdmin)