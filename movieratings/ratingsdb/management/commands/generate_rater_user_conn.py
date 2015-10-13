from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from ratingsdb.views import Rater


class Command(BaseCommand):
    def handle(self, *args, **options):
        for rater in Rater.objects.all():
            rater.user = User.objects.get(pk=rater.pk)
            rater.save()
