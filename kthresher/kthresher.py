#!/usr/bin/env python
from __future__ import print_function


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

'''Tool to Purge Unused Kernels
Removes those kernel packages marked as candidate for autoremoval.
Those packages are generally installed via Unattended upgrade or meta-packages
By default the latest kernel and manual installations are marked to Never
Auto Remove.

Ubuntu suggestions on how to remove kernels:
  https://help.ubuntu.com/community/Lubuntu/Documentation/RemoveOldKernels
It uses a shell script:
http://bazaar.launchpad.net/~kirkland/byobu/trunk/view/head:/usr/bin/purge-old-kernels

thresher - A device that first separates the head of a stalk of grain from
the straw, and then further separates the kernel from the rest of the head.
'''

import re
import sys
import logging
import argparse
from platform import uname, dist
from distutils.version import LooseVersion

try:
    import apt
except ImportError:
    distro = dist()[0]
    if (distro == 'debian' or distro == 'Ubuntu'):
        print('Error, python apt library was not found\n'
              'python-apt and/or python3-apt packages provide it.',
              file=sys.stderr)
    else:
        print('{0} distro not supported'.format(distro), file=sys.stderr)
    sys.exit(1)


__version__ = "1.0.0"


def show_autoremovable_pkgs():
    '''List all the kernel related packages available for autoremoval.
    '''
    packages = {}
    ver_max_len = 0
    try:
        apt_cache = apt.Cache()
    except:
        print('Error, unable to obtain the cache!', file=sys.stderr)
        sys.exit(1)
    for pkg_name in apt_cache.keys():
        pkg = apt_cache[pkg_name]
        if (
           (pkg.is_installed and pkg.is_auto_removable) and
           (pkg.section == 'kernel' or re.match("^linux-.*$", pkg_name))
           ):
            packages[pkg_name] = pkg.installed.version
            if ver_max_len < len(pkg.installed.version):
                ver_max_len = len(pkg.installed.version)
    if packages:
        print('List of kernel packages available for autoremoval:')
        print('{0:>{width}} {1:<{width}}'.format('Version', 'Package',
              width=ver_max_len+2))
        for package in sorted(packages.keys()):
            print('{0:>{width}} {1:<{width}}'
                  .format(packages[package], package, width=ver_max_len+2))
    else:
        print('No kernel packages available for autoremoval.')


def kthreshing(purge=None, keep=1):
    '''Purge or list the unused kernels.
    By default keeps 1, besides the running kernel.
    '''
    kernels = {}
    ver_max_len = 0
    try:
        apt_cache = apt.Cache()
    except:
        print('Error, unable to obtain the cache!', file=sys.stderr)
        sys.exit(1)
    current_kernel_ver = uname()[2]
    kernel_pkg = apt_cache["linux-image-%s" % current_kernel_ver]
    logging.info('Running kernel is {0} v[{1}]'.format(kernel_pkg.name,
                 kernel_pkg.installed.version))
    for pkg_name in apt_cache.keys():
        pkg = apt_cache[pkg_name]
        if (
           (pkg.is_installed and pkg.is_auto_removable) and
           (pkg.section == 'kernel' and
            re.match("^linux-image-.*-generic$", pkg_name))
           ):
            if ver_max_len < len(pkg.installed.version):
                ver_max_len = len(pkg.installed.version)
            kernels.setdefault(pkg.installed.version, []).append(pkg.name)
    if kernels:
        logging.info('Attempting to keep {0} kernel package(s)'.format(keep))
        kernel_versions = list(kernels.copy().keys())
        logging.info('Found {0} kernel image(s) installed and available for '
                     'autoremoval'.format(len(kernel_versions)))
        logging.info('Pre-sorting: {0}'.format(kernel_versions))
        # Sadly this is broken in python3, https://bugs.python.org/issue14894
        sorted_kernel_list = sorted(kernel_versions, key=LooseVersion)
        logging.info('Post-sorting: {0}'.format(sorted_kernel_list))
        if keep >= len(kernel_versions):
            logging.error('Nothing to do, attempting to keep {0} out of {1} '
                          'kernel images.'
                          .format(keep, len(kernel_versions)))
            sys.exit(1)
        else:
            for index in range(0, len(sorted_kernel_list) - keep):
                kernel_version = sorted_kernel_list[index]
                logging.info('\tPurging packages from version: {0}'
                             .format(kernel_version))
                for pkg_name in kernels[kernel_version]:
                    logging.info('\t\tPurging: {0}'.format(pkg_name))
                    if purge:
                        pkg = apt_cache[pkg_name]
                        pkg.mark_delete(purge=True)
            if purge:
                try:
                    apt_cache.commit(
                        fetch_progress=apt.progress.text.AcquireProgress(),
                        install_progress=apt.progress.base.InstallProgress()
                    )
                except SystemError:
                    logging.error('Unable to commit the changes')
                    sys.exit(1)
    else:
        logging.info('No packages available for autoremoval.')


def main():
    '''The main function.
    '''
    parser = argparse.ArgumentParser(description='Purge Unused Kernels.',
                                     prog='kthresher')
    parser.add_argument('-d', '--dry-run', action='store_true',
                        help='List unused kernel images available to purge'
                        '(dry run)')
    parser.add_argument('-n', '--number', nargs='?', type=int, default=1,
                        help='Number of kernels to keep, default 1.', const=0,
                        metavar='N', choices=range(0, 10))
    parser.add_argument('-p', '--purge', help='Purge Unused Kernels.',
                        action='store_true')
    parser.add_argument('-s', '--show-autoremoval', action='store_true',
                        help='Show kernel packages available for autoremoval.')
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='Be verbose.')
    parser.add_argument('-V', '--version', action='version',
                        version='%(prog)s v{0}'.format(__version__),
                        help='Print version.')
    args = parser.parse_args()

    if args.show_autoremoval:
        show_autoremovable_pkgs()
        sys.exit(0)
    if args.dry_run or args.verbose:
        log_level = logging.INFO
    else:
        log_level = logging.ERROR
    logging.basicConfig(format='%(levelname)s: %(message)s',
                        level=log_level)
    if args.dry_run:
        logging.info('----- DRY RUN -----')
        kthreshing(purge=False, keep=args.number)
        sys.exit(0)
    if args.purge:
        kthreshing(purge=True, keep=args.number)
        sys.exit(0)
    else:
        print('Error, no argument used.', file=sys.stderr)
        parser.print_help()
        sys.exit(1)

if __name__ == "__main__":
    main()
