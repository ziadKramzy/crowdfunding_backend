from django.urls import path
from .views import  list_all_projects , delete_project ,create_project , get_project
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView, 
#     TokenRefreshView      
# )

urlpatterns = [
    path('projects/', list_all_projects, name='list-projects'),
    path('projects/<int:pk>/', get_project, name='get-project'),
    path('projects/<int:pk>/delete/', delete_project, name='delete-project'),
    path('projects/create/', create_project, name='create-project'),
]
