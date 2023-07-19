from rest_framework import serializers

from .models import Goods


class GoodsSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, max_length=300)
    click_num = serializers.IntegerField(default=0)
    goods_front_image = serializers.ImageField()

    def create(self, validated_data):
        """接受前端的数据并保存"""
        # return super().create(validated_data)
        return Goods.objects.create(**validated_data)
