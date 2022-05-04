from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .serializers import (
     ExternalTransferSerializer, AccTransactionSerializer,
    AccountSerializer, InternalTransferSerializer
)
from .models import (
    CustomUser, ExternalTransfer, InternalTransfer,
    Account, AccTransaction
)
from .authentications import TokenAuthentication
from rest_framework import generics, permissions


class AccountCreateListView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    def get_queryset(self):
        return Account.objects.filter(customer=self.request.user)

    def perform_create(self, serializer):
        serializer.save(customer=self.request.user)


class AccountRetrieveDeleteUpdateView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    lookup_field = "pk"

    def get_object(self):
        try:
            Account.objects.get(customer=self.request.user, pk=self.kwargs['pk'])
        except Account.DoesNotExist as e:
            return Response({'detail': e}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def get_single_account_balance(request, pk):
    try:
        acc = Account.get_user_account_balance(acc_id=pk, user=request.user)
        if acc is not None:
            return Response({"Name": acc.name, "Amount": acc.amount}, status=status.HTTP_200_OK)
    except Account.DoesNotExist as e:
        return Response({"detail": "Account Not Found"}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def get_user_account_total_balance(request):
    bal = Account.get_user_total_balance(request.user)
    return Response(
        {"Total Balance": bal, "Number of Accounts": request.user.get_account_count},
        status=status.HTTP_200_OK
    )


# ======== ACCOUNT TRANSACTIONS
class CreateListTransactionView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    queryset = AccTransaction.objects.all()
    serializer_class = AccTransactionSerializer

    def get_queryset(self):
        return AccTransaction.objects.filter(customer=self.request.user)

    def perform_create(self, serializer):
        serializer.save(customer=self.request.user)


# ============= INTERNAL TRANSFER ROUTES
class InternalTransferCreateListView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    queryset = InternalTransfer.objects.all()
    serializer_class = InternalTransferSerializer

    def get_queryset(self):
        return InternalTransfer.objects.filter(customer=self.request.user)

    def perform_create(self, serializer):
        serializer.save(customer=self.request.user)


class InternalTransferRetrieveDeleteView(generics.RetrieveDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    queryset = InternalTransfer.objects.all()
    serializer_class = InternalTransferSerializer
    lookup_field = "pk"

    def get_object(self):
        return get_object_or_404(InternalTransfer, customer=self.request.user, pk=self.kwargs['pk'])


# ================ EXTERNAL TRANSFER ROUTES
class ExternalTransferCreateListView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    queryset = ExternalTransfer.objects.all()
    serializer_class = ExternalTransferSerializer

    def get_queryset(self):
        return ExternalTransfer.objects.filter(sender=self.request.user)

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)


class ExternalTransferRetrieveDeleteView(generics.RetrieveDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    queryset = ExternalTransfer.objects.all()
    serializer_class = ExternalTransferSerializer
    lookup_field = "pk"

    def get_object(self):
        return get_object_or_404(ExternalTransfer, sender=self.request.user, pk=self.kwargs['pk'])

