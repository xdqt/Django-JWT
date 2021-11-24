from .models import *
from rest_framework import serializers

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        
        
        
class TestTableSerializers(serializers.ModelSerializer):
    class Meta:
        model = TestTable
        fields = '__all__'