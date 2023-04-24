from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Account
from .serializers import AccountSerializer

class RegisterView(generics.CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        account = serializer.save()
        refresh = RefreshToken.for_user(account)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })

class LoginView(generics.CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')
        account = Account.objects.filter(email=email).first()
        if account is None or not account.check_password(password):
            return Response({'error': 'Invalid Credentials'}, status=401)
        refresh = RefreshToken.for_user(account)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })

class AccountView(generics.RetrieveAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'
