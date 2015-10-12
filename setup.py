#!/usr/bin/env python

import setuptools

setuptools.setup(
    name='kthresher',
    version='0.2.1',
    description=('Tool to purge unused kernels.'),
    author='Tony Garcia',
    author_email='tony DOT garcia AT rackspace DOT com',
    entry_points={
        'console_scripts': [
            'kthresher=kthresher.kthresher:main'
        ]
    },
    packages=['kthresher'],
    url='https://github.com/rackerlabs/kthresher',
    download_url='https://github.com/rackerlabs/kthresher/tarball/0.2.1',
    zip_safe=False
)
