from rest_framework import serializers
from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    customer = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Order
        fields = '__all__'

    def perform_create(self, serializer):
        serializer.save(customer=self.request.user)
        return super().perform_create(serializer)


