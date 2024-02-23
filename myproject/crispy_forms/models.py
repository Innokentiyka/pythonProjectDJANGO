from django.db import models

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