# from django .views import View
# from django .http import JsonResponse
# from .models import *
# http_method_names=['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace']
# class GoodsView(View):
#     def __init__(self):
#         super(GoodsView,self).__init__()
#         self.result={
#             "version":"",
#             "methon":"",
#             "data":"",
#             "mst":"",
#             "code":"",
#         }
#         self.obj=Goods
#
#     def get(self, request):
#         # result = {"methods": "get请求"}
#         id = request.GET.get("id")
#         if id:
#             # goods=Goods.objects.filter(id=id).first()
#             goods = self.obj.objects.filter(id=id).first()
#             data = {
#                 "goods_number": goods.goods_number,
#                 "goods_name": goods.goods_name,
#                 "goods_price": goods.goods_price,
#                 "goods_count": goods.goods_count,
#                 "goods_location": goods.goods_location,
#                 "goods_safe_date": goods.goods_safe_date,
#                 "goods_status": goods.goods_status,
#
#             }
#             # result["data"]=data
#         else:
#             # goods=Goods.objects.all()
#             goods = self.obj.objects.all()
#             data = []
#             for one in goods:
#                 res = {
#                     "goods_number": one.goods_number,
#                     "goods_name": one.goods_name,
#                     "goods_price": one.goods_price,
#                     "goods_count": one.goods_count,
#                     "goods_location": one.goods_location,
#                     "goods_safe_date": one.goods_safe_date,
#                     "goods_status": one.goods_status,
#
#                 }
#                 data.append(res)
#                 # result["data"]=data
#         self.result["methods"] = "get请求"
#         self.result["data"] = data
#         self.result["code"] = 10000
#         self.result["msg"] = "请求成功"
#
#         return JsonResponse(self.result)
#
#
#     def post(self,request):
#         result={"methods":"post请求"}
#         return JsonResponse(result)
#
#
#     def put(self,request):
#         result={"methods":"put请求"}
#         return JsonResponse(result)
#
#
#     def delete(self,request):
#         result={"methods":"delete请求"}
#         return JsonResponse(result)




