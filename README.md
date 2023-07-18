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