from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.db import models

class EmailRouter(models.Model):
    username = models.CharField(max_length=100)
    hostname = models.CharField(max_length=100)

    def clean(self):
        # Construir o endereço de email completo
        email_address = f"{self.username}@{self.hostname}"
        # Validar o endereço de email
        try:
            validate_email(email_address)
        except ValidationError:
            raise ValidationError("Endereço de email inválido.")

    def save(self, *args, **kwargs):
        # Converter para minúsculas antes de salvar
        self.username = self.username.lower()
        self.hostname = self.hostname.lower()
        # Chamar clean() para realizar a validação
        self.clean()
        super(EmailRouter, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.username}@{self.hostname}"

    class Meta:
        unique_together = ('username', 'hostname')
