from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings


def send_email(subject, to, context, template_name):
    html_message = render_to_string(template_name=template_name, context=context)
    plain_massage = strip_tags(html_message)
    
    try:
        send_mail(
            subject=subject,
            message=plain_massage,
            html_message=html_message,
            recipient_list=[to],
            from_email=settings.EMAIL_HOST_USER
        )
    except:
        pass