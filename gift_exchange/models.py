import os
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
import random


class Participant(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='participant',
                             blank=True,
                             null=True,
                             )
    participant_of = models.ForeignKey('GiftExchange',
                                       on_delete=models.CASCADE,
                                       blank=True,
                                       null=True,
                                       )

    def __str__(self):
        return self.user.username


class GiftExchange(models.Model):
    title = models.CharField('Название вашего обмена',
                             max_length=50
                             )
    slug = models.SlugField('Url адрес обмена',
                            max_length=100,
                            unique=True
                            )
    description: str = models.TextField('Описание')
    price_start = models.PositiveSmallIntegerField('Минимальная стоимость подарка',
                                                   blank=True,
                                                   null=True,
                                                   default=0
                                                   )
    price_limit = models.PositiveSmallIntegerField('Максимальная  стоимость подарка',
                                                   blank=True,
                                                   null=True,
                                                   default=10
                                                   )
    max_adorable_date = models.DateTimeField('Дата до которой можно подключится')
    image = models.ImageField('Картинка для вида',
                              upload_to='media/img/%Y/%m/%d',
                              null=True,
                              blank=True,
                              # i know its handbrake, but it's made only for heroku
                              default="media/img/0000/00/00/gifts-{}.jpg".format(random.randint(0, 9))
                              )
    created_by = models.ForeignKey(User,
                                   null=True,
                                   blank=True,
                                   on_delete=models.SET_NULL
                                   )
    the_draw_was = models.BooleanField('Была ли жеребьевка',
                                       default=False
                                       )
    creation_date = models.DateTimeField('Дата создания',
                                         auto_now=False,
                                         auto_now_add=True,
                                         null=True,
                                         blank=True,
                                         )

    class Meta:
        verbose_name = 'Обмен подарками'
        verbose_name_plural = 'Обмены подарками'

    def __str__(self):
        return self.title

    def get_absolute_image_url(self):
        return os.path.join(settings.MEDIA_URL, self.image.url)

    def get_absolute_url(self):
        return reverse('gift_exchange:create_gift_profile', kwargs={'slug': self.slug})


class Gift(models.Model):
    description = models.TextField('Напишите что бы вы хотели, а также укажите адрес куда ваш "Secret Santa" сможет '
                                   'доставить подарок.')
    user: User = models.ForeignKey(User,
                                   related_name="Пользователь",
                                   null=True,
                                   blank=True,
                                   on_delete=models.CASCADE,
                                   )
    gift_exchange = models.ForeignKey(GiftExchange,
                                      on_delete=models.CASCADE,
                                      null=True,
                                      blank=True,
                                      )
    to_whom: User = models.ForeignKey(User,
                                      related_name='Кому дарит+',
                                      default=None,
                                      null=True,
                                      blank=True,
                                      on_delete=models.SET_NULL,
                                      )

    class Meta:
        verbose_name = 'Подарок'
        verbose_name_plural = 'Подарки'

    def __str__(self):
        return self.description

    def get_absolute_url(self):
        return reverse('gift_exchange:gift_exchange_link', kwargs={'slug': self.gift_exchange.slug})
