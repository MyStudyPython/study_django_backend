# study_django_backend
学习Django后端接口

# Django xadmin数据迁移 记录报错
## 问题一
```sh
ImportError: cannot import name 'python_2_unicode_compatible' from 'django.utils.encoding'
```
### 解决方式：
```diff
- # from django.utils.encoding import python_2_unicode_compatible, smart_text
+ from six import python_2_unicode_compatible
+ from django.utils.encoding import smart_str
```

## 问题二
```sh
ImportError: cannot import name 'pretty_name' from 'django.forms.forms'
```
### 解决方式
直接注释这一句

## 问题三
```sh
ImportError: cannot import name 'force_text' from 'django.utils.encoding'
```
### 解决方式
```diff
- from django.utils.encoding import force_text, smart_text, smart_str
+ from django.utils.encoding import force_str, smart_str
```

## 问题四
```sh
ImportError: cannot import name 'ungettext' from 'django.utils.translation'
```
### 解决方式
```diff
- # from django.utils.translation import ungettext
+ from django.utils.translation import ngettext
```

## 问题五
```sh
ModuleNotFoundError: No module named 'django.contrib.staticfiles.templatetags'
```
### 解决方式
```diff
- # from django.contrib.staticfiles.templatetags.staticfiles import static
+ from django.templatetags.static import static
```

## 问题六
```sh
ImportError: cannot import name 'ugettext' from 'django.utils.translation'

or

ImportError: cannot import name 'ugettext_lazy' from 'django.utils.translation'
```
### 解决方式
分析：
Django已经弃用 ugettext(), ugettext_lazy(), ugettext_noop(), ungettext(), 和 ungettext_lazy()
查看[issues地址](https://www.yii666.com/blog/401684.html)

解决办法：
既然选择了高版本Django，就尝试在此版本下解决问题。

它已从Django 4中删除，请使用此选项
from django.utils.translation import gettext_lazy as _

```diff
- #from django.utils.translation import ugettext as _
+ from django.utils.translation import gettext as _
```

## 问题七
```sh
ImportError: cannot import name 'urlquote' from 'django.utils.http'
```

### 解决方式
dashboard.py文件
```diff
- # from django.utils.http import urlencode, urlquote
+ from django.utils.http import urlencode, quote
```

## 问题八
```sh
ImportError: cannot import name 'ungettext' from 'django.utils.translation'
```

### 解决方式
```diff
- from django.utils.translation import gettext as _, ungettext
+ from django.utils.translation import gettext as _, ngettext
```

## 问题九
```sh
ImportError: cannot import name 'lookup_needs_distinct' from 'django.contrib.admin.utils'
```

### 解决方式
```diff
- from django.contrib.admin.utils import get_fields_from_path, lookup_needs_distinct
+ from django.contrib.admin.utils import get_fields_from_path, lookup_spawns_duplicates
```

## 问题十
```sh
ImportError: cannot import name 'FieldDoesNotExist' from 'django.db.models.fields'
```
### 解决方式
先`pip install django-advanced-filters`
```diff
- # from django.db.models.fields import FieldDoesNotExist
+ from django.core.exceptions import FieldDoesNotExist
```

## 问题十一
```sh
ImportError: cannot import name 'FieldDoesNotExist' from 'django.db.models'
```
### 解决方式
```diff
- from django.db.models import FieldDoesNotExist,Avg, Max, Min, Count, Sum

+ from django.db.models import Avg, Max, Min, Count, Sum
+ from django.core.exceptions import FieldDoesNotExist
```

## 问题十二
```sh
ImportError: cannot import name 'SKIP_ADMIN_LOG' from 'import_export.admin'
```

### 解决方式
```diff
from import_export.admin import DEFAULT_FORMATS, SKIP_ADMIN_LOG, TMP_STORAGE_CLASS
from import_export.admin import DEFAULT_FORMATS, ImportMixin, ImportExportMixinBase
```

# 对xadmin配置访问路径 记录报错
## 问题一
```sh
AttributeError: 'Options' object has no attribute 'installed'
```
### 解决方式
我还研究了很久啥原因，看了看源码，后来直接看这段代码的意思，就是让把django.contrib.contenttypes安装到INSTALLED_APPS中，我检查了一下，安装了呀。
解决办法：直接注释掉，当然这样就没有检查安装django.contrib.contenttypes的过程了。

```python
# if not ContentType._meta.installed:
#     raise ImproperlyConfigured("Put 'django.contrib.contenttypes' in "
#                                "your INSTALLED_APPS setting in order to use the admin application.")
```

看源码，Django 2.0.x的源码中Options是有这个属性方法的，3.2.x也有，4.0.x也有。

> /django/db/models/options.py

```py
@property
def installed(self):
    return self.app_config is not None
```

在Django的release note中没有看到提及，看[GitHub的代码历史，是被移除了，说没用](https://github.com/django/django/commit/8e3b1cf098018b4632de63c359ef6d761e92ec04)。

## 问题二
```sh
TypeError: never_cache didn't receive an HttpRequest. If you are decorating a classmethod, be sure to use @method_decorator.
```
### 解决方式
这个exception好像还没解决，[点击这个链接反馈，加速fix](https://fixexception.com/django/never-cache-didn-t-receive-an-httprequest-if-you-are-decorating-a-classmethod-be-sure-to-use-method-decorator/)

我是注释掉了：

```python
        # if not hasattr(request, "META"):
        #     raise TypeError(
        #         "never_cache didn't receive an HttpRequest. If you are "
        #         "decorating a classmethod, be sure to use @method_decorator."
        #     )
```

## 问题三
```sh
raise TemplateSyntaxError(
django.template.exceptions.TemplateSyntaxError: 'crispy_forms_tags' is not a registered tag library. Must be one of:
admin_list
admin_modify
admin_urls
cache
i18n
l10n
log
static
tz
xadmin_tags
```
### 解决方式
在settings.py 加入`crispy_forms`

```diff
INSTALLED_APPS = [
      "django.contrib.admin",
      "django.contrib.auth",
      "django.contrib.contenttypes",
      "django.contrib.sessions",
      "django.contrib.messages",
      "django.contrib.staticfiles",
      "users.apps.UsersConfig",
      # "goods",
      # "trade",
      # "user_operation",
      "goods.apps.GoodsConfig",
      "trade.apps.TradeConfig",
      "user_operation.apps.UserOperationConfig",
      "DjangoUeditor",
      "xadmin",
+     "crispy_forms",
]
```

## 问题四
```sh
django.template.exceptions.TemplateDoesNotExist: bootstrap3/errors.html
```
### 解决方式
这是django高版本与xadmin低版本 不兼容导致的

在xadmin中找到`bootstrap3/errors.html`,可以发现xadmin只有两个页面使用到了`bootstrap3/errors.html`,把他们注释或者删除即可。

![](https://img-blog.csdnimg.cn/669d3f7b9cbb4cc2a34ff41d3ba1be2b.png)

把`login.html`页面的第46行注释掉

![](https://img-blog.csdnimg.cn/669d3f7b9cbb4cc2a34ff41d3ba1be2b.png)

把`form.html`页面的第19行注释掉

![](https://img-blog.csdnimg.cn/8de52effaa564226899a18211da69b3a.png)


# 点击菜单 记录报错
## 问题一 
```sh
AttributeError: 'WSGIRequest' object has no attribute 'is_ajax'
```
### 解决方式
这个[Django 3.1的release note](https://docs.djangoproject.com/en/3.1/releases/3.1/#id2)有提到

>The HttpRequest.is_ajax() method is deprecated as it relied on a jQuery-specific way of signifying AJAX calls, while current usage tends to use the JavaScript Fetch API. Depending on your use case, you can either write your own AJAX detection method, or use the new HttpRequest.accepts() method if your code depends on the client Accept HTTP header.
If you are writing your own AJAX detection method, request.is_ajax() can be reproduced exactly as request.headers.get(‘x-requested-with’) == ‘XMLHttpRequest’.

可以像这样用，创建一个自定义函数，进行检查：
```python
def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

```

网上的例子：
```python
from django.shortcuts import HttpResponse


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


def ajax_test(request):
    if is_ajax(request=request):
        message = "This is ajax"
    else:
        message = "Not ajax"
    return HttpResponse(message)

```

解决方法：
```python
        # return bool(self.request.is_ajax() or self.request.GET.get('_ajax'))
        return bool(self.request.headers.get('x-requested-with') == 'XMLHttpRequest' or self.request.GET.get('_ajax'))
```

## 问题二
```sh
AttributeError: module 'django.db.models' has no attribute 'FieldDoesNotExist'
```

### 解决方式
```python
最上面导包的代码
from django.core.exceptions import PermissionDenied, ObjectDoesNotExist
改成
from django.core.exceptions import PermissionDenied, ObjectDoesNotExist, FieldDoesNotExist

```

```python
报错的那个位置改成
# except models.FieldDoesNotExist:
 except FieldDoesNotExist:

```

## 问题三
```sh
django.template.exceptions.TemplateSyntaxError: Invalid block tag on line 2: 'ifequal'. Did you forget to register or load this tag?
```
### 解决方式
找到报错的模板文件，我报错的是项目根路径/venv/Lib/site-packages/xadmin/templates/xadmin/includes/pagination.html
```python
把ifequal cl.result_count 1 改成 if cl.result_count == 1
把endifequal 改成 endif
```


# `datetime` 用 `json.dumps()`方法序列化 记录报错
## 问题一
```sh
raise TypeError(f'Object of type {o.__class__.__name__} '
TypeError: Object of type date is not JSON serializable
```
### 解决方式
使用Django自带的`model_to_dict()`方法可以实现直接将模型数据转化为字典形式，但是对于DateTimeField、ImageField等字段时还是无法序列化，因此需要使用**serializer**进行序列化，views_base.py如下：

```python
import json

from django.views.generic.base import View
from django.http import HttpResponse, JsonResponse
from django.forms.models import model_to_dict
from django.core import serializers

from goods.models import Goods


class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, bytes):
            return str(obj, encoding='utf-8')

        return json.JSONEncoder.default(self, obj)


class GoodsListView(View):
    def get(self, request):
        '''通过serializers实现商品列表页'''
        goods = Goods.objects.all()[:10]
        json_data = serializers.serialize('json', goods)
        return HttpResponse(json_data, content_type='application/json')

```

# Django配置Restful framework 记录报错
## 问题一
```sh
TypeError: __str__ returned non-string (type NoneType)
```
在Django项目中配置Restful framework时，报错`__str__ returned non-string (type NoneType)`，如下
![](https://img-blog.csdnimg.cn/20200724150854328.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0NVRkVFQ1I=,size_16,color_FFFFFF,t_70)

这可能是自定义用户模型代替Django自带的用户模型时，允许name（或相似的）字段允许为空，例如name = models.CharField(max_length=30, null=True, blank=True, verbose_name='姓名')所以会返回non-string报错，完整模型如下：
```python
class UserProfile(AbstractUser):
    '''用户'''
    name = models.CharField(max_length=30, null=True, blank=True, verbose_name='姓名')
    birthday = models.DateField(null=True, blank=True, verbose_name='出生日期')
    gender = models.CharField(max_length=6, choices=(('male', u'男'), ('female', u'女')), default='female',
                              verbose_name='性别')
    mobile = models.CharField(max_length=11, verbose_name='电话')
    email = models.CharField(max_length=50, null=True, blank=True, verbose_name='邮箱')

    is_delete = models.BooleanField(default=False, verbose_name='是否删除')

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = '用户'

    def __str__(self):
        return self.name

```

### 解决方式
解决办法有2种：

1. 退出admin或xadmin后台登录
   
   退出后台管理登录，操作如下:

   ![](https://img-blog.csdnimg.cn/20200724151546458.gif)

2. 修改用户模型`__str__()`方法
   因为自定义用户如UserProfile继承自AbstractUser，而AbstractUser模型有username属性，不允许为空，所以可以设置为返回self.username，即如下：

   ```python
   def __str__(self):
    return self.username
   ```
   此时不登出后台管理也可以正常访问。
