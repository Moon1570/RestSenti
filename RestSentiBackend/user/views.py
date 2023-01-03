from rest_framework import generics, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.response import Response
from knox.models import AuthToken 
from .serializers import UserSerializer, RegisterSerializer, viewSerializer
from django.contrib.auth.models import User

# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })

@api_view(['GET'])
def user_records(request):
    records = User.objects.all()
    serializer = UserSerializer(records, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def records_by_userid(request,pk):
    records = User.objects.filter(id=pk)
    serializer = viewSerializer(records, many=True)
    return Response(serializer.data)