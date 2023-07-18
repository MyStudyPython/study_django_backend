# 导入日期
from datetime import datetime

# 导入模型
from django.db import models

# 导入Django框架中的认证模块(auth)中的AbstractUser类
# AbstractUser 用于扩展用户身份验证和授权的功能。
from django.contrib.auth.models import AbstractUser

# Create your models here.


class UserProfile(AbstractUser):
    """用户信息"""

    """
    CharField
    null=True ---> 据库中该字段的值可以为NULL（空值）。如果不设置该选项，默认情况下，字段值不能为NULL。
    blank=True---> 表示表单中该字段可以为空。如果不设置该选项，默认情况下，表单中的该字段是必填的。
    verbose_name="xxx ---> 设置字段在后台管理界面或自动生成的表单中的可读名称
    validators ---> 校验函数
    """

    name = models.CharField(max_length=30, null=True, blank=True, verbose_name="姓名")
    birthday = models.DateTimeField(null=True, blank=True, verbose_name="出生日期")
    gender = models.CharField(
        max_length=6,
        choices=(("male", "男"), ("female", "女")),
        default="famle",
        verbose_name="性别",
    )
    mobile = models.CharField(max_length=11, verbose_name="电话")
    email = models.EmailField(max_length=50, null=True, blank=True, verbose_name="邮箱")

    is_delete = models.BooleanField(default=False, verbose_name="是否删除")

    class Meta:
        verbose_name = "用户"
        # 复数形式
        verbose_name_plural = "用户"

    def __str__(self):
        return self.name


class VerifyCode(models.Model):
    code = models.CharField(max_length=10, verbose_name="验证码")
    mobile = models.CharField(max_length=11, verbose_name="电话")

    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    is_delete = models.BooleanField(default=False, verbose_name="是否删除")

    class Meta:
        verbose_name = "短信验证码"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
