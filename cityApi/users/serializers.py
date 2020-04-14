from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User, Group
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)

    class Meta:
        model = User
        fields = (
        	'id', 
        	'username', 
        	'email',
            'password',
            'password2',
        	'first_name', 
        	'last_name', 
        	'is_active', 
        	'is_staff', 
        	'is_superuser', 
        	'date_joined', 
        	'last_login', 
        	'user_permissions',
        	'groups')
        extra_kwargs = {
            'password':{'write_only':True},
            'date_joined':{'read_only':True},
            'last_login':{'read_only':True},
            'is_active':{'read_only':True},
            'is_staff':{'read_only':True},
            'is_superuser':{'read_only':True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password')
        password2 = validated_data.pop('password2')
        validated_data['is_staff'] = False
        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match.'})
        user  = super().create(validated_data)
        user.set_password(password)
        user.save()
        return user


class UpdateUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id', 
            'username', 
            'email',
            'first_name', 
            'last_name', 
            'is_active', 
            'is_staff', 
            'is_superuser', 
            'date_joined', 
            'last_login', 
            'user_permissions',
            'groups')
        extra_kwargs = {
            'date_joined':{'read_only':True},
            'last_login':{'read_only':True},
            'is_active':{'read_only':True},
            'is_staff':{'read_only':True},
            'is_superuser':{'read_only':True}
        }




# class CreateUserSerializer(serializers.ModelSerializer):
#     password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)

#     class Meta:
#         model = User
#         fields = (
#             'id',
#             'username', 
#             'email', 
#             'first_name', 
#             'last_name', 
#             'is_active', 
#             'is_staff', 
#             'is_superuser',
#             'password',
#             'password2',)
#         extra_kwargs = {
#             'password':{'write_only':True}
#         }

#     def create(self, validated_data):
#         password = validated_data.pop('password')
#         password2 = validated_data.pop('password2')
#         if password != password2:
#             raise serializers.ValidationError({'password': 'Passwords must match.'})
#         user  = super().create(validated_data)
#         user.set_password(password)
#         user.save()
#         return user

#     def update(self, instance, validated_data):
#         password = validated_data.pop('password')
#         password2 = validated_data.pop('password2')
#         user  = super().update(instance, validated_data)
#         user.set_password(password)
#         user.save()
#         return user

    # def save(self):
            
    #     password = self.validated_data.pop('password')
    #     password2 = self.validated_data.pop('password2')
        
    #     print(self.validated_data)

    #     user = User(**self.validated_data)

    #     if password != password2:
    #         raise serializers.ValidationError({'password': 'Passwords must match.'})

    #     user.set_password(password)
    #     user.save()
    #     return user

# class GroupSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Group
#         fields = ('name')
