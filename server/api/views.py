from rest_framework.response import Response    
from rest_framework import status
from Insightio.models import User
from .serializers import UserSerializer
from rest_framework.decorators import api_view
from django.contrib.auth.hashers import check_password
import jwt,datetime

@api_view(['POST'])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')

    user = User.objects.get(email=email) if User.objects.filter(email=email).exists() else None    
    
    if user:
        if check_password(password, user.password):            
            payload = {
                'id': user.id,
                'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=48),
                'iat': datetime.datetime.utcnow()
            }
                                
            token = jwt.encode(payload, key='secret', algorithm="HS256")
            response = Response()
            response.data = {
                'jwt':token,
                'status':'success',
                'id':user.id,
            }
            return response
        else:
            return Response({'status': 'error', 'message': 'Wrong Password'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'status': 'error', 'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)



@api_view(['POST'])
def signup(request):
    email = request.data.get('email')    
    user_email = None
    try:
        user_email = User.objects.get(email=email) 
    except:
        user_email= None
   
    if user_email is None:            
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():    
            serializer.save()
            return Response({'status': 'success', 'message': 'Data added successfully','email':email}, status=status.HTTP_201_CREATED)
        return Response({'status': 'error', 'message': 'Failed to add data'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        if user_email is not None:
            return Response({'status': 'error', 'message': 'Email already exists'}, status=status.HTTP_400_BAD_REQUEST)
      