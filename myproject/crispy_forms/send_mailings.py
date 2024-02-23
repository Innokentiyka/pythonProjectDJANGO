from django.core.management.base import BaseCommand
from django.utils import timezone
from .models import Mailing
# Импортируйте необходимые инструменты для отправки email

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