import os

from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, "README.rst")).read()

setup(
    name="django-attrs",
    version="0.1",
    packages=["attrs"],
    description="Entity-Attribute-Value (EAV) for Django through JSONField",
    long_description=README,
    author="yourname",
    author_email="dylan@dyve.net",
    url="https://github.com/zostera/django-attrs/",
    license="BSD-3-Clause",
    install_requires=["Django>=2", "psycopg2-binary>=2.7.5"],
)
