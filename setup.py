#!/usr/bin/env python
# -*- coding: utf-8 -*-

# https://jeffknupp.com/blog/2013/08/16/open-sourcing-a-python-project-the-right-way/
# https://github.com/audreyr/cookiecutter-pypackage
# pypi release checklist: https://gist.github.com/audreyr/5990987

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=6.0', 'Scrapy>=1.5.0', ]

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest', ]

setup(
    author="Gino Palazzo",
    author_email='ginopalazzo@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    description="Are you ready to operate, Doctor? - I'd love to, but first I have to perform surgery.",
    entry_points={
        'console_scripts': [
            'zoidberg=zoidberg.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='zoidberg drzoidberg dr-zoidberg doctor',
    name='dr-zoidberg',
    packages=find_packages(include=['zoidberg']),
    # packages=find_packages(),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/ginopalazzo/zoidberg',
    version='0.1.3.6',
    zip_safe=False,
)
