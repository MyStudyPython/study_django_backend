from rest_framework import mixins, viewsets, filters

# from rest_framework.views import APIView
# from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend

from .models import Goods, GoodsCategory
from .serializers import GoodsSerializer, CategorySerializer
from .filters import GoodsFilter  # 导入自定义模糊匹配过滤器

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
    """商品列表页，并实现分页、搜索、过滤、排序"""

    # queryset = Goods.objects.all()
    queryset = Goods.objects.all().order_by("goods_sn")
    serializer_class = GoodsSerializer
    pagination_class = GoodsPagination
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    # 这里需要将 filter_class 改为 filterset_class
    filterset_class = GoodsFilter

    # 新增搜索
    # search_fields = ["name", "goods_brief", "goods_desc"]
    # 取消模糊匹配
    search_fields = ["=name", "goods_brief", "goods_desc"]

    # 新增排序
    ordering_fields = ["sold_num", "market_price"]


# class CategoryViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
# mixins.RetrieveModelMixin 是一个用于处理获取单个对象详情的混合类。当你在视图集中使用该混合类时，它会自动配置路由来处理 GET 请求，并使用对象的 ID 或其他唯一标识来获取该对象的详情
class CategoryViewSet(
    mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet
):
    """商品分类列表数据"""

    queryset = GoodsCategory.objects.all()
    serializer_class = CategorySerializer
