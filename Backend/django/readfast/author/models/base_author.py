from django.db import models
from readfast.model_loader import Multi_Loader_List
from .data import Country_Select
from .language import LanguageSet

# Base Author Model.
class Author(models.Model):
    author_id = models.BigAutoField(primary_key=True)

    author_name =  models.CharField(max_length=300, default="Unknown", null=False, blank=False)
    author_surname =  models.CharField(max_length=300, default="Unknown", null=False, blank=False)
    author_from =  models.CharField(max_length=2, choices=Country_Select , default="U0", null=False, blank=False)

    author_birth = models.DateField(null=True, blank=True)
    author_death = models.DateField(null=True, blank=True)

    author_photo = models.URLField(null=True, blank=True)

    def __str__(self) -> str:
        return '(base) Author: %s %s - %s' %(self.author_name, self.author_surname, self.author_id)

    
    def save(self, *args, **kwargs):

        super().save(*args, **kwargs)  # Call the "real" save() method.

        author_lans = LanguageSet().values()
        author_lans = Multi_Loader_List("author", author_lans)
        for author_lan in author_lans:
            author_child = author_lan(author=self)
            author_child.save()
    
