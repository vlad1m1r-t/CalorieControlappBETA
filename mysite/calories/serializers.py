from rest_framework import serializers

from calories.models import Visitor


class CaloriesSerializer(serializers.ModelSerializer):
    nameProduct = serializers.StringRelatedField()
    class Meta:
        model = Visitor
        fields = ('time_create', 'userid', 'nameProduct', 'amount', 'caldj', 'protein', 'fat', 'carbohydrates')