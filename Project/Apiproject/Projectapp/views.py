from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
import hashlib

class AccountRegister(APIView):
    def post(self, request):
        serializer = Accountserializer(data=request.data)
        
        if not serializer.is_valid():
            return Response({'status': 403, 'errors': serializer.errors, 'message': 'Wrong data received'})

        serializer.save()

        account = Account.objects.get(account_id=serializer.data['account_id'])
        refresh = RefreshToken.for_user(account)

        return Response({'status' : 200 , 'payload' : serializer.data , 'refresh': str(refresh),
        'access': str(refresh.access_token), 'message': "Data saved"})

class AccountAPI(APIView):
    authentication_classes = [ JWTAuthentication]
    permission_classes = [ IsAuthenticated]
        
    def get(self, request):
        account_id = self.request.query_params.get('account_id')
        account = Account.objects.get(account_id=account_id)
        
        if not account:
            return Response({'status': 403, 'errors': serializer.errors, 'message': 'Invalid account id'})
        else:
            return Response({'status': 200, 'email': account.email, 'account_id': account.account_id, 'account_name': account.account_name,
            'website': account.website, 'message': 'Data retrieved successfully'})
            
    def delete(self, request):
        account_id = self.request.query_params.get('account_id')
        account = Account.objects.get(account_id=account_id)

        if not account:
            return Response({'status': 403, 'errors': serializer.errors, 'message': 'Invalid account id'})
        else:
            Account.objects.filter(account_id=account_id).delete()
            return Response({'status': 200, "message": "Deleted successfully"})
            
class DestinationAPI(APIView):
    def post(self, request):
        account_id = self.request.data['account_id']
        print(account_id)
        data = Account.objects.get(account_id=account_id)
        if not data:
            return Response({'status': 403, 'message': 'Invalid account id'})
        
        d = Destination(url=request.data['url'], http_method=request.data['http_method'], headers=request.data['headers'], account=data)
        d.save()

        return Response({'status': 200, 'message': "Data saved"})
        
    def get(self, request):
        url = self.request.query_params.get('url')
        data = Destination.objects.get(url=url)
        
        if not data:
            return Response({'status': 403, 'errors': serializer.errors, 'message': 'Invalid account id'})
        else:
            return Response({'status': 200, 'account': data.account.account_id, 'url': data.url, 'header': data.headers, 'message': 'Data retrieved successfully'})
            
    

        
