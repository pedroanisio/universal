from rest_framework import serializers
from mailbox.models import EmailHeader, EmailRouter, MessageRecipient
from typing import Dict, List, Tuple

class EmailPostSerializer(serializers.Serializer):
    """
    Serializer for creating an email post, handling the serialization of email-related data.

    Attributes:
        subject (CharField): The subject of the email.
        date (DateTimeField): The date of the email.
        from_email (EmailField): The email address of the sender.
        to_emails (ListField): A list of recipient email addresses.
        cc_emails (ListField): A list of CC email addresses.
        bcc_emails (ListField): A list of BCC email addresses.
        reply_to_emails (ListField): A list of reply-to email addresses.
        size (IntegerField): The size of the email.
        message_id (CharField): The message ID of the email.
        references (CharField): Email references, optional.
        priority (CharField): The priority of the email, optional.
        mime_version (CharField): The MIME version of the email, optional.
        content_type (CharField): The content type of the email, optional.
        user_agent (CharField): The user agent of the email, optional.
    """

    subject = serializers.CharField(max_length=255)
    date = serializers.DateTimeField()
    from_email = serializers.EmailField()
    to_emails = serializers.ListField(child=serializers.EmailField(), required=False)
    cc_emails = serializers.ListField(child=serializers.EmailField(), required=False)
    bcc_emails = serializers.ListField(child=serializers.EmailField(), required=False)
    reply_to_emails = serializers.ListField(child=serializers.EmailField(), required=False)
    size = serializers.IntegerField()
    message_id = serializers.CharField(max_length=255)
    references = serializers.CharField(required=False, allow_blank=True)
    priority = serializers.CharField(required=False, max_length=50, allow_blank=True)
    mime_version = serializers.CharField(required=False, max_length=50, allow_blank=True)
    content_type = serializers.CharField(required=False, max_length=100, allow_blank=True)
    user_agent = serializers.CharField(required=False, max_length=255, allow_blank=True)

    def create(self, validated_data: Dict) -> EmailHeader:
        """
        Creates an EmailHeader instance along with associated recipients.

        Args:
            validated_data (Dict): The validated data from the serializer.

        Returns:
            EmailHeader: The created EmailHeader instance.
        """

        email_header = EmailHeader.objects.create(
            subject=validated_data['subject'],
            date=validated_data['date'],
            size=validated_data['size'],
            message_id=validated_data['message_id'],
            references=validated_data.get('references', ''),
            priority=validated_data.get('priority', ''),
            mime_version=validated_data.get('mime_version', ''),
            content_type=validated_data.get('content_type', ''),
            user_agent=validated_data.get('user_agent', '')
        )

        # Mapeamento explícito de campos para tipos de destinatários
        recipient_mappings = {
            'to_emails': 'to',
            'cc_emails': 'cc',
            'bcc_emails': 'bcc',
            'reply_to_emails': 'reply_to'
        }        

        # Process sender and recipients
        self._create_recipient(validated_data['from_email'], email_header, 'from')
        # Processamento dos destinatários
        for field, recipient_type in recipient_mappings.items():
            for email in validated_data.get(field, []):
                self._create_recipient(email, email_header, recipient_type)

        return email_header

    def _create_recipient(self, email: str, email_header: EmailHeader, recipient_type: str) -> None:
        """
        Creates or retrieves an EmailRouter instance and associates it with an EmailHeader.

        Args:
            email (str): The email address of the recipient.
            email_header (EmailHeader): The EmailHeader instance to associate with.
            recipient_type (str): The type of recipient (e.g., 'to', 'cc').

        Raises:
            serializers.ValidationError: If the email format is invalid.
        """
        try:
            email_router = self._create_or_get_email_router(email)
        except ValueError as e:
            raise serializers.ValidationError({"email": str(e)})

        MessageRecipient.objects.create(
            email_message=email_header,
            email_router=email_router,
            recipient_type=recipient_type
        )

    def _create_or_get_email_router(self, email: str) -> EmailRouter:
        """
        Retrieves or creates an EmailRouter based on the provided email address.

        Args:
            email (str): The email address to process.

        Returns:
            EmailRouter: The EmailRouter instance corresponding to the email address.

        Raises:
            ValueError: If the email format is invalid.
        """
        try:
            username, hostname = email.split('@')
        except ValueError:
            raise ValueError("Invalid email format.")

        email_router, _ = EmailRouter.objects.get_or_create(
            username=username, hostname=hostname
        )
        return email_router
