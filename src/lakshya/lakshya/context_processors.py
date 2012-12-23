
def google_analytics(request):
    from django.conf import settings
    return {'GOOGLE_SITE_CODE': settings.GOOGLE_SITE_CODE}