"""
Django management command to wait for the database to be available.
"""
import time
from psycopg2 import OperationalError as Psycopg2OperationalError
from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to wait for the database to be available."""

    def handle(self, *args, **options):
        self.stdout.write("Waiting for database...")
        db_conn = False

        while not db_conn:
            try:
                # Try opening a connection
                connection = connections['default']
                connection.cursor()
                db_conn = True

            except (Psycopg2OperationalError, OperationalError):
                self.stdout.write(
                    "Database unavailable, waiting 1 second..."
                )
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS("Database available!"))
