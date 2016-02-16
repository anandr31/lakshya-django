# A management command to send emails to authors and pledgers based on the status of the projects.
# This will be run using a cron job once every day.

from lakshya.util import send_cron_job_emails
from django.core.management.base import BaseCommand

class Command(BaseCommand):
	args = ''
	help = 'Sends emails to pledgers and authors based on the status of the project'
	def handle(self, *args, **options):
		send_cron_job_emails()