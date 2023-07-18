import sys, os

# 获取当前文件的路径。
pwd = os.path.dirname(os.path.realpath(__file__))
# 将上级目录添加到sys.path中，以便可以导入上级目录中的模块
# sys.path.append(pwd + "../")
sys.path.append(os.path.join(pwd, ".."))
# 设置环境变量DJANGO_SETTINGS_MODULE，指定Django项目的设置文件。
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "FreshECommerce.settings")

# print("os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Fresh_Ecommerce.settings')")

import django

# 初始化Django的设置，包括数据库连接等
django.setup()

from goods.models import GoodsCategory  # 不能位于前面的代码之前，否则会出错

from db_tools.data.category_data import raw_data

for lev1_cat in raw_data:
    lev1_instance = GoodsCategory()

    lev1_instance.code = lev1_cat["code"]
    lev1_instance.name = lev1_cat["name"]
    lev1_instance.category_type = 1
    lev1_instance.save()

    for lev2_cat in lev1_cat["sub_categorys"]:
        lev2_instance = GoodsCategory()

        lev2_instance.code = lev2_cat["code"]
        lev2_instance.name = lev2_cat["name"]
        lev2_instance.category_type = 2
        lev2_instance.parent_category = lev1_instance
        lev2_instance.save()

        for lev3_cat in lev2_cat["sub_categorys"]:
            lev3_instance = GoodsCategory()

            lev3_instance.code = lev3_cat["code"]
            lev3_instance.name = lev3_cat["name"]
            lev3_instance.category_type = 3
            lev3_instance.parent_category = lev2_instance
            lev3_instance.save()

print("Category data imported successfully")
