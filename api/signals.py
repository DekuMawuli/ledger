from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404

from .models import (
    AccTransaction, Account,
    InternalTransfer, ExternalTransfer
)


@receiver(pre_save, sender=AccTransaction)
def amount_suitable(sender, instance, **kwargs):
    amount = instance.amount
    acc_num = instance.account_num
    trans_type = instance.trans_type
    try:
        account = Account.objects.get(account_number=acc_num)
    except Account.DoesNotExist:
        raise ValidationError({'error': "Account Does not Exist"})

    if trans_type not in ["D", "W"]:
        raise ValidationError({'error': "Transaction verb incorrect"})
    elif trans_type == "W" and amount > account.amount:
        raise ValidationError({'error': "You cannot withdraw more than what you have in your account"})
    elif amount <= 0:
        raise ValidationError({'error': "You cannot Deposit or Withdraw 0.00. Invalid Amount"})


@receiver(post_save, sender=AccTransaction)
def transaction_added(sender, created, instance, **kwargs):
    if created:
        amount = instance.amount
        acc_num = instance.account_num
        trans_type = instance.trans_type
        try:
            account = Account.objects.get(account_number=acc_num)
        except Account.DoesNotExist:
            raise ValidationError({'error': "Account Does not Exist"})

        if trans_type == "W":
            account.amount -= amount
            account.save()
        else:
            account.amount += amount
            account.save()


@receiver(pre_save, sender=InternalTransfer)
def internal_trans_amount(sender, instance, **kwargs):
    amount = instance.amount
    sender_acc = instance.sender_account
    receiver_acc = instance.receiving_account
    customer = instance.customer

    if customer.pk != sender_acc.customer.pk or customer.pk != receiver_acc.customer.pk:
        raise ValidationError({'error': "Account Does not Belong to you. Please Verify"})
    if amount > sender_acc.amount:
        raise ValidationError({'error': "Amount to be sent is more than current balance"})


@receiver(post_save, sender=InternalTransfer)
def trans_successful(sender, created, instance, **kwargs):
    if created:
        amount = instance.amount
        sender_acc = instance.sender_account
        receiver_acc = instance.receiving_account
        sender_acc.amount -= amount
        receiver_acc.amount += amount
        sender_acc.save()
        receiver_acc.save()


@receiver(pre_save, sender=ExternalTransfer)
def external_trans_amount(signal, instance, **kwargs):
    amount = instance.amount
    sender_acc = instance.sender_account
    receiver_acc = instance.receiver_account
    sender = instance.sender
    receiver_user = instance.receiver
    print(f"Sender: {sender.pk}")
    print(f"Receiver: {receiver_user.pk}")

    if sender.pk == receiver_user.pk:
        raise ValidationError({'error': "Sender account is the same as recipient Account!"})
    elif sender.pk != sender_acc.customer.pk:
        raise ValidationError({'error': "Account Does not Belong to Sender. Please Verify"})
    elif receiver_user.pk != receiver_acc.customer.pk:
        raise ValidationError({'error': "Account Does not Belong to Receiver. Please Verify"})
    if amount > sender_acc.amount:
        raise ValidationError({'error': "Amount to be sent is more than current balance"})


@receiver(post_save, sender=ExternalTransfer)
def ex_trans_successful(signal, created, instance, **kwargs):
    if created:
        amount = instance.amount
        sender_acc = instance.sender_account
        receiver_acc = instance.receiver_account
        sender_acc.amount -= amount
        receiver_acc.amount += amount
        sender_acc.save()
        receiver_acc.save()
