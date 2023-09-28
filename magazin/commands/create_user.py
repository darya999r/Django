from django.core.management.base import BaseCommand

from magazin.models import User


class Command(BaseCommand):
    help = "Create user."

    def handle(self, *args, **kwargs):
        user = User(name='Oleg', email='olegjfv@mail.com', phone='465113515', address='xfbtgfbx',
                    registered_at='30.12.1984')
        user.save()
        self.stdout.write(f'{user}')