from django.db import models

# Change "TEMPLATE" in file name with Language code 
# Change "TEMPLATE"s with Language code 
# import class in .__init__.py 
# register model in admin.py 

# Author template model
class Author_TEMPLATE(models.Model):
    author = models.OneToOneField('Author', on_delete=models.CASCADE)

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
        return 'TEMPLATE Author:  %s - %s' %(" ".join(self.LName()), self.author.author_id) 