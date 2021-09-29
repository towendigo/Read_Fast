from django.contrib import admin
from .models import Author, Author_en, Author_tr
# Register your models here.

admin.site.register([Author, Author_en, Author_tr])