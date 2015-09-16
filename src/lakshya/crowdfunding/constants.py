
# Project Status
UNAPPROVED = 1
APPROVED = 2
EXPIRED = 3
SUCCESSFUL = 4
CANCELLED = 5

PROJECT_STATUS = ((UNAPPROVED, 'Unapproved'),
				   (APPROVED, 'Approved'),
				   (EXPIRED, 'Expired'),
				   (SUCCESSFUL, 'Successful'),
				   (CANCELLED, 'Cancelled'),
			   )


MAIL_NOT_SENT = 0
CAMPAIGN_FULLY_BACKED_MAIL_SENT = 1
CAMPAIGN_EXPIRED_UNSUCCESSFULLY_MAIL_SENT = 2


PROJECT_MAIL_STATUSES = ((MAIL_NOT_SENT, "Mail not sent"),
						(CAMPAIGN_FULLY_BACKED_MAIL_SENT, "Campaign fully backed mail sent"),
						(CAMPAIGN_EXPIRED_UNSUCCESSFULLY_MAIL_SENT, "Campaign expired unsuccessfully mail sent"))
