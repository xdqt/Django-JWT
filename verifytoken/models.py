from django.db import models
class User(models.Model):
    user_name = models.CharField(max_length=200)
    user_email = models.EmailField(blank=False,null=False)
    user_password = models.CharField(max_length=200)
    
    class Meta:
        db_table = "userinfo"
        
class TestTable(models.Model):
    user_name = models.CharField(max_length=200)
    user_id = models.IntegerField()
    
    class Meta:
        db_table = 'testtable'

# Create your models here.
