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

def get_version():
    with open('kthresher.py') as f:
        for line in f:
            if line.startswith('__version__'):
                return eval(line.split('=')[-1])

setuptools.setup(
    name='kthresher',
    version=get_version(),
    description=('Purge Unused Kernels.'),
    long_description=('Tool to remove kernel image packages marked as '
                      'candidates for autoremoval.'),
    url='https://github.com/rackerlabs/kthresher',
    author='Tony Garcia',
    author_email='tony DOT garcia AT rackspace DOT com',
    license='Apache License, Version 2.0',
    entry_points={
        'console_scripts': [
            'kthresher=kthresher:main'
        ]
    },
    py_modules=['kthresher'],
    download_url='https://github.com/rackerlabs/kthresher/tarball/{0}'
                 .format(get_version()),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python',
        'Environment :: Console',
        'Operating System :: POSIX :: Linux',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2.7',
    ],
    data_files=[('/etc', ['kthresher.conf']),
                ('/usr/share/man/man8', ['kthresher.8'])
    ]
)
