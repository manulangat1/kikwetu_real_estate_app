from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view, permission_classes 
from rest_framework.response import Response
from rest_framework import permissions  , status
from apps.profiles.models import Profile 
from .models import Rating
# Create your views here.


User = get_user_model()

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def create_agent_review(request, profile_id):
    agent_profile = Profile.objects.get(id=profile_id, is_agent=True)
    data = request.data

    profile_user = User.objects.get(pkid=agent_profile.user.pkid)

    if profile_user.email == request.user.email:
        return Response({"message": "You cannot review yourself"}, status=status.HTTP_400_BAD_REQUEST) 

    alreadyExists = agent_profile.agent_reviews.filter(agent__pkid=profile_user.pkid).exists() 
    if alreadyExists:
        content = { "detail": "You have already reviewed this agent"}
        return Response(content, status=status.HTTP_403_BAD_REQUEST)
    elif data['rating'] == 0:
        content = { "detail": "You cannot give a rating of 0"}
        return Response(content, status=status.HTTP_400_BAD_REQUEST)
    else: 
        rating = Rating.objects.create(rater=request.user, agent=agent_profile, rating=data['rating'], comment=data['comment'])
        reviews = agent_profile.agent_reviews.all()
        agent_profile.num_reviews = len(reviews)
        total = 0 
        for  i in reviews:
            total += i.rating
        content = { "detail": "Rating created successfully"}
        return Response(content, status=status.HTTP_201_CREATED)


