#!/usr/bin/env python
"""
sentry-heroku
=============

A Sentry extension which integrates with Heroku release tracking.

:copyright: (c) 2015 by Sentry Team, see AUTHORS for more details.
:license: Apache 2.0, see LICENSE for more details.
"""
from setuptools import setup, find_packages


install_requires = [
    # 'sentry>=7.5.0',
]

setup(
    name='sentry-heroku',
    version='0.1.0',
    author='David Cramer',
    author_email='dcramer@gmail.com',
    url='https://github.com/getsentry/sentry-heroku',
    description='A Sentry extension which integrates Heroku release tracking.',
    long_description=open('README.rst').read(),
    license='Apache 2.0',
    package_dir={'': 'src'},
    packages=find_packages('src'),
    zip_safe=False,
    install_requires=install_requires,
    include_package_data=True,
    entry_points={
        'sentry.apps': [
            'sentry_heroku = sentry_heroku',
        ],
        'sentry.plugins': [
            'sentry_heroku = sentry_heroku.plugin:HerokuPlugin',
        ]
    },
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ],
)
