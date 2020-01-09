from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, DetailView

from gift_exchange.forms import GiftExchangeForm, GiftForm
from gift_exchange.models import GiftExchange, Gift, Participant


class Link(DetailView):
    model = GiftExchange
    template_name = "link.html"

    def get_context_data(self, **kwargs):
        context = super(Link, self).get_context_data()
        context['Gift'] = Gift.objects.all()
        context['Gift_exchange_participants'] = Gift.objects.filter(gift_exchange__slug=self.request.path.split('/')[1])
        context['User'] = User.objects.all()
        context['Participant'] = Participant.objects.all()
        return context

    # this gef is baddest practice ever. I know it, sorry :(
    def post(self, model, *args, **kwargs):
        object_list_of_participants = Participant.objects.filter(
            participant_of=self.model.objects.get(
                slug__exact=self.request.path.split('/')[1]
            )
        )
        object_list_of_gifts = Gift.objects.filter(
            gift_exchange=self.model.objects.get(
                slug__exact=self.request.path.split('/')[1]
            )
        )
        participant_user_id_list = []

        for participant in object_list_of_participants:
            participant_user_id_list.append(participant.user.id)

        for gift in object_list_of_gifts:
            copy_participant_user_id_list = participant_user_id_list.copy()

            if gift.user.id in copy_participant_user_id_list:
                copy_participant_user_id_list.remove(gift.user.id)

            last_of = copy_participant_user_id_list[-1]
            gift.to_whom = User.objects.get(id=last_of)
            gift.save()

            if last_of in participant_user_id_list:
                participant_user_id_list.remove(last_of)

        current_gift_exchange = self.model.objects.get(slug__exact=self.request.path.split('/')[1])
        current_gift_exchange.the_draw_was = True
        current_gift_exchange.save()
        massage = 'Зайдите к нам на сайт' \
                  '(https://vast-headland-94854.herokuapp.com/hats-i-member-in/)' \
                  'и посмотрите свою пару по событию "{}".'.format(current_gift_exchange)

        for user in object_list_of_participants:
            from SecretSanta.settings import EMAIL_HOST_USER
            send_mail('Secret Santa',
                      massage,
                      EMAIL_HOST_USER,
                      [user.user.email],
                      fail_silently=False,
                      )

        return redirect('gift_exchange:gift_exchange_link', self.request.path.split('/')[1])


class GiftExchangeCreate(CreateView):
    model = GiftExchange
    form_class = GiftExchangeForm
    template_name = 'create_hat.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(GiftExchangeCreate, self).form_valid(form)


class GiftProfileCreate(CreateView):
    model = Gift
    form_class = GiftForm
    template_name = 'create_profile.html'

    def get_context_data(self, **kwargs):
        context = super(GiftProfileCreate, self).get_context_data()
        context['GiftExchange'] = GiftExchange.objects.get(slug__exact=self.request.path.split('/')[-2])
        return context

    def form_valid(self, form):
        try:
            if Gift.objects.get(gift_exchange=GiftExchange.objects.get(slug__exact=self.request.path.split('/')[-2]),
                                user=self.request.user):
                return redirect('gift_exchange:hats_i_member_in')
        except ObjectDoesNotExist:
            form.instance.user = self.request.user
            form.instance.gift_exchange = GiftExchange.objects.get(slug__exact=self.request.path.split('/')[-2])
            p = Participant(user=self.request.user,
                            participant_of=GiftExchange.objects.get(slug__exact=self.request.path.split('/')[-2])
                            )
            p.save()
            return super(GiftProfileCreate, self).form_valid(form)


class GiftExchangeList(ListView):
    model = GiftExchange
    paginate_by = 10
    template_name = 'hat_list.html'

    def get_queryset(self):
        return GiftExchange.objects.filter(the_draw_was=False).order_by('-creation_date')


class MyGiftExchangeList(ListView):
    model = GiftExchange
    context_object_name = "my_gift_exchange_list"
    paginate_by = 10
    template_name = 'hats_i_member_in_list.html'

    def get_queryset(self):
        _user = self.request.user
        return GiftExchange.objects.filter(gift__user=_user).order_by('-creation_date')


def index(request):
    context = {}
    if request.user.is_authenticated:
        context['username'] = request.user.username
    return render(request, 'index.html', context)
