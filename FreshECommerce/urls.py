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
from django.urls import path
from django.views.static import serve
from django.views.generic import RedirectView

import xadmin

from FreshECommerce.settings import MEDIA_ROOT

from goods.views_base import GoodsListView

urlpatterns = [
    # path("xadmin/", xadmin.site.urls),
    # 这是直接把 /xadmin 设置为主页，但是没有指向
    # path("", xadmin.site.urls),
    # 这是直接指向了/xadmin
    path("", RedirectView.as_view(url="/xadmin/")),
    path("xadmin/", xadmin.site.urls),
    # url(r'^media/(?P<path>.*)$', serve, {'document_root':MEDIA_ROOT}),
    path("media/<path:path>", serve, {"document_root": MEDIA_ROOT}),
    # 商品列表页api
    path("goods/", GoodsListView.as_view(), name="goods-list"),
]
