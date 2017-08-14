import random
import time

from django.core.management.base import BaseCommand

from django.contrib.auth.models import User
from products.models import Products


class Command(BaseCommand):

    def handle(self, *args, **options):
        self._gen_products()

    def _gen_products(self):
        print('Generate products')

        random.seed(time.time())

        user = User.objects.create_user('user')

        for i in range(25):
            Products.objects.create(
                name='name {}'.format(i),
                description='description {}'.format(i),
                owner=user
            )
