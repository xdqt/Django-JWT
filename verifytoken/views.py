from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from .models import *
from django.http.response import JsonResponse
from .serialize import *
from rest_framework_jwt.serializers import VerifyJSONWebTokenSerializer
from rest_framework_jwt.settings import api_settings
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.response import Response

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


from django.contrib.auth.models import User
from .serialize import RegisterSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny
from djangojwt import settings
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
    
    
    
# 自定义生成token
from rest_framework_jwt.utils import jwt_payload_handler,jwt


@api_view(['POST'])
@permission_classes([AllowAny, ])
def authenticate_user(request):
    try:
        print(request.method)
        email = request.data['email']
        username = request.data['username']
        user = User.objects.get(email=email, username=username)
        if user:
            try:
                payload = jwt_payload_handler(user)
                print(payload)
                token = jwt.encode(payload, settings.SECRET_KEY)
                user_details = {}
                user_details['name'] = "%s %s" % (user.first_name, user.last_name)
                user_details['token'] = token
                return Response(user_details, status=status.HTTP_200_OK)
            except Exception as e:
                raise e
        else:
            res = {'error': 'can not authenticate with the given credentials or the account has been deactivated'}
            return Response(res, status=status.HTTP_403_FORBIDDEN)
    except Exception as e:
        res = {'error': 'please provide a email and a username'}
        return Response(res)
