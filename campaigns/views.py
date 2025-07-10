from django.db.models import Q, F
from rest_framework.decorators import api_view , permission_classes, parser_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status,parsers
from campaigns.models import Campaign
from campaigns.serializers import CampaignSerializer
from datetime import datetime
from django.utils import timezone
from decimal import Decimal



def get_today():
    return timezone.now().date()

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
@parser_classes([parsers.MultiPartParser, parsers.FormParser, parsers.JSONParser])
@permission_classes([IsAuthenticated])
def create_project(request):
    obj = CampaignSerializer(data=request.data, context={'request': request})
    target_amount = request.data.get('target_amount')

    start_str = request.data.get('start_date')
    end_str = request.data.get('end_date')

    try:
        start_date = datetime.strptime(start_str, "%Y-%m-%d").date() if start_str else get_today()
        end_date = datetime.strptime(end_str, "%Y-%m-%d").date() if end_str else None
    except ValueError:
        return Response({"error": "Invalid date format. Use YYYY-MM-DD."}, status=400)

    if end_date and end_date < start_date:
        return Response({"error": "End date cannot be before start date."}, status=400)

    if target_amount is not None:
        if float(target_amount) < 0:
            return Response({'Error': 'Target amount cannot be negative'}, status=status.HTTP_403_FORBIDDEN)
    
    if obj.is_valid():
        obj.save()
        return Response(data={'msg': 'Campaign created successfully', 'Campaign': obj.data }, status=status.HTTP_201_CREATED)
    else:
        return Response(data={'msg': 'Failed to create Campaign', 'errors': obj.errors}, status=status.HTTP_400_BAD_REQUEST)



@api_view(['PUT'])
@parser_classes([parsers.MultiPartParser, parsers.FormParser, parsers.JSONParser])
@permission_classes([IsAuthenticated])
def update_campaign(request, pk):
    try:
        campaign = Campaign.objects.get(pk=pk)
    except Campaign.DoesNotExist:
        return Response({'detail': 'Campaign not found.'}, status=status.HTTP_404_NOT_FOUND)
    if campaign.owner != request.user:
        return Response({'detail': 'Not authorized to update this campaign.'}, status=status.HTTP_403_FORBIDDEN)

    serializer = CampaignSerializer(campaign, data=request.data, partial=True)

    target_amount = request.data.get('target_amount')
    start_str = request.data.get('start_date')
    end_str = request.data.get('end_date')

    try:
        start_date = datetime.strptime(start_str, "%Y-%m-%d").date() if start_str else campaign.start_date
        end_date = datetime.strptime(end_str, "%Y-%m-%d").date() if end_str else campaign.end_date
    except ValueError:
        return Response({"error": "Invalid date format. Use YYYY-MM-DD."}, status=400)

    if end_date and start_date and end_date < start_date:
        return Response({"error": "End date cannot be before start date."}, status=400)

    if target_amount is not None:
        if float(target_amount) < 0:
            return Response({'Error': 'Target amount cannot be negative'}, status=status.HTTP_403_FORBIDDEN)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def search_campaigns(request):
    title = request.GET.get('title', '')
    start_date = request.GET.get('start_date', None)
    end_date = request.GET.get('end_date', None)

    campaigns = Campaign.objects.all()
    if title:
        campaigns = campaigns.filter(title__icontains=title)

    try:
        if start_date:
            start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
            campaigns = campaigns.filter(start_date__gte=start_date)

        if end_date:
            end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
            campaigns = campaigns.filter(end_date__lte=end_date)
    except ValueError:
        return Response({'error': 'Invalid date format. Use YYYY-MM-DD.'}, status=status.HTTP_400_BAD_REQUEST)

    serializer = CampaignSerializer(campaigns, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def donate_campaign(request, pk):
    try:
        campaign = Campaign.objects.get(pk=pk)
    except Campaign.DoesNotExist:
        return Response({'error': 'Campaign not found.'}, status=status.HTTP_404_NOT_FOUND)

    amount = request.data.get('amount')

    if amount is None:
        return Response({'error': 'Amount is required.'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        amount = Decimal(amount)
    except ValueError:
        return Response({'error': 'Amount must be a number.'}, status=status.HTTP_400_BAD_REQUEST)

    if amount <= 0:
        return Response({'error': 'Amount must be positive.'}, status=status.HTTP_400_BAD_REQUEST)

    campaign.amount_raised = campaign.amount_raised + amount
    campaign.save()

    serializer = CampaignSerializer(campaign)
    return Response({'message': 'Donation received', 'campaign': serializer.data}, status=status.HTTP_200_OK)