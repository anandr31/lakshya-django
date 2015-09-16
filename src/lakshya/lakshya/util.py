
from django.core.mail.message import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
from crowdfunding.models import Project, Pledge, Message, ProjectImage, ProjectUpdate
from datetime import date
from crowdfunding.constants import MAIL_NOT_SENT, CAMPAIGN_FULLY_BACKED_MAIL_SENT, \
        CAMPAIGN_EXPIRED_UNSUCCESSFULLY_MAIL_SENT, UPDATE_MAIL_NOT_SENT, UPDATE_MAIL_SENT



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


def send_cron_job_emails(request):
    projects = Project.objects.all()
    for project in projects:
        if campaign_fully_backed(project):
            send_email_fully_funded_backers(project, request)
            update_project_sent_email_status(project, CAMPAIGN_FULLY_BACKED_MAIL_SENT)
        elif campaign_expired_unsuccessfully(project):
            send_email_campaign_unsuccessful_backers(project, request)
            send_email_campaign_unsuccessful_author(project, request)
            update_project_sent_email_status(project, CAMPAIGN_EXPIRED_UNSUCCESSFULLY_MAIL_SENT)
        elif campaign_within_three_days_expiry(project):
            send_email_campaign_close_to_expiry_author(project, request)

        if campaign_new_update(project):
            send_email_campaign_update_backers(project, request)


def campaign_fully_backed(project):
    return (project.is_fully_pledged() and project.mail_status == MAIL_NOT_SENT)


def campaign_expired_unsuccessfully(project):
    return (project.is_expired() and (project.get_total_pledged_amount() < project.goal) and \
                                        project.mail_status == MAIL_NOT_SENT)


def campaign_new_update(project):
    # Has there been an update in the last 24 hours?
    return (ProjectUpdate.objects.filter(project=project, mail_status=UPDATE_MAIL_NOT_SENT).exists())
    # return ((date.today() - project.updates.first().timestamp.date()).days <= 1)


def campaign_within_three_days_expiry(project):
    return (project.get_days_remaining() <= 3)


def update_project_sent_email_status(project, status):
    project.mail_status = status
    project.save()


def send_email_fully_funded_backers(project, request):
    subject = '[NITW Crowdfund] Campaign you backed gets fully funded!'
    template = 'emails/campaign_successful_backer.html'
    pledges = Pledge.objects.filter(project=project).all()
    # recipients = map(str,Pledge.objects.filter(project=project).values_list('user__email', flat=True))
    for pledge in pledges:
        context = {'pledge': pledge, 'request': request}
        recipient = pledge.user.email
        send_email_from_template(template, context, subject, recipient)


def send_email_campaign_unsuccessful_backers(project, request):
    subject = '[NITW Crowdfund] Campaign Ended'
    template = 'emails/campaign_unsuccessful_backer.html'
    pledges = Pledge.objects.filter(project=project).all()
    # recipients = map(str,Pledge.objects.filter(project=project).values_list('user__email', flat=True))
    for pledge in pledges:
        context = {'pledge': pledge, 'request': request}
        recipient = pledge.user.email
        send_email_from_template(template, context, subject, recipient)


def send_email_campaign_unsuccessful_author(project, request):
    subject = '[NITW Crowdfund] Campaign Ended'
    context = {'project': project, 'request': request}
    template = 'emails/campaign_unsuccessful_author.html'
    recipient = project.author.email
    send_email_from_template(template, context, subject, recipient)


def send_email_campaign_update_backers(project, request):
    subject = '[NITW Crowdfund] New Project Campaign Update'
    template = 'emails/project_updated_backer.html'
    pledges = Pledge.objects.filter(project=project).all()
    # recipients = map(str,Pledge.objects.filter(project=project).values_list('user__email', flat=True))
    for pledge in pledges:
        context = {'pledge': pledge, 'request': request, 'updates': ProjectUpdate.objects.filter(project=project, mail_status=UPDATE_MAIL_NOT_SENT)}
        recipient = pledge.user.email
        send_email_from_template(template, context, subject, recipient)
    ProjectUpdate.objects.filter(project=project, mail_status=UPDATE_MAIL_NOT_SENT).update(mail_status = UPDATE_MAIL_SENT)
        # ProjectUpdate.save()


def send_email_campaign_close_to_expiry_author(project, request):
    subject = '[NITW Crowdfund] Your Campaign is about to end'
    context = {'project': project, 'request': request}
    template = 'emails/campaign_close_to_expiry_author.html'
    recipient = project.author.email
    send_email_from_template(template, context, subject, recipient)


    # collect list of projects, check for >=100% backing change, get list of emails for each project,
    # call send-email function with list of ids, html email template, record that email is sent for that project

