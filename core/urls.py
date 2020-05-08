from django.urls import path
from .views import (
    ItemDetailView,
    CategoryView,
    CheckoutView,
    HomeView,
    OrderSummaryView,
    add_to_cart,
    remove_from_cart,
    remove_single_item_from_cart,
    PaymentView,
    PaymentViewC,
    AddCouponView,
    RequestRefundView
)
from . import views


app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('add-coupon/', AddCouponView.as_view(), name='add-coupon'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('remove-item-from-cart/<slug>/', remove_single_item_from_cart,
         name='remove-single-item-from-cart'),
    path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
    path('paymentc/<payment_option>/', PaymentViewC.as_view(), name='paymentc'),
    path('request-refund/', RequestRefundView.as_view(), name='request-refund'),
    path('category/<slug>/', CategoryView.as_view(), name='category'),
    path('mpesa/accesstoken', views.getAccessToken, name='get_mpesa_access_token'),
    path('mpesaonline/<payment_option>/', views.lipa_na_mpesa_online, name='lipa_na_mpesa'), #lipa_na_mpesa_online

    # These urls are for registering, confirmation, validation and callback
    path('c2b/register', views.register_urls, name="register_mpesa_validation"),
    path('c2b/confirmation', views.confirmation, name="confirmation"),
    path('c2b/validation', views.validation, name="validation"),
    path('c2b/callback', views.call_back, name="call_back"),
]
