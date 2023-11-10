from django.db.models import Q
from mailbox.models import EmailHeader

class EmailQueryService:
    @staticmethod
    def get_emails_sent_by(user_id):
        sent_emails = EmailHeader.objects.filter(
            messagerecipient__email_router=user_id, 
            messagerecipient__recipient_type='from'
        )
        return sent_emails

    @staticmethod
    def get_emails_sent_to(user_id):
        received_emails = EmailHeader.objects.filter(
            messagerecipient__email_router=user_id, 
            messagerecipient__recipient_type='to'
        )
        return received_emails