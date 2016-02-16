# A management command to send emails to authors and pledgers based on the status of the projects.
# This will be run using a cron job once every day.
from datetime import datetime
from lakshya.util import send_cron_job_emails
from django.core.management.base import BaseCommand

class Command(BaseCommand):
	args = ''
	help = 'Sends emails to pledgers and authors based on the status of the project'
	def handle(self, *args, **options):
		self.stdout.write("Job starts at [" + datetime.now().strftime('%d/%m/%Y %H:%M:%S') + "]")
		send_cron_job_emails()
		self.stdout.write("Job ends at [" + datetime.now().strftime('%d/%m/%Y %H:%M:%S') + "]")