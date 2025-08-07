"""
Django command to wait for the db to be avalailbe
"""

import time
from psycopg2 import OperationalError as Psycopg2Error
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    """Django command to wait for database"""

    def handle(self,*args,**options):
        """ENTRE POINT FOR CMMANDS"""
        self.stdout.write("WAiting for Database.....")
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up=True
            except (Psycopg2Error,OperationalError):
                self.stdout.write("Database unavaliable, waiting 1 secon....")
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS("DATABASE AVALIABLE"))