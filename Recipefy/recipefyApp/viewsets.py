from django.shortcuts import render
from rest_framework import viewsets, filters

from .models import Users, User_Groceries, User_Preferences, Recipes, Login_logs
from .serializers import UsersSerializer, RecipesSerializer, User_Groceries_Serializer, User_Preferences_Serializer, Login_Logs_Serializer

class UsersViewSet(viewsets.ModelViewSet):
    queryset=Users.objects.all()
    serializer_class = UsersSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('username', 'email')

class RecipesViewSet(viewsets.ModelViewSet):
    queryset = Recipes.objects.all()
    serializer_class = RecipesSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('apple', 'rice','tomato','onion','orange','tea','chocolate','egg','lentil','potato','lemon','garlic','strawberry','vegan','poultry','organic','no_cook','no_sugar','lunch','high_fiber','healthy','grill','dinner','dairy_free','meal_22_minutes','appetizer')

class UserGroceriesViewSet(viewsets.ModelViewSet):
    queryset= User_Groceries.objects.all()
    serializer_class = User_Groceries_Serializer
    filter_backends = (filters.SearchFilter,)
    search_fields=('username','apple','rice','tomato','onion','orange','tea','chocolate','egg','lentil','potato','lemon','garlic','strawberry')

class UserPreferencesViewSet(viewsets.ModelViewSet):
    queryset = User_Preferences.objects.all()
    serializer_class = User_Preferences_Serializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('username','vegan','poultry','organic','no_cook','no_sugar','lunch','high_fiber','healthy','grill','dinner','dairy_free','meal_22_minutes','appetizer')

class LoginLogsViewSet(viewsets.ModelViewSet):
    queryset = Login_logs.objects.all()
    serializer_class = Login_Logs_Serializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('username','datetime')