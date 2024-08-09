from setuptools import setup

from demo.version import get_version

setup(
    name='demo',
    version=get_version(),
    packages=['demo'],
    include_package_data=True,
    install_requires=["setuptools"],
)
