from django.db import models

# Create your models here.
#makemigration - create changes and store in a file
#migrate - apply the pending changes created by makemigration 
class contact(models.Model):
    name =models.Charfield(max_length = 122)
    email =models.Charfield(max_length = 122)
    phone =models.Charfield(max_length = 122)
    
    desc = models.Charfield ()
    date = models.DateField () 

    def_str_(self)
       return self.name