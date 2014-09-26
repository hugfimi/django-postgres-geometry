# coding=utf-8
from setuptools import setup, find_packages


setup(
    name="django-posgtres-geometry",
    version="0.1.2",
    packages=find_packages(),
    install_requires=['django', 'psycopg2', 'mock'],
    description="Django ORM field for Postgres geometry types",
    author="Daniele Esposti",
    author_email="expo@expobrain.net",
    maintainer="Bjarki Ásbjarnarson",
    maintainer_email="bjarki@hugfimi.is",
    url="http://github.com/hugfimi/django-postgres-geometry",
)
