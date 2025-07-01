from django.urls import path,include
from .views import  list_all_projects , delete_project
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView, 
#     TokenRefreshView      
# )
 
urlpatterns = [
    path('projects/', list_all_projects, name='list-projects'),
    path('projects/<int:pk>/delete/', delete_project, name='delete-project'),
    
]
