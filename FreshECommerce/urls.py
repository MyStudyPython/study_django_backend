"""FreshECommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.views.static import serve

# 重定向
from django.views.generic import RedirectView

# 导入路由
from rest_framework.routers import DefaultRouter

import xadmin

from .settings import MEDIA_ROOT

# from goods.views_base import GoodsListView
# from goods.views import GoodsListView
from goods.views import GoodsListViewSet

# from rest_framework.documentation import include_docs_urls

# ===================== 自动生成API文档=========================
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="生鲜电商",  # 必传
        default_version="v1",  # 必传
        description="这是一个接口文档",
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    # permission_classes=(permissions.AllowAny,),   # 权限类
)

router = DefaultRouter()

# 配置goods的路由
router.register("goods", GoodsListViewSet, basename="goods-list")

urlpatterns = [
    # path("xadmin/", xadmin.site.urls),
    # 这是直接把 /xadmin 设置为主页，但是没有指向
    # path("", xadmin.site.urls),
    # 这是直接指向了/docs
    # path("", RedirectView.as_view(url="/docs/")),
    # path("docs/", include_docs_urls(title="生鲜电商")),
    # ===================== 自动生成API文档=========================
    path("", RedirectView.as_view(url="/swagger/")),
    # 对测试人员更友好
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    # 对开发人员更友好
    path(
        "redoc/",
        schema_view.with_ui("redoc", cache_timeout=0),
        name="schema-redoc",
    ),
    path("xadmin/", xadmin.site.urls),
    path("media/<path:path>", serve, {"document_root": MEDIA_ROOT}),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    # 商品列表页api
    # path("goods/", goods_list, name="goods-list"),
    path("", include(router.urls)),
]
