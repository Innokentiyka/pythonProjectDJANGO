
from django.db import models
from django.contrib.auth import get_user_model

class Client(models.Model):
    email = models.EmailField(max_length=254, unique=True)
    full_name = models.CharField(max_length=100)
    comment = models.TextField(blank=True)

    def __str__(self):
        return self.full_name

class Mailing(models.Model):
    PERIODICITY_CHOICES = [
        ('D', 'Daily'),
        ('W', 'Weekly'),
        ('M', 'Monthly'),
    ]
    STATUS_CHOICES = [
        ('C', 'Created'),
        ('R', 'Running'),
        ('F', 'Finished'),
    ]
    start_time = models.DateTimeField()
    periodicity = models.CharField(max_length=1, choices=PERIODICITY_CHOICES)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    clients = models.ManyToManyField(Client, related_name='mailings')

    def __str__(self):
        return f"Mailing {self.id} - {self.get_status_display()}"

class Message(models.Model):
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE, related_name='messages')
    subject = models.CharField(max_length=255)
    body = models.TextField()

    def __str__(self):
        return self.subject

class Log(models.Model):
    message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name='logs')
    attempt_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50)
    server_response = models.TextField(blank=True)

    def __str__(self):
        return f"Log for {self.message.subject} at {self.attempt_time}"



User = get_user_model()

class MailingList(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mailing_lists')

    def __str__(self):
        return self.title

class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscriptions')
    mailing_list = models.ForeignKey(MailingList, on_delete=models.CASCADE, related_name='subscriptions')
    is_subscribed = models.BooleanField(default=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'mailing_list')

    def __str__(self):
        return f"{self.user.email} - {'Subscribed' if self.is_subscribed else 'Unsubscribed'}"

class MyModel(models.Model):
    # Поля модели

    class Meta:
        permissions = [
            ('custom_permission', 'Описание вашего кастомного разрешения'),
        ]


class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name