from .models import item2item
from rest_framework import serializers, viewsets

class item2itemSerializer(serializers.ModelSerializer):
    class Meta:
        model = item2item
        fields = '__all__'

class item2itemViewSet(viewsets.ModelViewSet):
    queryset = item2item.objects.all()
    serializer_class = item2itemSerializer
