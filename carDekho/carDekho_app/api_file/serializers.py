from rest_framework import serializers
from ..models import Carlist


# class CarSerializer(serializers.Serializer):
#   id = serializers.IntegerField(read_only=True)
#   name = serializers.CharField()
#   description = serializers.CharField()
#   active = serializers.BooleanField(read_only=True)

class CarSerializer(serializers.Serializer):
  id = serializers.IntegerField(read_only=True)
  name = serializers.CharField()
  description = serializers.CharField()
  active = serializers.BooleanField(read_only=True)
  
  def create(self,validate_data):
    return Carlist.objects.create(**validate_data)
  
 
  
  def update(self,instance,validate_data):
    instance.name = validate_data.get('name',instance.name)
    instance.description = validate_data.get('description',instance.description)
    instance.active = validate_data.get('active',instance.active)
    instance.chassisNumber = validate_data.get('chassisNumber',instance.chassisNumber)
    instance.price = validate_data.get('price',instance.price)
    
    instance.save()
    return instance