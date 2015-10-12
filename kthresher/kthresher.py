from __future__ import print_function

'''Tool to Purge Unused Kernels
Removes those kernel packages marked as candidate for autoremoval.
Those packages are generally installed via Unattended upgrade or meta-packages
By default the latest kernel and manual installations are marked to Never
Auto Remove.

thresher - A device that first separates the head of a stalk of grain from
the straw, and then further separates the kernel from the rest of the head.
'''

import re
import sys
import argparse
from platform import uname, dist

try:
    import apt
except ImportError:
    distro = dist()[0]
    if (dist == 'debian' or dist == 'Ubuntu'):
        print('Error, python apt library was not found\n'
              'python-apt and/or python3-apt packages provide it.',
              file=sys.stderr)
    else:
        print('{} distro not supported'.format(distro), file=sys.stderr)
    sys.exit(1)


__version__ = "0.2.1"


def kthreshing(purge=None, force=None):
    '''Purge or list the unused kernels.
    '''
    purging = []
    try:
        apt_cache = apt.Cache()
    except:
        print('Error, unable to obtain the cache!')
        sys.exit(1)
    current_kernel = uname()[2]
    kernel_pkg = apt_cache["linux-image-%s" % current_kernel]
    print('## Running kernel: {} [{}]'.format(kernel_pkg.name,
                                              kernel_pkg.installed.version))
    for pkg_name in apt_cache.keys():
        pkg = apt_cache[pkg_name]
        if (
           (pkg.is_installed and pkg.is_auto_removable) and
           (pkg.section == 'kernel' or re.match("^linux-", pkg_name))
           ):
            if purge:
                pkg.mark_delete(purge=True)
                purging.append(pkg.name)
                print('Mark for deletion: {} [{}]'
                      .format(pkg_name, pkg.installed.version))
            else:
                print('{} [{}]'.format(pkg_name,
                                       pkg.installed.version))
    if purging:
        try:
            apt_cache.commit()
        except SystemError:
            print('Unable to commit the changes')
            sys.exit(1)


def main():
    '''The main function.
    '''
    parser = argparse.ArgumentParser(description='Purge Unused Kernels.')
    parser.add_argument('-l', '--list-kernel', action='store_true',
                        help='List unused kernel packages available to purge.')
    parser.add_argument('-p', '--purge', help='Purge Unused Kernels.',
                        action='store_true')
    parser.add_argument('-f', '--force', help='Proceed without confirmation',
                        action='store_true')
    parser.add_argument('-v', '--version', action='store_true')
    args = parser.parse_args()

    if args.version:
        print('kthresher v{0}'.format(__version__))
        return
    if args.list_kernel:
        kthreshing(purge=None)
        sys.exit(0)
    if args.purge:
        kthreshing(purge=True, force=args.force)
        sys.exit(0)
    else:
        print('Error, no argument used.', file=sys.stderr)
        parser.print_help()
        sys.exit(1)

if __name__ == "__main__":
    main()
