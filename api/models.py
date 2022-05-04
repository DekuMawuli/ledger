from django.db import models
from users.models import CustomUser


class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Account(TimeStamp):
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, related_name="accounts")
    name = models.CharField(max_length=200)
    account_number = models.CharField(max_length=20, unique=True)
    amount = models.DecimalField(max_digits=30, decimal_places=2, default=0.00)

    @classmethod
    def get_user_account_balance(cls, user, acc_id):
        return cls.objects.get(customer=user, pk=acc_id)

    @classmethod
    def get_user_total_balance(cls, user):
        accounts = cls.objects.filter(customer=user)
        return sum([acc.amount for acc in accounts])

    @classmethod
    def get_customer_accounts(cls, user):
        return cls.objects.filter(customer=user)

    def __str__(self):
        return f"{self.customer.get_full_name()} - {self.name}"


class InternalTransfer(TimeStamp):
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True)
    sender_account = models.ForeignKey(Account, on_delete=models.DO_NOTHING, related_name="sender_account")
    receiving_account = models.ForeignKey(Account, on_delete=models.DO_NOTHING, related_name="receiving_account")
    amount = models.DecimalField(max_digits=30, decimal_places=2)

    def __str__(self):
        return f"Internal Transfer: {self.customer.get_full_name()}"

    @classmethod
    def get_user_internal_transfers(cls, user):
        return cls.objects.filter(customer=user)


class ExternalTransfer(TimeStamp):
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, related_name="sender")
    receiver = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, related_name="receiver")
    sender_account = models.ForeignKey(Account, on_delete=models.DO_NOTHING, related_name="external_sender_account")
    receiver_account = models.ForeignKey(Account, on_delete=models.DO_NOTHING, related_name="external_receiving_account")
    amount = models.DecimalField(max_digits=30, decimal_places=2)

    @classmethod
    def get_user_external_transfers(cls, user):
        return cls.objects.filter(customer=user)

    def __str__(self):
        return f"External Transfer:"


class AccTransaction(TimeStamp):
    TRANS_TYPE = [
        ("W", "Withdrawal"),
        ("D", "Deposit")
    ]

    trans_type = models.CharField(max_length=1, choices=TRANS_TYPE)
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True)
    account_num = models.CharField(max_length=20, blank=True, null=True)
    amount = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return f"Transaction: {self.customer.get_full_name()} - Type: {self.get_trans_type_display()}"
