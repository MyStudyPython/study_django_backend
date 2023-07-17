# 导入时间
from datetime import datetime

# 导入模块
from django.db import models

# 导入富文本编辑器字段
from DjangoUeditor.models import UEditorField

# Create your models here.


class GoodsCategory(models.Model):
    """商品分类"""

    CATEGORY_TYPE = (
        (1, "一级类目"),
        (2, "二级类目"),
        (3, "三级类目"),
    )

    name = models.CharField(
        default="", max_length=30, verbose_name="类别名", help_text="类别名"
    )
    code = models.CharField(
        max_length="", verbose_name=30, verbose_name="类别code", help_text="类别code"
    )
    desc = models.TextField(default="", verbose_name="类别描述", help_text="类别描述")
    category_type = models.IntegerField(
        choices=CATEGORY_TYPE, verbose_name="类目级别", help_text="类目级别"
    )

    """
    关联主键，一对多的关系

    self ---> 指明了关联的是同一模型的对象,指向自己。
    related_name --->  关联的GoodsCategory模型中，可以使用该名称来获取与之相关的子级别
    on_delete ---> 当关联的GoodsCategory对象被删除时的操作，在这种情况下，如果该GoodsCategory对象被删除。
    """
    parent_category = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        verbose_name="父级别",
        related_name="sub_cat",
        on_delete=models.SET_NULL,
    )
    is_tab = models.BooleanField(default=False, verbose_name="是否导航", help_text="是否导航")
    is_delete = models.BooleanField(default=False, verbose_name="是否删除")

    class Meta:
        verbose_name = "商品类别"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
