import sys, os

pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(pwd, ".."))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "FreshECommerce.settings")

import django

django.setup()

from goods.models import Goods, GoodsCategory, GoodsImage

from db_tools.data.product_data import raw_data

for goods_detail in raw_data:
    goods = Goods()

    goods.name = goods_detail["name"]
    goods.market_price = float(
        goods_detail["market_price"].replace("￥", "").replace("元", "")
    )
    goods.shop_price = float(
        goods_detail["sale_price"].replace("￥", "").replace("元", "")
    )

    """
    if goods_detail["desc"] is not None：

    这是一个条件判断，判断商品的描述是否不为 None。
    如果条件为真，则返回 goods_detail["desc"]，即商品的描述。
    
    如果条件为假，则执行 else 后面的逻辑。
    """
    goods.goods_brief = goods_detail["desc"] if goods_detail["desc"] is not None else ""
    goods.goods_desc = goods_detail["desc"] if goods_detail["desc"] is not None else ""
    goods.goods_front_image = (
        goods_detail["images"][0] if goods_detail["images"] is not None else ""
    )

    """
    为什么取左后一个元素：
    目的是获取商品所属的最具体的类别名称。

    这样做的目的是将商品与其所属的最细粒度的类别进行关联，以便准确地表示商品的分类信息。
    """
    category_name = goods_detail["categorys"][-1]
    """
    GoodsCategory.objects.filter(name=category_name)：这是一个 Django ORM 查询语句，
    通过查询 GoodsCategory 模型，找到名称等于 category_name 的类别。
    """
    category = GoodsCategory.objects.filter(name=category_name)
    if category:
        goods.category = category[0]

    goods.save()

    for goods_image in goods_detail["images"]:
        goods_iamge_instance = GoodsImage()

        goods_iamge_instance.image = goods_image
        goods_iamge_instance.goods = goods
        goods_iamge_instance.save()


print("Goods data imported successfully")
