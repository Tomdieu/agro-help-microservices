from django.core.management.base import BaseCommand

from django.forms.models import model_to_dict
from django.contrib.auth import get_user_model
from core.models import Soil, SoilArea

User = get_user_model()
class Command(BaseCommand):
    help = 'création d\'un admin par défaut pour vous permettre de visulaisé vos sols par zone sur la carte et d\'en ajouter de nouvelles'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        print()
        admin = User.objects.create_user(username='soilAdmin', email='soilAdmin@gmail.com', password='12345678')
        admin.is_staff = True
        admin.is_superuser = True
        admin.save()
        self.stdout.write(self.style.SUCCESS(f'an admin user by default with the username {admin.get_username()} was created'))
        print()