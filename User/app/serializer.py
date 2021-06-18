from rest_framework import serializers 
from app.models import AppUser
 
 
class AppUserSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = AppUser
        fields = ('id',
                  'Username',
                  'email',
                  'mobile')