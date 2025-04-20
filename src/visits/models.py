from django.db import models

class PageVisit(models.Model):
    # db -> table
    # id -> hidden -> primary key -> autofield -> 1, 2, 3, 4, 5, ..., n
    path = models.TextField(blank=True, null=True) # col
    timestamp = models.DateField(auto_now_add=True) # col
    pass
 