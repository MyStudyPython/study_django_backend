from rest_framework import mixins, viewsets

# from rest_framework.views import APIView
# from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend

from .models import Goods
from .serializers import GoodsSerializer
from .filters import GoodsFilter # 导入自定义模糊匹配过滤器

# Create your views here.


class GoodsPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    page_query_param = "p"
    max_page_size = 100


# class GoodsListView(APIView):
#     """商品序列化"""

#     def get(self, request, format=None):
#         goods = Goods.objects.all()[:10]
#         goods_serializer = GoodsSerializer(goods, many=True)
#         return Response(goods_serializer.data)

#     def post(self, request, format=None):
#         serializer = GoodsSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class GoodsListView(mixins.ListModelMixin, generics.GenericAPIView):
# class GoodsListView(generics.ListAPIView):
#     """商品列表页"""

#     queryset = Goods.objects.all()
#     serializer_class = GoodsSerializer
#     pagination_class = GoodsPagination

#     # def get(self, request, *args, **kwargs):
#     #     return self.list(request, *args, **kwargs)


# class GoodsListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
#     """商品列表页"""

#     # queryset = Goods.objects.all().order_by("goods_sn")
#     # serializer_class = GoodsSerializer
#     # pagination_class = GoodsPagination

#     # def get_queryset(self):
#     #     queryset = Goods.objects.all().order_by("goods_sn")
#     #     price_min = self.request.query_params.get("price_min", default=0)
#     #     if price_min:
#     #         queryset = queryset.filter(shop_price__gt=int(price_min))

#     #     return queryset

#     # 通过django-filters的**DjangoFilterBackend**类实现字段过滤。
#     queryset = Goods.objects.all()
#     serializer_class = GoodsSerializer
#     pagination_class = GoodsPagination

#     filter_backends = [DjangoFilterBackend]
#     filterset_fields = ["name", "market_price"]

class GoodsListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    '''商品列表页'''

    # queryset = Goods.objects.all()
    queryset = Goods.objects.all().order_by("goods_sn")
    serializer_class = GoodsSerializer
    pagination_class = GoodsPagination
    filter_backends = [DjangoFilterBackend]
    filter_class = GoodsFilter