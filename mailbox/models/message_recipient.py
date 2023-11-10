
from django.db import models
from mailbox.models import EmailHeader, EmailRouter

class MessageRecipient(models.Model):
    RECIPIENT_TYPE_CHOICES = (
        ('from', 'FROM'),
        ('to', 'TO'),
        ('cc', 'CC'),
        ('bcc', 'BCC'),
        ('reply_to', 'REPLY TO'),  # Adicionado aqui
    )

    email_message = models.ForeignKey(EmailHeader, on_delete=models.CASCADE)
    email_router = models.ForeignKey(EmailRouter, on_delete=models.CASCADE)
    recipient_type = models.CharField(max_length=10, choices=RECIPIENT_TYPE_CHOICES)

    def __str__(self):
        return f"{self.email_router} - {self.recipient_type}"
