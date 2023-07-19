Django Restful framework简称**DRF**，可以查看官方文档https://www.django-rest-framework.org/，从官方文档可以看到，Django REST框架是用于构建Web API的功能**强大且灵活**的工具包。

使用REST框架的一些原因：
该网站可浏览API是你的开发人员一个巨大的可用性胜利；
身份验证策略，包括OAuth1a和OAuth2的软件包；
支持ORM和非ORM数据源的序列化；
完全可自定义；
广泛的文档资料以及强大的社区支持。

要使用DRF，还需要DRF所依赖的第三方库django-guardian、coreapi，直接通过`pip install django-guardian coreapi`命令添加即可，还需要在settings.py中进行配置：
```diff
INSTALLED_APPS = [
      'django.contrib.auth',
      'django.contrib.contenttypes',
      'django.contrib.sessions',
      'django.contrib.messages',
      'django.contrib.staticfiles',
      'apps.users.apps.UsersConfig',
      'goods.apps.GoodsConfig',
      'trade.apps.TradeConfig',
      'user_operation.apps.UserOperationConfig',
      'DjangoUeditor',
      'xadmin',
      'crispy_forms',
+     'django.contrib.admin',
+     'rest_framework',
]

```

# 1.使用serializer实现基本序列化
通过DRF实现商品列表页的原理是：
通过DRF返回数据，基于**CBV**（Class-based Views， 即基于类的视图）方式编码。

urls.py中配置路径：
```diff
  from django.urls import path
  from django.views.static import serve
  from django.views.generic import RedirectView

  import xadmin

  from FreshECommerce.settings import MEDIA_ROOT

  from goods.views_base import GoodsListView
+ from rest_framework.documentation import include_docs_urls

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
+     # 文档路由
+     path("docs/", include_docs_urls(title="生鲜电商")),
]
```

apps/goods下新建serializers.py如下：
```python
from rest_framework import serializers


class GoodsSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, max_length=300)
    click_num = serializers.IntegerField(default=0)

```

现在建立基于类的视图CBV，apps/goods/views.py如下：
```python
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Goods
from .serializers import GoodsSerializer

# Create your views here.

class GoodsListView(APIView):
    '''商品序列化'''
    def get(self, request, format=None):
        goods = Goods.objects.all()[:10]
        goods_serializer = GoodsSerializer(goods, many=True)
        return Response(goods_serializer.data)

```

urls.py修改如下：

```python
from django.conf.urls import url, include
from django.views.static import serve
from rest_framework.documentation import include_docs_urls

import xadmin
from .settings import MEDIA_ROOT
# from goods.views_base import GoodsListView
from goods.views import GoodsListView

urlpatterns = [
       url(r'^xadmin/', xadmin.site.urls),
       url(r'^media/(?P<path>.*)$', serve, {'document_root':MEDIA_ROOT}),
       url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

       # 商品列表页
       url(r'goods/$', GoodsListView.as_view(), name='goods-list'),

       # 文档路由
       url(r'docs/', include_docs_urls(title='生鲜电商'))
]

```

此时再访问http://127.0.0.1:8000/goods/，显示：

![](https://img-blog.csdnimg.cn/20200725154650449.gif)

显然，此时还是显示出了数据，并且经过restful_framework优化，不是单纯地显示json数据，而且可以通过json和API两种方式查看，还能查看OPTIONS数据。

如果报错`__str__ returned non-string (type NoneType)` ，可以通过退出登录后台管理或者修改自定义的用户模型的`__str__()`方法解决，具体可参考

https://blog.csdn.net/CUFEECR/article/details/107469168。