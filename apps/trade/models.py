from datetime import datetime

from django.db import models

# from user.models import UserProfile
# get_user_model是Django中的一个函数，用于获取当前使用的用户模型。通常情况下，Django的用户模型是django.contrib.auth.models.User，但是可以通过自定义用户模型替换它。
from django.contrib.auth.models import (
    get_user_model,
)

from goods.models import Goods

User = get_user_model()

# Create your models here.


class ShoppingCart(models.Model):
    """购物车"""

    user = models.ForeignKey(
        User, verbose_name="用户", null=True, on_delete=models.SET_NULL
    )
    goods = models.ForeignKey(
        Goods, verbose_name="商品", null=True, on_delete=models.SET_NULL
    )
    goods_num = models.IntegerField(default=0, verbose_name="商品数量")

    add_time = models.DateField(default=datetime.now, verbose_name="添加时间")
    is_delete = models.BooleanField(default=False, verbose_name="是否删除")

    class Meta:
        verbose_name = "购物车"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.goods.name}({self.goods_num})"


class OrderInfo(models.Model):
    """订单信息"""

    ORDER_STATUS = (
        ("success", "成功"),
        ("cancel", "取消"),
        ("paying", "待支付"),
    )

    user = models.ForeignKey(
        User, verbose_name="用户", null=True, on_delete=models.SET_NULL
    )
    order_sn = models.CharField(max_length=30, unique=True, verbose_name="订单号")
    trade_no = models.CharField(
        max_length=50, unique=True, null=True, blank=True, verbose_name="交易号"
    )
    pay_status = models.CharField(
        max_length=100, choices=ORDER_STATUS, verbose_name="订单状态"
    )
    pay_script = models.CharField(max_length=11, verbose_name="订单留言")
    order_mount = models.FloatField(default=0.0, verbose_name="订单金额")
    pay_time = models.DateTimeField(null=True, blank=True, verbose_name="支付时间")

    # 用户基本信息
    address = models.CharField(max_length=100, default="", verbose_name="收货地址")
    signer_name = models.CharField(max_length=20, default="", verbose_name="签收人")
    signer_mobile = models.CharField(max_length=11, verbose_name="联系电话")

    add_time = models.DateField(default=datetime.now, verbose_name="添加时间")
    is_delete = models.BooleanField(default=False, verbose_name="是否删除")


class OrderGoods(models.Model):
    """订单商品详情"""

    order = models.ForeignKey(
        OrderInfo, verbose_name="订单信息", null=True, on_delete=models.SET_NULL
    )
    goods = models.ForeignKey(
        Goods, verbose_name="商品", null=True, on_delete=models.SET_NULL
    )
    goods_num = models.IntegerField(default=0, verbose_name="商品数量")

    add_time = models.DateField(default=datetime.now, verbose_name="添加时间")
    is_delete = models.BooleanField(default=False, verbose_name="是否删除")

    class Meta:
        verbose_name = "订单商品"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.order.order_sn
