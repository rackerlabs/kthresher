#!/usr/bin/env python
# Copyright 2015 Tony Garcia
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import setuptools

setuptools.setup(
    name='kthresher',
    version='0.2.3',
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
    download_url='https://github.com/rackerlabs/kthresher/tarball/0.2.3',
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python',
        'Environment :: Console',
        'Operating System :: POSIX :: Linux',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ]
)
