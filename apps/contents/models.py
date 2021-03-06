from django.db import models

from . import managers
from ..accounts.models import User
from ..core.models import TimeStampedModel


class Advertisement(TimeStampedModel):

    title = models.CharField(
        max_length=100
    )

    body = models.TextField(
        null=True,
        blank=True
    )

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='as_advertisement_author'
    )

    is_published = models.BooleanField(
        default=False
    )

    published_date = models.DateField(
        null=True,
        blank=True
    )

    is_deleted = models.BooleanField(
        default=False
    )

    audiences = models.ManyToManyField(
        User,
        through='AdvertisementAudiences'
    )

    objects = models.Manager()
    availables = managers.AvailableAdvertisementManager()
    deleteds = managers.DeletedAdvertisementManager()
    publisheds = managers.PublishedAdvertisementManager()
    pendings = managers.PendingAdvertisementManager()

    def __str__(self):
        return f'{self.id} - {self.title}'


class AdvertisementAudiences(models.Model):

    advertisement = models.ForeignKey(
        Advertisement,
        on_delete=models.CASCADE
    )

    audience = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    date_joined = models.DateTimeField(
        auto_now_add=True
    )

    is_read = models.BooleanField(
        default=False
    )

    recent_read_on = models.DateTimeField(
        null=True,
        blank=True
    )

    def __str__(self):
        return f'{self.advertisement} - ({self.audience})'


class Notification(TimeStampedModel):

    title = models.CharField(
        max_length=100
    )

    body = models.TextField()

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='as_notifications_author'
    )

    is_sent = models.BooleanField(
        default=False
    )

    sent_on = models.DateTimeField(
        null=True,
        blank=True
    )

    is_deleted = models.BooleanField(
        default=False
    )

    audiences = models.ManyToManyField(
        User,
        through='NotificationAudiences'
    )

    objects = models.Manager()
    sents = managers.SentNotificationManager()
    pendings = managers.PendingNotificationManager()
    availables = managers.AvailableNotificationManager()
    deleteds = managers.DeletedNotificationManager()

    def __str__(self):
        return f'{self.id} - {self.title}'


class NotificationAudiences(models.Model):

    notification = models.ForeignKey(
        Notification,
        on_delete=models.CASCADE
    )

    audience = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    date_joined = models.DateTimeField(
        auto_now_add=True
    )

    is_read = models.BooleanField(
        default=False
    )

    recent_read_on = models.DateTimeField(
        null=True,
        blank=True
    )

    is_deleted = models.BooleanField(
        default=False
    )

    def __str__(self):
        return f'{self.notification} - ({self.audience.name})'
