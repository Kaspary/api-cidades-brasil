from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'shema': reverse('shema', request=request, format=format),
        'users': reverse('cityApi.users', request=request, format=format),
        # 'state': reverse('state-list', request=request, format=format),
        # 'city': reverse('city-list', request=request, format=format)
    })


