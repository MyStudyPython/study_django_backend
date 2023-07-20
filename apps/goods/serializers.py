from rest_framework import serializers

from .models import Goods, GoodsCategory


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = "__all__"


class GoodsSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Goods
        # fields = [
        #     "category",
        #     "name",
        #     "sold_num",
        #     "shop_price",
        #     "goods_brief",
        #     "goods_front_image",
        #     "is_hot",
        # ]
        fields = "__all__"
