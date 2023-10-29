from django.core.management import call_command
from django.core.management.base import BaseCommand
from django.db import connection

SQL = """
CALL public.redis_worker_extra()
"""


class Command(BaseCommand):
    def handle(self, *args, **options):
        cursor = connection.cursor()
        cursor.execute(SQL.strip())
