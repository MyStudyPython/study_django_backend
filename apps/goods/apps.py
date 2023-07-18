from django.apps import AppConfig


class GoodsConfig(AppConfig):
    # 用于指定模型的默认自增字段类型,BigAutoField，适用于更大的整数范围
    # default_auto_field = 'django.db.models.BigAutoField'
    name = "goods"
    verbose_name = "商品"
