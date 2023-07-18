# xadmin后台管理系统的配置
xadmin是一个Django自带后台管理工具的替代品，可以直接使用pip install xadmin命令安装，但是由于通过这种方式安装的官方版本对版本2.1及以后的Django支持不友好，因此可点击https://download.csdn.net/download/CUFEECR/12647622 或者 https://github.com/sshwsfc/xadmin/tree/django2 下载修改后的版本，并将其解压放入extra_apps下。

然后在4个apps下分别创建`adminx.py`，
## apps/goods/adminx.py如下：
```python
import xadmin
from .models import Goods, GoodsCategory, GoodsImage, GoodsCategoryBrand, Banner

class GoodsAdmin(object):
    list_display = ["name", "click_num", "sold_num", "fav_num", "goods_num", "market_price",
                    "shop_price", "goods_brief", "goods_desc", "is_new", "is_hot", "add_time"]
    search_fields = ['name', ]
    list_editable = ["is_hot", ]
    list_filter = ["name", "click_num", "sold_num", "fav_num", "goods_num", "market_price",
                   "shop_price", "is_new", "is_hot", "add_time", "category__name"]
    style_fields = {"goods_desc": "ueditor"}

    class GoodsImagesInline(object):
        model = GoodsImage
        exclude = ["add_time"]
        extra = 1
        style = 'tab'

    inlines = [GoodsImagesInline]


class GoodsCategoryAdmin(object):
    list_display = ["name", "category_type", "parent_category", "add_time"]
    list_filter = ["category_type", "parent_category", "name"]
    search_fields = ['name', ]


class GoodsBrandAdmin(object):
    list_display = ["category", "image", "name", "desc"]

    def get_context(self):
        context = super(GoodsBrandAdmin, self).get_context()
        if 'form' in context:
            context['form'].fields['category'].queryset = GoodsCategory.objects.filter(category_type=1)
        return context


class BannerGoodsAdmin(object):
    list_display = ["goods", "image", "index"]


class HotSearchAdmin(object):
    list_display = ["keywords", "index", "add_time"]


class IndexAdAdmin(object):
    list_display = ["category", "goods"]


xadmin.site.register(Goods, GoodsAdmin)
xadmin.site.register(GoodsCategory, GoodsCategoryAdmin)
xadmin.site.register(Banner, BannerGoodsAdmin)
xadmin.site.register(GoodsCategoryBrand, GoodsBrandAdmin)
```

## apps/trade/adminx.py如下：
```python
import xadmin
from .models import ShoppingCart, OrderInfo, OrderGoods


class ShoppingCartAdmin(object):
    list_display = ["user", "goods", "nums", ]


class OrderInfoAdmin(object):
    list_display = ["user", "order_sn", "trade_no", "pay_status", "post_script", "order_mount",
                    "order_mount", "pay_time", "add_time"]

    class OrderGoodsInline(object):
        model = OrderGoods
        exclude = ['add_time', ]
        extra = 1
        style = 'tab'

    inlines = [OrderGoodsInline, ]


xadmin.site.register(ShoppingCart, ShoppingCartAdmin)
xadmin.site.register(OrderInfo, OrderInfoAdmin)

```

## apps/user_operation/adminx.py如下：
```python
import xadmin
from .models import UserFav, UserLeavingMessage, UserAddress


class UserFavAdmin(object):
    list_display = ['user', 'goods', "add_time"]


class UserLeavingMessageAdmin(object):
    list_display = ['user', 'message_type', "message", "add_time"]


class UserAddressAdmin(object):
    list_display = ["signer_name", "signer_mobile", "district", "address"]


xadmin.site.register(UserFav, UserFavAdmin)
xadmin.site.register(UserAddress, UserAddressAdmin)
xadmin.site.register(UserLeavingMessage, UserLeavingMessageAdmin)

```

## apps/users/adminx.py如下：
```python
import xadmin
from xadmin import views
from .models import VerifyCode


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = "生鲜后台"
    site_footer = "fresh_ec"


class VerifyCodeAdmin(object):
    list_display = ['code', 'mobile', "add_time"]


xadmin.site.register(VerifyCode, VerifyCodeAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)

```

## 将xadmin配置到settings.py中：
```diff
INSTALLED_APPS = [
      'django.contrib.auth',
      'django.contrib.contenttypes',
      'django.contrib.sessions',
      'django.contrib.messages',
      'django.contrib.staticfiles',
      'apps.users.apps.UsersConfig',
      'goods',
      'trade',
      'user_operation',
      'DjangoUeditor',
+     'xadmin'
]
```

# 数据库迁移
还需要安装xadmin的依赖包，从https://github.com/sshwsfc/xadmin/blob/master/requirements.txt 可以看到，包括django、django-crispy-forms、django-import-export、django-reversion、django-formtools、future、httplib2和six，可以直接使用一条命令`pip install django django-crispy-forms django-import-export django-reversion django-formtools future httplib2 six`安装即可。

此外，还需要安装xlwt和xlsxwriter，这主要用于操作Excel文件、使功能更完善，直接使用命令`pip install xlwt xlsxwriter`安装即可。
最后还需要对xadmin进行数据映射，即执行`makemigrations`和`migrate`即可。

如果遇到`ImportError: cannot import name 'six' from 'django.utils'`，可按照下面方法解决：

![](https://img-blog.csdnimg.cn/20200721182109240.gif)

如果遇到以下报错：
```sh
forms.Field.__init__(self, required, widget, label, initial, help_text,
TypeError: __init__() takes 1 positional argument but 6 were given
```
可直接在xadmin\views\dashboard.py中将`forms.Field.__init__(self, required, widget, label, initial, help_text, *args, **kwargs)`改为`forms.Field.__init__(self)`即可。

如果遇到其他问题，可参考https://blog.csdn.net/CUFEECR/article/details/104031620进行解决。

进行映射后，在Navicat用`SHOW TABLES;`进行查询数据库：
```sh
+------------------------------------+                   
| Tables_in_fresh_ec                 |                   
+------------------------------------+                   
| auth_group                         |                   
| auth_group_permissions             |                   
| auth_permission                    |                   
| django_content_type                |                   
| django_migrations                  |                   
| django_session                     |                   
| goods_banner                       |                   
| goods_goods                        |                   
| goods_goodscategory                |                   
| goods_goodscategorybrand           |                   
| goods_goodsimage                   |                   
| trade_ordergoods                   |                   
| trade_orderinfo                    |                   
| trade_shoppingcart                 |                   
| user_operation_useraddress         |                   
| user_operation_userfav             |                   
| user_operation_userleavingmessage  |                   
| users_userprofile                  |                   
| users_userprofile_groups           |                   
| users_userprofile_user_permissions |                   
| users_verifycode                   |                   
| xadmin_bookmark                    |                   
| xadmin_log                         |                   
| xadmin_usersettings                |                   
| xadmin_userwidget                  |                   
+------------------------------------+                   
25 rows in set (0.01 sec)                                
                                                        
```

显然，xadmin的数据表已经映射进数据库。

此时，还需要对xadmin配置访问路径，urls.py如下：

```diff
- from django.contrib import admin
+ from django.urls import path
+ import xadmin

urlpatterns = [
-    path('admin/', admin.site.urls),
+    path("xadmin/", xadmin.site.urls),
]
```

# 创建超级用户
此时还需要创建超级用户，在manage.py@Fresh Ecommerce窗口中执行createsuperuser命令，输入用户名、邮箱和密码后即可创建超级管理员。
```sh
python manage.py createsuperuser
```
![](https://img-blog.csdnimg.cn/img_convert/acf15e5baa9b51ccf8284a3c70005e65.png)

然后访问http://127.0.0.1:8000/xadmin/ 如下：
![](https://img-blog.csdnimg.cn/20200721182142503.gif)

## 对settings.py配置
显然，此时可以（用刚刚创建的用户名和密码）登录后台，但是网页语言还是英文，需要对settings.py进行设置如下：
```python
# LANGUAGE_CODE = "en-us"
LANGUAGE_CODE = "zh-hans"

# TIME_ZONE = "UTC"
TIME_ZONE = "Asia/Shanghai"

USE_I18N = True

# 用于控制是否启用本地化（Localization）功能
USE_L10N = True

# USE_TZ = True
# 用于控制是否启用时区支
USE_TZ = False

```

## apps/goods/apps.py如下：
```python
from django.apps import AppConfig


class GoodsConfig(AppConfig):
    name = 'goods'
    verbose_name = '商品'


```

## apps/trade/apps.py如下：
```python
from django.apps import AppConfig


class TradeConfig(AppConfig):
    name = 'trade'
    verbose_name = '交易管理'


```

## apps/user_operation/apps.py如下：
```python
from django.apps import AppConfig


class UserOperationConfig(AppConfig):
    name = 'user_operation'
    verbose_name = '用户操作管理'


```

## apps/user/apps.py如下：
```python
from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'apps.users'
    verbose_name = '用户管理'


```

## 此时再查看网页如下：
![](https://img-blog.csdnimg.cn/20200721184843685.gif)

显然，此时已经变为中文，并且点击每个导航栏都能看到具体内容，并且可以进行导出数据等多种操作。