#!/usr/bin/env python3
import os

from setuptools import setup

about = {}  # type: ignore
root = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(root, "graphene_disable_introspection", "__version__.py")) as f:
    exec(f.read(), about)

with open("README.md", "r") as f:
    readme = f.read()

setup(
    name=about["__title__"],
    description=about["__description__"],
    long_description=readme,
    long_description_content_type="text/markdown",
    version=about["__version__"],
    author=about["__author__"],
    author_email=about["__author_email__"],
    url=about["__url__"],
    packages=["graphene_disable_introspection"],
    include_package_data=True,
    python_requires=">=3.10.*",
    license=about["__license__"],
)
