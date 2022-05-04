from django.urls import path
from . import views

urlpatterns = [
    path("accounts/", views.AccountCreateListView.as_view()),
    path("accounts/<int:pk>/", views.AccountRetrieveDeleteUpdateView.as_view()),
    path("accounts/<int:pk>/balance/", views.get_single_account_balance),
    path("accounts/balance/", views.get_user_account_total_balance),
    path("accounts/transaction/", views.CreateListTransactionView.as_view()),

    # INTERNAL TRANSFER
    path("internal-transfer/", views.InternalTransferCreateListView.as_view()),
    path("internal-transfer/<int:pk>/", views.InternalTransferRetrieveDeleteView.as_view()),

    # EXTERNAL TRANSFER
    path("external-transfer/", views.ExternalTransferCreateListView.as_view()),
    path("external-transfer/<int:pk>/", views.ExternalTransferRetrieveDeleteView.as_view()),
]
