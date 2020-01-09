from django import forms
from gift_exchange.models import GiftExchange, Gift, Participant


class GiftExchangeForm(forms.ModelForm):
    class Meta:
        model = GiftExchange
        fields = ['title', 'slug', 'description', 'price_start', 'price_limit', 'max_adorable_date']


class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = '__all__'


class GiftForm(forms.ModelForm):
    class Meta:
        model = Gift
        fields = ['description']
