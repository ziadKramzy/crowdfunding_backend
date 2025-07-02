from rest_framework.decorators import api_view , permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from campaigns.models import Campaign
from campaigns.serializers import CampaignSerializer



@api_view(['GET'])
def list_all_projects(request):
    campaigns = Campaign.objects.all()
    campaigns_json = CampaignSerializer(campaigns, many=True)

    return Response(data= campaigns_json.data  , status=status.HTTP_200_OK)  

@api_view(['GET'])
def get_project(request, pk):
    try:
        campaign = Campaign.objects.get(pk=pk)
        serialized = CampaignSerializer(campaign)
        return Response(data=serialized.data, status=status.HTTP_200_OK)
    except Campaign.DoesNotExist:
        return Response({'error': 'Campaign not found'}, status=status.HTTP_404_NOT_FOUND)



@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_project(request, pk):
    try:
        campaign = Campaign.objects.get(pk=pk)
    except Campaign.DoesNotExist:
        return Response({'error': 'Campaign not found.'}, status=status.HTTP_404_NOT_FOUND)

    if campaign.owner != request.user:
        return Response({'error': 'Not authorized to delete this campaign.'}, status=status.HTTP_403_FORBIDDEN)

    campaign.delete()
    return Response({'message': 'Campaign deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_project(request):
    obj = CampaignSerializer(data=request.data, context={'request': request})
    if obj.is_valid():
        obj.save()
        return Response(data={'msg': 'Campaign created successfully'}, status=status.HTTP_201_CREATED)
    else:
        return Response(data={'msg': 'Failed to create Campaign', 'errors': obj.errors}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_campaign(request, pk):
    try:
        campaign = Campaign.objects.get(pk=pk)
    except Campaign.DoesNotExist:
        return Response({'detail': 'Campaign not found.'}, status=status.HTTP_404_NOT_FOUND)
    if campaign.owner != request.user:
        return Response({'detail': 'Not authorized to update this campaign.'}, status=status.HTTP_403_FORBIDDEN)

    serializer = CampaignSerializer(campaign, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)