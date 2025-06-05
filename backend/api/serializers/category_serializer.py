from rest_framework import serializers
from ..models import Category



# dev_5
class CategorySimpleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ["id", "name"]


