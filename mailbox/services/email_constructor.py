from django.db.models import Q
from mailbox.models import EmailHeader, MessageRecipient

class EmailConstructor:
    def __init__(self, message_id):
        self.message_id = message_id
        self.header = EmailHeader.objects.get(message_id=message_id)
        self.recipients = self.header.message_recipients.all()
        self.from_email = None
        self.to_emails = []
        self.cc_emails = []
        self.bcc_emails = []

        self._construct_email()

    def _construct_email(self):
        # Construir os componentes da mensagem de email
        for recipient in self.recipients:
            email_address = f"{recipient.email_router.username}@{recipient.email_router.hostname}"

            if recipient.recipient_type == 'from':
                self.from_email = email_address
            elif recipient.recipient_type == 'to':
                self.to_emails.append(email_address)
            elif recipient.recipient_type == 'cc':
                self.cc_emails.append(email_address)
            elif recipient.recipient_type == 'bcc':
                self.bcc_emails.append(email_address)

    def get_email_data(self):
        # Retornar os dados da mensagem de email reconstruída
        return {
            'from': self.from_email,
            'to': self.to_emails,
            'cc': self.cc_emails,
            'bcc': self.bcc_emails,
            'subject': self.header.subject,
            'date': self.header.date,
            # Outros campos do cabeçalho podem ser adicionados aqui
        }

# # Uso da classe
# email_constructor = EmailConstructor(message_id='algum_message_id')
# email_data = email_constructor.get_email_data()
