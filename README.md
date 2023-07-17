# study_django_backend
学习Django后端接口

# 记录报错
## 问题一
```sh
SystemCheckError: System check identified some issues:

ERRORS:
goods.Banner.image: (fields.E210) Cannot use ImageField because Pillow is not installed.
        HINT: Get Pillow at https://pypi.org/project/Pillow/ or run command "python -m pip install Pillow".
goods.Goods.goods_front_image: (fields.E210) Cannot use ImageField because Pillow is not installed.
        HINT: Get Pillow at https://pypi.org/project/Pillow/ or run command "python -m pip install Pillow".
goods.GoodsCategoryBrand.img: (fields.E210) Cannot use ImageField because Pillow is not installed.
goods.GoodsImage.image: (fields.E210) Cannot use ImageField because Pillow is not installed.
        HINT: Get Pillow at https://pypi.org/project/Pillow/ or run command "python -m pip install Pillow".
```
### 解决方式：
直接安装`python -m pip install Pillow`
