from django.db import models


# Author template model
class Author_tr(models.Model):
    author = models.OneToOneField('Author', unique=True, on_delete=models.CASCADE)

    local_name =  models.CharField(max_length=300, null=True, blank=True)
    local_surname =  models.CharField(max_length=300, null=True, blank=True)
    local_life = models.TextField(max_length=10000, null=True, blank=True)
    
    def LName(self):
        name = [self.author.author_name, self.author.author_surname]
        
        if self.local_name:
            name[0] = "%s" %(self.local_name)
        if self.local_surname:
            name[1] = "%s" %(self.local_surname)

        return name
    
    def LLife(self):
        if self.local_life:
            return "%s" %(self.local_life)
        else:
            return False

    def __str__(self) -> str:
        return '(tr) Author:  %s - %s' %(" ".join(self.LName()), self.author.author_id) 