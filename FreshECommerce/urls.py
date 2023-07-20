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
from rest_framework.documentation import include_docs_urls

router = DefaultRouter()

# 配置goods的路由
router.register("goods", GoodsListViewSet)

urlpatterns = [
    # path("xadmin/", xadmin.site.urls),
    # 这是直接把 /xadmin 设置为主页，但是没有指向
    # path("", xadmin.site.urls),
    # 这是直接指向了/xadmin
    path("", RedirectView.as_view(url="/xadmin/")),
    path("xadmin/", xadmin.site.urls),
    path("media/<path:path>", serve, {"document_root": MEDIA_ROOT}),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    # 商品列表页api
    # path("goods/", goods_list, name="goods-list"),
    path("", include(router.urls)),
    # 文档路由
    path("docs/", include_docs_urls(title="生鲜电商")),
]
