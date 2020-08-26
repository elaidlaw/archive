from django.core.management.base import BaseCommand, CommandError
import os

import config
from main.models import Photo

class Command(BaseCommand):
    help = 'Loads photos'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        photos_list = os.listdir(os.path.join(config.ARCHIVE_PATH, 'photos'))
        for photo in photos_list:
            if not (len(Photo.objects.filter(image_field=photo)) > 0 or photo[0] == '.'):
                Photo.objects.create(image_field=photo)

      