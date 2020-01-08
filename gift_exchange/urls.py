from django.urls import path
from allauth.account.views import login, logout
from gift_exchange.views import *
from django.contrib.auth.decorators import login_required

app_name = 'gift_exchange'
urlpatterns = [
	path('', index, name='index'),
	path('hats-i-member-in/', MyGiftExchangeList.as_view(), name='hats_i_member_in'),
	path('create-hat/', GiftExchangeCreate.as_view(), name='create_hat'),
	path('create-gift-profile/<slug:slug>/', login_required(GiftProfileCreate.as_view()), name='create_gift_profile'),
	path('all-hats/', GiftExchangeList.as_view(), name='all_hats'),
	path('login/', login, name='login'),
	path('logout/', logout, name='logout'),
	path('<slug:slug>/', login_required(Link.as_view()), name='gift_exchange_link'),
]
