from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from campaigns.models import Campaign
from campaigns.serializers import CamapaignSerialzer


@api_view(['GET'])
def list_all_projects(request):
    campaigns = Campaign.objects.all()
    campaigns_json = CamapaignSerialzer(campaigns, many=True)

    return Response(data= campaigns_json.data  , status=status.HTTP_200_OK)  

@api_view(['DELETE'])
def delete_project(request, pk):
    try:
        campaign = Campaign.objects.get(pk=pk)
        campaign.delete()
        return Response({'message': 'Campaign deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)
    except Campaign.DoesNotExist:
        return Response({'error': 'Campaign not found.'}, status=status.HTTP_404_NOT_FOUND)
