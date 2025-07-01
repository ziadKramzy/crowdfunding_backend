
from django.urls import path,include
from .views import welcomeTest,register,loginUser,protected_route,custom_token_refresh
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView, 
#     TokenRefreshView      
# )
 
urlpatterns = [
    path('', welcomeTest, name='welcomeTest'),
    path('register', register, name='register'),
    path('login', loginUser, name='token_obtain_pair'),
    path('token/refresh', custom_token_refresh, name='token_refresh'),
    path('protected', protected_route, name='protected_route'),
    
]
