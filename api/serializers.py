from rest_framework import serializers
from .models import InternalTransfer, ExternalTransfer, Account, AccTransaction


class InternalTransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = InternalTransfer
        fields = '__all__'


class AccTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccTransaction
        fields = '__all__'


class ExternalTransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExternalTransfer
        fields = '__all__'


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'

