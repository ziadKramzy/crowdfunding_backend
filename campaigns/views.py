from django.db.models import F
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
    start_str = request.GET.get('start')
    end_str = request.GET.get('end')
    title_query = request.GET.get('title')
    sort_field = request.GET.get('sort', 'start_date')
    sort_order = request.GET.get('order', 'asc')

    try:
        start_date = datetime.strptime(start_str, "%Y-%m-%d").date() if start_str else None
        end_date = datetime.strptime(end_str, "%Y-%m-%d").date() if end_str else None
    except ValueError:
        return Response({"error": "Invalid date format. Use YYYY-MM-DD."}, status=status.HTTP_400_BAD_REQUEST)

    # Base queryset
    campaigns = Campaign.objects.all()

    # Exclude logically invalid campaigns: end < start
    campaigns = campaigns.filter(end_date__gte=F('start_date'))

    # Filter by date range
    if start_date:
        campaigns = campaigns.filter(start_date__gte=start_date)
    if end_date:
        campaigns = campaigns.filter(end_date__lte=end_date)

    # Optional title search (case-insensitive)
    if title_query:
        campaigns = campaigns.filter(title__icontains=title_query)

    # Sorting
    if sort_order == 'desc':
        sort_field = f'-{sort_field}'
    campaigns = campaigns.order_by(sort_field)

    # Serialize results
    serialized = CampaignSerializer(campaigns, many=True)
    return Response(serialized.data, status=status.HTTP_200_OK)



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
    if (campaign.target_amount - amount) <= 0 :
        campaign.target_amount = 0
    else:
        campaign.target_amount = campaign.target_amount - amount

    campaign.save()

    serializer = CampaignSerializer(campaign)
    return Response({'message': 'Donation received', 'campaign': serializer.data}, status=status.HTTP_200_OK)