# 用来对接接口返回的数据  进行序列化
from rest_framework import serializers
from .models import Goods
class GoodsSerializers(serializers.ModelSerializer):
    class Meta:
        model =Goods  #序列化的模型  决定返回数据的字段
        fields=["id","goods_number","goods_name","goods_price","goods_count","goods_location","goods_safe_date","goods_pro_time","goods_status"]
    # goods_number = models.CharField(max_length=11, verbose_name="商品编号")
    # goods_name = models.CharField(max_length=32, verbose_name="商品名字")
    # goods_price = models.FloatField(verbose_name="商品价格")
    # goods_count = models.IntegerField(verbose_name="商品数量")
    # goods_location = models.CharField(max_length=32, verbose_name="商品产地")
    # goods_safe_date = models.IntegerField(verbose_name="商品保质期")
    # goods_pro_time = models.DateTimeField(auto_now=True, verbose_name="生成日期")
    # goods_status = models.IntegerField(verbose_name="商品状态", default=1)