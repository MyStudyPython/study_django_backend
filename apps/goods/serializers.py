from rest_framework import serializers

from .models import Goods


class GoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goods
        fields = [
            "category",
            "name",
            "sold_num",
            "shop_price",
            "goods_brief",
            "goods_front_image",
            "is_hot",
        ]
