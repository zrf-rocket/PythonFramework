from datetime import timedelta
from django.core.mail import mail_admins
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

User = get_user_model()


class Command(BaseCommand):
    help = 'Send Email Information to Admin....'

    def handle(self, *args, **options):
        today = timezone.now()
        yesterday = today - timedelta(1)
        user_count = User.objects.filter(date_joined__range=(yesterday, today)).count()
        if user_count:
            message = "You have got {} user(s) in the past 24 hours".format(user_count)
            subject = (f"New user count for {today.strftime('%Y-%m-%d')}: {user_count}")
            try:
                mail_admins(subject=subject, message=message, html_message=None)
            except Exception as e:
                self.stderr.write(f"Send email error, msg:{e}")
            self.stdout.write(f'Send email success, user count:{user_count}')
        else:
            self.stdout.write('No new users today')
