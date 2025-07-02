from rest_framework import serializers
from .models import Campaign

# class CampaignSerialzer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(max_length=255)
#     description = serializers.CharField()
#     start_date = serializers.DateField()
#     end_date = serializers.DateField()
#     target_amount = serializers.DecimalField(max_digits=10, decimal_places=2)
#     owner = serializers.IntegerField()
        
class CampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaign
        fields = '__all__'
        read_only_fields = ['id', 'owner']

    def create(self, validated_data):
        validated_data['owner'] = self.context['request'].user
        return super().create(validated_data)
