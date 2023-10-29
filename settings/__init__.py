import os

from configurations import Configuration, values
from django_installed_apps_generator import INSTALLED_APPS


INSTALLED_APPS = (
    list(
        filter(
            lambda s: s.strip() and s.strip()[0] != "#",
            open("settings/INSTALLED_APPS.txt").read().splitlines(),
        )
    )
    + INSTALLED_APPS
)


class Base(Configuration):
    DATABASES = values.DatabaseURLValue(environ_name="DJANGO_DATABASE_URL")
    INSTALLED_APPS = INSTALLED_APPS
    REDIS_PULL_QUEUE_LIST = ["response", "exception"]


class Dev(Base):
    DEBUG = True


class Prod(Base):
    DEBUG = False
