from django.db import models
#models essentially represent database items

# Create your models here.
class PlayerSearch(models.Model):#This one doesnt do anything right now
    search_text = models.CharField(max_length=200)
