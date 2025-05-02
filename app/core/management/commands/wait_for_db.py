"""
Django command to wait for the database to be available.
"""

from django.core.management.base import BaseCommand
from psycopg2 import OperationalError as Psycopg2Error

from django.db.utils import OperationalError


class Command(BaseCommand):
    """Django command to await for database."""

    def handle(self, *args, **options):
        """Entry point for the command."""
        self.stdout.write('Waiting for database...')
        db_conn = False
        while db_conn is False:
            try:
                self.check(databases=['default'])
                db_conn = True
            except( Psycopg2Error, OperationalError ):
                self.stdout.write('Database unavailable, waiting 1 second...')
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('Database available!'))