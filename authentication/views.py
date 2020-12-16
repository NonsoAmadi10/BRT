from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from .serializers import (RegistrationSerializer,
                          LoginSerializer, UserListQuerySerializer)
from .messages.success import USER_CREATED, LOGIN_SUCCESS
from .models import User
from BRT.response import success_response


class RegistrationAPIView(APIView):
    """Handles users registration"""

    # Allow any user (authenticated or not) to hit this endpoint.
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer

    @swagger_auto_schema(
        operation_description="apiview post description override",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['email', 'password',
                      'first_name', 'last_name', 'is_admin'],
            properties={
                "status": openapi.Schema(type=openapi.TYPE_STRING),
                'email': openapi.Schema(type=openapi.TYPE_STRING),
                'password': openapi.Schema(type=openapi.TYPE_STRING),
                'first_name': openapi.Schema(type=openapi.TYPE_STRING),
                'last_name': openapi.Schema(type=openapi.TYPE_STRING),
                'is_admin': openapi.Schema(type=openapi.TYPE_BOOLEAN)
            },
        ),
        security=[],
        tags=['Users'],
    )
    def post(self, request):
        """Creates a user
            Args:
                request (request object): Django request object
            Returns:
                JSON: Newly crearted user
        """
        user = request.data

        email = request.data.get('email')

        user_exist = User.objects.filter(email=email)
        if (user_exist):
            response = {"error": "Email is already in use"}
            return Response(response, status=status.HTTP_409_CONFLICT)

        else:

            serializer = self.serializer_class(data=user)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            return success_response(serializer.data, USER_CREATED, status.HTTP_201_CREATED)


class LoginAPIView(APIView):
    """ Handles Users Login Details """
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['email', 'password'],
            properties={
                'email': openapi.Schema(type=openapi.TYPE_STRING),
                'password': openapi.Schema(type=openapi.TYPE_STRING),

            },
        ),
        responses={200: LoginSerializer(many=False)},
        tags=['Users'],
    )
    def post(self, request):
        """ Logs a User \n
            args: 
                request(request object): Django request object

            returns:
                JSON user data and token 
        """

        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)

        return success_response(serializer.data, LOGIN_SUCCESS, status.HTTP_200_OK)
