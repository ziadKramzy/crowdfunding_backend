from rest_framework import serializers

class CamapaignSerialzer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=255)
    description = serializers.CharField()
    start_date = serializers.DateField()
    end_date = serializers.DateField()
    target_amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    owner = serializers.IntegerField()
