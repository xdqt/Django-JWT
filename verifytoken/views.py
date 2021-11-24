from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from .models import *
from django.http.response import JsonResponse
from .serialize import *
from rest_framework_jwt.serializers import VerifyJSONWebTokenSerializer
@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
@authentication_classes((JSONWebTokenAuthentication,))
def posts(request):
    token = request.META.get('HTTP_AUTHORIZATION', " ").split(' ')[1]
    print(token)
    data = {'token': token}
    valid_data = VerifyJSONWebTokenSerializer().validate(data)
    user = valid_data['user']# 打印出来用户信息
    print(user)
    datas = TestTable.objects.all()
    return JsonResponse(TestTableSerializers(datas,many=True).data,safe=False)
