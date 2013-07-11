# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
        name = 'twisted-memcached',
        version = '0.1',
        url = 'https://github.com/dustin/twisted-memcached',
        description = 'memcached protocol in twisted',
        packages = find_packages('.'),
        install_requires = (
                'Twisted',
            ),
        zip_safe=False,
    )


