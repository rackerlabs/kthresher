kthresher
=========

Tool to remove unused kernels that were installed automatically in Debian/Ubuntu.

This tool removes those kernel packages marked as candidate for autoremoval. Those packages are generally installed via Unattended upgrade or meta-packages. By default the latest kernel and manual installations are marked to Never Auto Remove.

*thresher - A device that first separates the head of a stalk of grain from the straw, and then further separates the kernel from the rest of the head.*


-----

|version| |downloads| |versions| |license|

-----

.. contents:: Table of Contents
        :local:
        :depth: 1
        :backlinks: none

-----

Supported Operating Systems
---------------------------

* Debian (Tested on Version(s))
    * `8 <https://www.debian.org/releases/jessie/>`__
* Ubuntu (Tested on Version(s))
    * `12.04 <http://releases.ubuntu.com/precise/>`__
    * `14.04 <http://releases.ubuntu.com/trusty/>`__
    * `15.10 <http://releases.ubuntu.com/wily/>`__
    * `16.04(development branch/Beta 2) <http://releases.ubuntu.com/xenial/>`__


Installation
------------
script
~~~~~~

.. code-block:: bash

    wget -O kthresher https://raw.githubusercontent.com/rackerlabs/kthresher/master/kthresher/kthresher.py
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

    git clone https://https://github.com/rackerlabs/kthresher.git
    python kthresher/setup.py install


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

    # kthresher -p -k3 v
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


Known Issues
------------
Python3 support is currently broken due to a known disutils.LooseVersion `issue <https://bugs.python.org/issue14894>`__.


Bugs
----

Submit Bug reports, feature requests via `issues <https://github.com/rackerlabs/kthresher/issues>`__.


-----

.. |version| image:: https://img.shields.io/pypi/v/kthresher.svg
        :target: https://pypi.python.org/pypi/kthresher/
        :alt: Latest Version
.. |downloads| image:: https://img.shields.io/pypi/dm/kthresher.svg
        :target: https://pypi.python.org/pypi/kthresher
        :alt: Downloads
.. |versions| image:: https://img.shields.io/pypi/pyversions/kthresher.svg
        :target: https://pypi.python.org/pypi/kthresher/
        :alt: Versions
.. |license| image:: https://img.shields.io/pypi/l/kthresher.svg
        :target: https://pypi.python.org/pypi/kthresher/
        :alt: License

