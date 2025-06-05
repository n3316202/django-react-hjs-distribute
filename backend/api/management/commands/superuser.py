from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model
from decouple import config

# dev_8
DJANGO_SUPERUSER_USERNAME = 'admin'
DJANGO_SUPERUSER_PASSWORD = '1234'
DJANGO_SUPERUSER_EMAIL = 'admin@admin.com'

class Command(BaseCommand):
    help = 'Create a superuser if it does not exist'

    def handle(self, *args, **options):
        try:
            User = get_user_model()
            if User.objects.filter(username=DJANGO_SUPERUSER_USERNAME).exists():
                self.stdout.write(self.style.WARNING('Superuser already exists. Skipping creation.'))
                return

            user = User(
                email=DJANGO_SUPERUSER_EMAIL,
                username=DJANGO_SUPERUSER_USERNAME,
            )
            user.set_password(DJANGO_SUPERUSER_PASSWORD)
            user.is_superuser = True
            user.is_staff = True
            user.is_admin = True  # ⚠️ 사용자 모델에 따라 필요 없을 수도 있음
            user.save()
            self.stdout.write(self.style.SUCCESS('Successfully created new superuser'))
        except Exception as e:
            raise CommandError(f"Failed to create superuser: {e}")