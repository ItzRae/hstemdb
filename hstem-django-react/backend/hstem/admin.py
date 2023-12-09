from django.contrib import admin
from .models import Author
from .models import Project
from .models import Create
from .models import File
from .models import Department
from .models import Sponsor


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'major', 'year')

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'primary_theme', 'secondary_theme', 'audience', 'link_to_file ', 'thumbnail_url')

class CreateAdmin(admin.ModelAdmin):
    list_display = ('date', 'name', 'title')

class FileAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_public', 'type', 'title')

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('school',)

class SponsorAdmin(admin.ModelAdmin):
    list_display = ('title', 'school')

# Register your models here.
admin.site.register(Author, AuthorAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Create, CreateAdmin)
admin.site.register(File, FileAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Sponsor, SponsorAdmin)


