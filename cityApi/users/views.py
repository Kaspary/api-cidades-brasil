from rest_framework import permissions, viewsets, generics, authentication, mixins, status
from rest_framework.views import APIView
from rest_framework.decorators import action, api_view, authentication_classes, permission_classes
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken

from django.contrib.auth.models import User, Group

from .serializers import UserSerializer,UpdateUserSerializer
from .permissions import UserModelPermission, IsSelfOrAdmin

class User(viewsets.ModelViewSet):
    """
    manager users
    """

    http_method_names = ['get', 'post', 'put', 'delete']
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


    # Change the serializer class by method
    def get_serializer_class(self):
        if self.request.method in ['PUT',]:
                return UpdateUserSerializer
        return self.serializer_class


    # return correct permission to method
    def get_permissions(self):
        if self.action == 'create':
            return [permissions.AllowAny()]
        elif self.action == 'list':
            return [permissions.IsAdminUser()]
        elif self.action in ('retrieve', 'update', 'destroy'):
            return [IsSelfOrAdmin()]

        

class ObtainAuthTokenView(ObtainAuthToken, generics.GenericAPIView):
    """
    Return token from user
    """
    pass

class NewAuthTokenView(ObtainAuthToken, generics.GenericAPIView):
    """
    Return a new token from user
    """

    def post(self, request, *args, **kwargs):

        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            if not created:
                key = token.generate_key()
                Token.objects.filter(user=user).update(key=key)

            return Response({'token': key}, 200)
        except Exception as e:
            print(str(e))
            return Response({'error': str(e)}, 400)





# EXAMPLES

# @api_view(['GET'])
# @permission_classes([permissions.IsAuthenticated])
# def get_token(request):
#     return Response({'key' : Token.objects.get(user=request.user).key})


# class UserViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """

#     queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer

#     @action(methods=['get'], detail=True, permission_classes=[permissions.IsAuthenticated])
#     def token(self, request, pk=None):
#         return Response({'token': Token.objects.get(user=pk).key})


#     @action(methods=['put'], detail=True, permission_classes=[permissions.IsAuthenticated])
#     def token(self, request, pk=None):
#         Token.objects.get(user=pk).update()
#         return Response({'token': Token.objects.get(user=pk).key})
