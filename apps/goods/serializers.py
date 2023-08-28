from rest_framework import serializers

from .models import Goods, GoodsCategory


class TerCategorySerializer(serializers.ModelSerializer):
    """三级商品子类别序列化"""

    class Meta:
        model = GoodsCategory
        fields = "__all__"


class SecCategorySerializer(serializers.ModelSerializer):
    """二级商品子类别序列化"""

    # many=True 用于指定一个关联字段是多对多关系（ManyToMany）或一对多关系（ForeignKey 或 OneToOne)
    # 对于多对多关系字段，需要设置 many=True 参数；而对于一对多关系字段，不需要设置 many=True 参数。
    sub_cat = TerCategorySerializer(many=True)

    class Meta:
        model = GoodsCategory
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    """一级商品类别序列化"""

    sub_cat = SecCategorySerializer(many=True)

    class Meta:
        model = GoodsCategory
        fields = "__all__"


# class CategorySerializer(serializers.ModelSerializer):
#     """商品分类序列化"""

#     class Meta:
#         model = GoodsCategory
#         fields = "__all__"


class GoodsSerializer(serializers.ModelSerializer):
    """商品序列化"""

    category = CategorySerializer()

    class Meta:
        model = Goods
        fields = "__all__"
