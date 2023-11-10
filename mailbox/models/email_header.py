from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone

class EmailHeader(models.Model):
    subject = models.CharField(max_length=255)
    date = models.DateTimeField()
    size = models.PositiveIntegerField()
    message_id = models.CharField(max_length=255, unique=True)
    references = models.TextField(blank=True, null=True)
    priority = models.CharField(max_length=50, blank=True, null=True)
    mime_version = models.CharField(max_length=50, blank=True, null=True)
    content_type = models.CharField(max_length=100, blank=True, null=True)
    user_agent = models.CharField(max_length=255, blank=True, null=True)

    def clean(self):
        # Verificar se a data não é futura
        if self.date and self.date > timezone.now():
            raise ValidationError("A data não pode ser no futuro.")

        # Verificar se message_id não está vazio
        if not self.message_id:
            raise ValidationError("O campo message_id não pode estar vazio.")

    def save(self, *args, **kwargs):
        # Chamar clean() para realizar a validação
        self.clean()
        super(EmailHeader, self).save(*args, **kwargs)

    # Método __str__ já definido
    def __str__(self):
        return self.subject