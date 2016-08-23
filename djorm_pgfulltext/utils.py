import psycopg2

from django.db import connection
from django.utils.text import force_text


def adapt(text):
    if not connection.connection:
        connection.cursor()
    a = psycopg2.extensions.adapt(force_text(text))
    a.prepare(connection.connection)
    return a
