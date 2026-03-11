'''
1 Standard Library : none
2 Third-party: django, restframework 
3 Local application : none
'''
# 2-1 django 
from django.contrib.auth.models import User
# 2-2 django rest_framework
from rest_framework import serializers

class SignupSerializers(serializers.Serializer):
    username = serializers.CharField(max_length = 150)
    password = serializers.CharField(write_only = True, min_length=4)
    password2 = serializers.CharField(write_only = True, min_length = 4)

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("이미 사용중인 이름입니다.")
        
        return value
    
    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError({
                "password":"두 비밀번호가 일치하지 않습니다."
            })
        return attrs
        
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            password=validated_data["password"],
        )
        return user 
