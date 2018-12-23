from rest_framework import routers
from recipefyApp.viewsets import UsersViewSet, RecipesViewSet, UserGroceriesViewSet, UserPreferencesViewSet, LoginLogsViewSet

router = routers.DefaultRouter()

router.register(r'Users', UsersViewSet)
router.register(r'Recipes', RecipesViewSet)
router.register(r'User_Groceries', UserGroceriesViewSet )
router.register(r'User_Preferences', UserPreferencesViewSet)
router.register(r'Login_Logs', LoginLogsViewSet)

