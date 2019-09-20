"""A setuptools based setup module.

See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://github.com/pypa/sampleproject
"""

from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='maritime-update-manager',
    version='0.0.1',
    description='Update manager for maritime data',
    long_description=long_description,
    url='https://github.com/mapgears/maritime-update-manager',
    author='Mapgears',
    author_email='abrault@mapgears.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
    ],
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    python_requires='>=3.7',
    entry_points={
        'console_scripts': [
            'mum_update=mum.update:main',
        ],
        'mum.update_module': [
            'smac-m-data=mum.update.modules.smacm:SmacDataUpdater',
            'smac-m-mapfile=mum.update.modules.smacm:SmacMapUpdater',
            'pgrastertime=mum.update.modules.pgrastertime:PgRasterTimeUpdater',
        ]
    },
)
