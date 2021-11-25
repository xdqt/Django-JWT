from django.db import models

        
class TestTable(models.Model):
    user_name = models.CharField(max_length=200)
    user_id = models.IntegerField()
    
    class Meta:
        db_table = 'testtable'

# Create your models here.
