from django.urls import path
from .views import *
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView, 
#     TokenRefreshView      
# )

urlpatterns = [
    path('projects/', list_all_projects ),
    path('projects/<int:pk>/', get_project ),
    path('projects/<int:pk>/delete/', delete_project ),
    path('projects/create/', create_project),
    path('projects/<int:pk>/update/', update_campaign ),
    path('projects/search/', search_campaigns),
]
