from pyexpat import model
from django.contrib import admin
from .models import Scheme, Incomes, Castes, Genders, Educations, Catagories, Documents
# Register your models here.
# admin.site.register(Scheme)


class IncomesInline(admin.StackedInline):
    model = Incomes
    can_delete = True
    verbose_name_plural = 'incomes'


class GendersInline(admin.StackedInline):
    model = Genders
    can_delete = True
    verbose_name_plural = 'genders'


class EducationsInline(admin.StackedInline):
    model = Educations
    can_delete = True
    verbose_name_plural = 'educations'


class CastesInline(admin.StackedInline):
    model = Castes
    can_delete = True
    verbose_name_plural = 'castes'


class CatagoriesInline(admin.StackedInline):
    model = Catagories
    can_delete = True
    verbose_name_plural = 'catagories'


class DocumentsInline(admin.StackedInline):
    model = Documents
    can_delete = True
    verbose_name_plural = 'documents'


class SchemeAdmin(admin.ModelAdmin):
    model = Scheme
    inlines = (IncomesInline, GendersInline, EducationsInline,
               CastesInline, CatagoriesInline, DocumentsInline)


admin.site.register(Scheme, SchemeAdmin)
