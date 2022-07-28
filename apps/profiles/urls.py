import imp
from django.urls import path 

from .views import AgentListAPIView, TopAgentsListAPIView, GetProfileAPIView, UpdateProfileAPIView

urlpatterns = [
    path('agents/all', AgentListAPIView.as_view(), name='agent-list'),
    path('top-agents/all', TopAgentsListAPIView.as_view(), name='top-agent-list'),
    path('me/', GetProfileAPIView.as_view(), name='profile-detail'),
    path('update/<str:username>/', UpdateProfileAPIView.as_view(), name='profile-update'),
]