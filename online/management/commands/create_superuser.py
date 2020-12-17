from django.core.management.base import BaseCommand

from online.models import UserRegisteration


class Command(BaseCommand):
    help = 'Create Customer users'

    def add_arguments(self, parser):
        parser.add_argument('phone', type=str, help='PHONE')
        parser.add_argument('email', type=str, help='EMAIL')
        parser.add_argument('password', type=str, help='PASSWORD')
        parser.add_argument('first_name', type=str, help='FIRST_NAME')




    def handle(self, *args, **kwargs):
        phone = kwargs['phone']
        password = kwargs['password']
        email = kwargs['email']
        first_name = kwargs['first_name']
        user = UserRegisteration()
        user.phone = phone
        user.is_staff = True
        user.is_active = True
        user.set_password(password)
        user.email = email
        user.first_name = first_name
        user.save()

        self.stdout.write("SuperUser added successfully.")

