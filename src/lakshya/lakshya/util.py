
from django.core.mail.message import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings


def send_html_mail(subject, html_content, recipients, sender=None):
    """Send a HTML email from sender to one or many recipients"""
    if not isinstance(recipients, list):
        recipients = [recipients]
    if not sender:
        sender = settings.EMAIL_HOST_USER
    msg = EmailMultiAlternatives(subject, '', sender, recipients)
    msg.attach_alternative(html_content, "text/html")
    msg.send()


def send_email_from_template(template_name, context, subject, recipients):
    body = render_to_string(template_name, context)
    send_html_mail(subject, body, recipients)
