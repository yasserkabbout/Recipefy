from rest_framework import serializers
from recipefyApp import models

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Users
        fields='__all__'

class RecipesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Recipes
        fields='__all__'

class User_Preferences_Serializer(serializers.ModelSerializer):
    class Meta:
        model = models.User_Preferences
        fields='__all__'

class User_Groceries_Serializer(serializers.ModelSerializer):
    class Meta:
        model = models.User_Groceries
        fields='__all__'

class Login_Logs_Serializer(serializers.ModelSerializer):
    class Meta:
        model = models.Login_logs
        fields='__all__'