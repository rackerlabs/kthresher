|logo0|

kthresher
=========

.. image:: https://img.shields.io/github/release/rackerlabs/kthresher.svg
        :target: https://github.com/rackerlabs/kthresher/releases/latest
        :alt: Github release
.. image:: https://img.shields.io/travis/rackerlabs/kthresher/master.svg?logo=travis&label=master
        :target: https://travis-ci.org/rackerlabs/kthresher
        :alt: Build Master Status
.. image:: https://img.shields.io/travis/rackerlabs/kthresher/master.svg?logo=travis&label=development
        :target: https://travis-ci.org/rackerlabs/kthresher
        :alt: Build Development Status
.. image:: https://img.shields.io/github/license/rackerlabs/kthresher.svg
        :target: https://raw.githubusercontent.com/rackerlabs/kthresher/master/LICENSE
        :alt: License
.. image:: https://img.shields.io/twitter/url/https/github.com/rackerlabs/kthresher.svg?style=social
        :target: https://twitter.com/intent/tweet?text=Check%20this%20out:&url=https%3A%2F%2Fgithub.com%2Frackerlabs%2Fkthresher
        :alt: Twitter

Tool to remove unused kernels that were installed automatically in Debian/Ubuntu.

This tool removes those kernel packages marked as candidate for autoremoval. Those packages are generally installed via Unattended upgrade or meta-packages.

By default, on apt 1.0 and below, the booted kernel, the latest-installed kernel and the latest kernel are set to "NeverAutoRemove". Or, for apt 1.2 and above, the booted kernel, the latest-installed kernel, the latest kernel and the second-latest kernel are set to "NeverAutoRemove".

The official documentation has multiple suggestions on how to remove kernels:
  https://help.ubuntu.com/community/RemoveOldKernels

A great recommendation is to make use of unattended-upgrades `u-u` (`debian <https://wiki.debian.org/UnattendedUpgrades>`__, `ubuntu <https://help.ubuntu.com/community/AutomaticSecurityUpdates>`__). Since version **1.0** (`debian <https://packages.debian.org/search?keywords=unattended-upgrades>`__, `ubuntu <https://packages.ubuntu.com/search?keywords=unattended-upgrades>`__) *u-u* removes unused kernel packages by default (*Remove-Unused-Kernel-Packages*).
Some distribution versions may not make reference or may comment out that setting in its configuration, but unless it is explicitly disabled, *u-u* will attempt to remove unused kernels. `More info here <https://github.com/rackerlabs/kthresher/issues/79>`__.

For scenarios where *u-u* is not available or older than **1.0**, `kthresher` is still a good option.


*thresher - A device that first separates the head of a stalk of grain from the straw, and then further separates the kernel from the rest of the head.*

-----

|version| |downloads-pypi| |versions| |license| |stars-github|

-----

.. contents:: Table of Contents
   :depth: 1
   :backlinks: none

-----

How a package is marked for autoremoval?
----------------------------------------

Whenever a package is auto-installed and there is no other dependency for it, the package is marked as a candidate for autoremoval, there is an exception if the *APT* configuration does have the package marked as "NeverAutoRemove".


How the kernel image is added into the "APT::NeverAutoRemove::" config?
-----------------------------------------------------------------------

When a kernel image is installed the *postinstall* script will issue the *run-parts* on */etc/kernel/postinst.d/* and */etc/kernel/postinst.d/${version}* if any exist.  The *run-parts* script will run each one of the scripts located in that directory, e.g.

.. code-block:: bash

    # ls -1 /etc/kernel/postinst.d/
    apt-auto-removal
    initramfs-tools
    update-notifier
    x-grub-legacy-ec2
    zz-update-grub

All the scripts found by *run-parts* are executed on post install of the kernel package and the output of apt-get install/upgrade/dist-upgrade will show them, e.g.

.. code-block:: bash

    run-parts: executing /etc/kernel/postinst.d/apt-auto-removal 3.13.0-96-generic /boot/vmlinuz-3.13.0-96-generic
    run-parts: executing /etc/kernel/postinst.d/initramfs-tools 3.13.0-96-generic /boot/vmlinuz-3.13.0-96-generic
    run-parts: executing /etc/kernel/postinst.d/update-notifier 3.13.0-96-generic /boot/vmlinuz-3.13.0-96-generic
    run-parts: executing /etc/kernel/postinst.d/x-grub-legacy-ec2 3.13.0-96-generic /boot/vmlinuz-3.13.0-96-generic
    run-parts: executing /etc/kernel/postinst.d/zz-update-grub 3.13.0-96-generic /boot/vmlinuz-3.13.0-96-generic

The first script *"apt-auto-removal"* takes care of adding a configuration in /etc/apt/apt.conf.d/01autoremove-kernels this script generates that list based on the logic described above, it means that the NeverAutoRemove may have anything between two to three kernels listed.

Supported Operating Systems
---------------------------

* Debian (Tested on Version(s))
    * `8 <https://www.debian.org/releases/jessie/>`__
    * `9 <https://www.debian.org/releases/stretch/>`__
* Ubuntu (Tested on Version(s))
    * `12.04 <http://releases.ubuntu.com/precise/>`__
    * `14.04 <http://releases.ubuntu.com/trusty/>`__
    * `16.04 <http://releases.ubuntu.com/xenial/>`__
    * `17.10 <http://releases.ubuntu.com/artful/>`__


Installation
------------
script
~~~~~~

.. code-block:: bash

    wget -O kthresher https://raw.githubusercontent.com/rackerlabs/kthresher/master/kthresher.py
    chmod u+x kthresher

pip
~~~

.. code-block:: bash

    pip install kthresher

or

.. code-block:: bash

    pip install git+https://github.com/rackerlabs/kthresher.git

Github
~~~~~~

.. code-block:: bash

    git clone https://github.com/rackerlabs/kthresher.git
    cd kthresher && python setup.py install


Usage
-----

.. code-block::

    $ kthresher -h
    usage: kthresher [-h] [-c FILE] [-d] [-H] [-k [N]] [-p] [-s] [-v] [-V]
    
    Purge Unused Kernels.
    
    optional arguments:
      -h, --help            show this help message and exit
      -c FILE, --config FILE
                            Config file, default is /etc/kthresher.conf
      -d, --dry-run         List unused kernel images available to purge(dry run).
                            Is always verbose.
      -H, --headers         Include the search for kernel headers.
      -k [N], --keep [N]    Number of kernels to keep, default 1.
      -p, --purge           Purge Unused Kernels.
      -s, --show-autoremoval
                            Show kernel packages available for autoremoval.
      -v, --verbose         Be verbose.
      -V, --version         Print version.


Examples
--------

List which kernel images and its dependencies would remove(dry run)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::

    # kthresher -d
    INFO: Attempting to read /etc/kthresher.conf.
    INFO: Config file /etc/kthresher.conf is empty or does not exist, ignoring.
    INFO: Options: {'purge': False, 'verbose': False, 'dry_run': True, 'keep': 1}
    INFO: ----- DRY RUN -----
    INFO: Running kernel is linux-image-3.13.0-83-generic v[3.13.0-83.127]
    INFO: Attempting to keep 1 kernel package(s)
    INFO: Found 4 kernel image(s) installed and available for autoremoval
    INFO: Pre-sorting: ['3.16.0-60.80~14.04.1', '3.13.0-77.121', '3.13.0-63.103', '3.16.0-33.44~14.04.1']
    INFO: Post-sorting: ['3.13.0-63.103', '3.13.0-77.121', '3.16.0-33.44~14.04.1', '3.16.0-60.80~14.04.1']
    INFO:   Purging packages from version: 3.13.0-63.103
    INFO:           Purging: linux-image-extra-3.13.0-63-generic
    INFO:           Purging: linux-image-3.13.0-63-generic
    INFO:   Purging packages from version: 3.13.0-77.121
    INFO:           Purging: linux-image-3.13.0-77-generic
    INFO:           Purging: linux-image-extra-3.13.0-77-generic
    INFO:   Purging packages from version: 3.16.0-33.44~14.04.1
    INFO:           Purging: linux-image-3.16.0-33-generic


Show all kernel packages available for autoremoval
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::

    # kthresher -s
    List of kernel packages available for autoremoval:
                   Version Package
              3.13.0.83.89 linux-generic
              3.13.0-51.84 linux-headers-3.13.0-51
              3.13.0-51.84 linux-headers-3.13.0-51-generic
             3.13.0-71.114 linux-headers-3.13.0-71
             3.13.0-71.114 linux-headers-3.13.0-71-generic
             3.13.0-77.121 linux-headers-3.13.0-77
             3.13.0-77.121 linux-headers-3.13.0-77-generic
             3.13.0-79.123 linux-headers-3.13.0-79
             3.13.0-79.123 linux-headers-3.13.0-79-generic
             3.13.0-63.103 linux-image-3.13.0-63-generic
             3.13.0-77.121 linux-image-3.13.0-77-generic
      3.16.0-33.44~14.04.1 linux-image-3.16.0-33-generic
      3.16.0-60.80~14.04.1 linux-image-3.16.0-60-generic
             3.13.0-63.103 linux-image-extra-3.13.0-63-generic
             3.13.0-77.121 linux-image-extra-3.13.0-77-generic
              3.13.0.83.89 linux-image-generic


Purge Unused Kernels, keep 3 kernels and be verbose
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::

    # kthresher -p -k3 -v
    INFO: Attempting to read /etc/kthresher.conf.
    INFO: Config file /etc/kthresher.conf is empty or does not exist, ignoring.
    INFO: Options: {'purge': True, 'verbose': True, 'dry_run': False, 'keep': 3}
    INFO: Running kernel is linux-image-3.13.0-83-generic v[3.13.0-83.127]
    INFO: Attempting to keep 3 kernel package(s)
    INFO: Found 4 kernel image(s) installed and available for autoremoval
    INFO: Pre-sorting: ['3.16.0-60.80~14.04.1', '3.13.0-77.121', '3.13.0-63.103', '3.16.0-33.44~14.04.1']
    INFO: Post-sorting: ['3.13.0-63.103', '3.13.0-77.121', '3.16.0-33.44~14.04.1', '3.16.0-60.80~14.04.1']
    INFO:   Purging packages from version: 3.13.0-63.103
    INFO:           Purging: linux-image-extra-3.13.0-63-generic
    INFO:           Purging: linux-image-3.13.0-63-generic
    Fetched 0 B in 0s (0 B/s)
    (Reading database ... 169514 files and directories currently installed.)
    Removing linux-image-extra-3.13.0-63-generic (3.13.0-63.103) ...
    run-parts: executing /etc/kernel/postinst.d/apt-auto-removal 3.13.0-63-generic /boot/vmlinuz-3.13.0-63-generic
    run-parts: executing /etc/kernel/postinst.d/initramfs-tools 3.13.0-63-generic /boot/vmlinuz-3.13.0-63-generic
    update-initramfs: Generating /boot/initrd.img-3.13.0-63-generic
    run-parts: executing /etc/kernel/postinst.d/zz-update-grub 3.13.0-63-generic /boot/vmlinuz-3.13.0-63-generic
    Generating grub configuration file ...
    Found linux image: /boot/vmlinuz-3.16.0-60-generic
    Found initrd image: /boot/initrd.img-3.16.0-60-generic
    Found linux image: /boot/vmlinuz-3.16.0-33-generic
    Found initrd image: /boot/initrd.img-3.16.0-33-generic
    Found linux image: /boot/vmlinuz-3.13.0-83-generic
    Found initrd image: /boot/initrd.img-3.13.0-83-generic
    Found linux image: /boot/vmlinuz-3.13.0-77-generic
    Found initrd image: /boot/initrd.img-3.13.0-77-generic
    Found linux image: /boot/vmlinuz-3.13.0-63-generic
    Found initrd image: /boot/initrd.img-3.13.0-63-generic
    done
    Purging configuration files for linux-image-extra-3.13.0-63-generic (3.13.0-63.103) ...
    Removing linux-image-3.13.0-63-generic (3.13.0-63.103) ...
    Examining /etc/kernel/postrm.d .
    run-parts: executing /etc/kernel/postrm.d/initramfs-tools 3.13.0-63-generic /boot/vmlinuz-3.13.0-63-generic
    update-initramfs: Deleting /boot/initrd.img-3.13.0-63-generic
    run-parts: executing /etc/kernel/postrm.d/zz-update-grub 3.13.0-63-generic /boot/vmlinuz-3.13.0-63-generic
    Generating grub configuration file ...
    Found linux image: /boot/vmlinuz-3.16.0-60-generic
    Found initrd image: /boot/initrd.img-3.16.0-60-generic
    Found linux image: /boot/vmlinuz-3.16.0-33-generic
    Found initrd image: /boot/initrd.img-3.16.0-33-generic
    Found linux image: /boot/vmlinuz-3.13.0-83-generic
    Found initrd image: /boot/initrd.img-3.13.0-83-generic
    Found linux image: /boot/vmlinuz-3.13.0-77-generic
    Found initrd image: /boot/initrd.img-3.13.0-77-generic
    done
    Purging configuration files for linux-image-3.13.0-63-generic (3.13.0-63.103) ...
    Examining /etc/kernel/postrm.d .
    run-parts: executing /etc/kernel/postrm.d/initramfs-tools 3.13.0-63-generic /boot/vmlinuz-3.13.0-63-generic
    run-parts: executing /etc/kernel/postrm.d/zz-update-grub 3.13.0-63-generic /boot/vmlinuz-3.13.0-63-generic


Verbose run using a non-default config file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    # kthresher -c myconf.conf
    INFO: Attempting to read myconf.conf.
    INFO: Options found: ['keep', 'dry_run'].
    INFO: Valid setting found "keep"
    INFO:   keep = 1
    INFO: Valid setting found "dry_run"
    INFO:   dry_run = True
    INFO: Options: {'purge': False, 'verbose': True, 'dry_run': True, 'keep': 1}
    INFO: ----- DRY RUN -----
    INFO: Running kernel is linux-image-3.13.0-83-generic v[3.13.0-83.127]
    INFO: Attempting to keep 1 kernel package(s)
    INFO: Found 2 kernel image(s) installed and available for autoremoval
    INFO: Pre-sorting: ['3.16.0-60.80~14.04.1', '3.16.0-33.44~14.04.1']
    INFO: Post-sorting: ['3.16.0-33.44~14.04.1', '3.16.0-60.80~14.04.1']
    INFO:   Purging packages from version: 3.16.0-33.44~14.04.1
    INFO:           Purging: linux-image-3.16.0-33-generic

Content of myconf.conf is:
.. code-block::

    [main]
    keep    = 1
    dry_run = yes
    #purge = yes


Dry run including headers
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    # kthresher -v -d -H
    INFO: Attempting to read /etc/kthresher.conf.
    INFO: Options found: ['keep', 'dry_run', 'purge', 'verbose'].
    INFO: Valid setting found "keep"
    INFO:   keep = 2
    INFO: Valid setting found "dry_run"
    INFO:   dry_run = False
    INFO: Valid setting found "purge"
    INFO:   purge = True
    INFO: Valid setting found "verbose"
    INFO:   verbose = True
    INFO: Options: {'verbose': True, 'dry_run': True, 'keep': 2, 'purge': True, 'headers': True}
    INFO: ----- DRY RUN -----
    INFO: Running kernel is linux-image-3.13.0-83-generic v[3.13.0-83.127]
    INFO: Attempting to keep 2 kernel package(s)
    INFO: Found 4 kernel image(s) installed and available for autoremoval
    INFO: Pre-sorting: ['3.16.0-60.80~14.04.1', '3.16.0-33.44~14.04.1', '3.13.0-85.129', '3.13.0-79.123']
    INFO: Post-sorting: ['3.13.0-79.123', '3.13.0-85.129', '3.16.0-33.44~14.04.1', '3.16.0-60.80~14.04.1']
    INFO:   Purging packages from version: 3.13.0-79.123
    INFO:           Purging: linux-image-3.13.0-79-generic
    INFO:           Purging: linux-headers-3.13.0-79-generic
    INFO:           Purging: linux-headers-3.13.0-79
    INFO:   Purging packages from version: 3.13.0-85.129
    INFO:           Purging: linux-image-3.13.0-85-generic
    INFO:           Purging: linux-headers-3.13.0-85
    INFO:           Purging: linux-headers-3.13.0-85-generic


Testing
-------

The below code can be used to install up to a fixed amount of kernels and headers if available of the form "linux-(image|headers)-[0-9].*-(generic|amd64)" at the end it should end up with two or three kernels in the NeverAutoRemove list, including the latest, the prior to latest and the running kernel.

.. code-block:: python

    #!/usr/bin/env python
    '''Installs available linux-image-* and linux-headers-*
    And set them for autoremoval, so kthresher can be used for testing.
    '''
    
    import re
    import apt
    import sys
    from platform import uname
    
    def autorm_install(pkgs):
        '''Install a list of packages and set them autoremovable.
        '''
        latest_kernel = ''
        ac = apt.Cache()
        for pkg in pkgs:
            latest_kernel = pkg
            k = ac[pkg]
            if not k.is_installed:
                k.mark_install(from_user=False)
        try:
            ac.commit(install_progress=None)
        except apt.cache.LockFailedException as lfe:
            print('{}, are you root?'.format(lfe))
            sys.exit(1)
        except SystemError:
            print('Something failed')
            sys.exit(1)
    
    def get_pkg(regex):
        '''Get a list of packages available that match the regex.
        '''
        pkgs = []
        ac = apt.Cache()
        ac.update()
        for pkg in ac:
            if re.match(regex, pkg.name):
                # ignore running kernel
                if pkg.name == 'linux-image-{0}'.format(uname()[2]):
                    continue
                pkgs.append(pkg.name)
        return pkgs
    
    def main():
        limit = 5
        if len(sys.argv) > 1:
            try:
                limit = int(sys.argv[1])
            except:
                print("Use an integer as the limit of pkgs to install.")
                sys.exit(1)
        print("Installing {} kernels/headers if available...".format(limit))
        kernel_regex = "^linux-image-\d\..*-(generic|amd64)$"
        header_regex = "^linux-headers-\d\..*-(generic|amd64)$"
        kernels = get_pkg(kernel_regex)
        headers = get_pkg(header_regex)
        pkgs = kernels[0:limit] + headers[0:limit]
        print("Installing {} packages total\n\tkernels: {}\n\theaders: {}"
              .format(len(pkgs), kernels[0:limit], headers[0:limit]))
        autorm_install(pkgs)

    if __name__ == "__main__":
        main()



Bugs
----

Submit Bug reports, feature requests via `issues <https://github.com/rackerlabs/kthresher/issues>`__.

Logos
-----

The art was created by `Carlos Garcia <https://hellyeahdesign.com.mx>`__ <hellyeahdesign AT gmail DOT com> and released under CC BY-SA 4.0

+---------+---------+
| |logo0| | |logo1| |
+---------+---------+
| |logo2| | |logo3| |
+---------+---------+

.. image:: https://i.creativecommons.org/l/by-sa/4.0/88x31.png
   :target: http://creativecommons.org/licenses/by-sa/4.0/
   :alt: Creative Commons License

-----

.. |version| image:: https://img.shields.io/pypi/v/kthresher.svg
        :target: https://github.com/rackerlabs/kthresher/releases/latest
        :alt: Latest Version
.. |downloads-pypi| image:: https://img.shields.io/pypi/dm/kthresher.svg
        :target: https://pypi.python.org/pypi/kthresher
        :alt: PyPi Downloads
.. |stars-github| image::	https://img.shields.io/github/stars/rackerlabs/kthresher.svg
        :target: https://github.com/rackerlabs/kthresher
        :alt: Github Stars
.. |versions| image:: https://img.shields.io/pypi/pyversions/kthresher.svg
        :target: https://github.com/rackerlabs/kthresher/releases
        :alt: Versions
.. |license| image:: https://img.shields.io/pypi/l/kthresher.svg
        :target: https://github.com/rackerlabs/kthresher/blob/master/LICENSE
        :alt: License

.. |logo0| image:: https://github.com/rackerlabs/kthresher/wiki/img/kthresher.png      

.. |logo1| image:: https://github.com/rackerlabs/kthresher/wiki/img/kthresher_horiz.png

.. |logo2| image:: https://github.com/rackerlabs/kthresher/wiki/img/kthresher_circ.png

.. |logo3| image:: https://github.com/rackerlabs/kthresher/wiki/img/kthresher_half.png
