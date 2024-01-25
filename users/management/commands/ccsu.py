from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='my@email.net',
            first_name='admin',
            last_name='DB_admin',
            is_staff=True,
            is_superuser=True,
            is_active=True,
        )

        user.set_password('admin280310')
        user.save()
