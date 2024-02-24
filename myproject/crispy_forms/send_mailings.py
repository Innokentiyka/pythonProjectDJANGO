from django.core.management.base import BaseCommand
from django.utils import timezone
from .models import Mailing
from django.core.mail import send_mass_mail
from django.template.loader import render_to_string
from .models import Subscription, MailingList

class Command(BaseCommand):
       help = 'Send scheduled mailings to clients'

       def handle(self, *args, **options):
           now = timezone.now()
           mailings = Mailing.objects.filter(start_time__lte=now, status='R')  # Предполагаем, что 'R' обозначает "Ready to send"
           for mailing in mailings:
               # Здесь должна быть логика отправки сообщений вашим клиентам
               # Например, использование Django EmailBackend или других сервисов
               print(f"Sending mailing {mailing.id}")
               mailing.status = 'S'  # Предполагаем, что 'S' обозначает "Sent"
               mailing.save()
               self.stdout.write(self.style.SUCCESS(f'Successfully sent mailing {mailing.id}'))


def send_mailings():
    mailings = MailingList.objects.filter(active=True)
    messages = []
    for mailing in mailings:
        subscribers = Subscription.objects.filter(mailing_list=mailing, active=True)
        subject = mailing.subject
        for subscriber in subscribers:
            message = render_to_string('mailing/email_template.html', {'content': mailing.content})
            messages.append((subject, message, 'from@example.com', [subscriber.email]))

    send_mass_mail(messages, fail_silently=False)