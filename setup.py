from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in agua_jerusalen_frappe/__init__.py
from agua_jerusalen_frappe import __version__ as version

setup(
	name="agua_jerusalen_frappe",
	version=version,
	description="Aplicacion para la junta de agua potable de jerusalen",
	author="Luis Pillaga",
	author_email="lpillag@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
