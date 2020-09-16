import os

from setuptools import setup, find_packages

DESCRIPTION = "ZExtenions - Jupyter extensions"
NAME = "zextensions"
PACKAGES = ["airflow_scheduler"]
AUTHOR = "PPExtensions Development Team"
AUTHOR_EMAIL = "jupyter@googlegroups.org"
URL = 'https://github.com/webscal3r/zextensions'
DOWNLOAD_URL = 'https://github.com/webscal3r/zextensions'
LICENSE = 'BSD License'

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md'), encoding='utf-8').read()

VERSION = '0.0.7'

install_requires = [
    'airflow',
    'requests',
]


setup(name=NAME,
      version=VERSION,
      description=DESCRIPTION,
      long_description=README,
      author=AUTHOR,
      author_email=AUTHOR_EMAIL,
      url=URL,
      download_url=DOWNLOAD_URL,
      license=LICENSE,
      packages=find_packages(),
      include_package_data=True,
      classifiers=[
          'Intended Audience :: System Administrators',
          'Intended Audience :: Science/Research',
          'License :: OSI Approved :: BSD License',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5'],
      install_requires=install_requires,
      )

