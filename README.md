kthresher
=========

[![](https://img.shields.io/pypi/v/kthresher.svg)](https://pypi.python.org/pypi/kthresher/)
[![](https://img.shields.io/pypi/dm/kthresher.svg)](https://pypi.python.org/pypi/kthresher/)
[![](https://img.shields.io/pypi/pyversions/kthresher.svg)](https://pypi.python.org/pypi/kthresher/)
[![](https://img.shields.io/pypi/l/kthresher.svg)](https://pypi.python.org/pypi/kthresher/)

Tool to remove unused kernels that were installed automatically in Debian/Ubuntu.

This tool removes those kernel packages marked as candidate for autoremoval. Those packages are generally installed via Unattended upgrade or meta-packages. By default the latest kernel and manual installations are marked to Never Auto Remove.

*thresher - A device that first separates the head of a stalk of grain from the straw, and then further separates the kernel from the rest of the head.*


Supported Operating Systems
---------------------------

* Debian (Tested on Version(s))
  * [8](https://www.debian.org/releases/jessie/)
* Ubuntu (Tested on Version(s))
  * [14.04](http://releases.ubuntu.com/trusty/)
  * [15.10](http://releases.ubuntu.com/trusty/)
  * [16.04(development branch/Beta 2)](http://releases.ubuntu.com/xenial/)


Installation
-----
### script

    wget -O kthresher https://raw.githubusercontent.com/rackerlabs/kthresher/master/kthresher/kthresher.py
    chmod u+x kthresher


### pip

    pip install kthresher

or

    pip install git+https://github.com/rackerlabs/kthresher.git

### Github

    git clone https://https://github.com/rackerlabs/kthresher.git
    python kthresher/setup.py install


Usage
-----

    $ kthresher -h
    usage: kthresher [-h] [-d] [-n [N]] [-p] [-s] [-v] [-V]
    
    Purge Unused Kernels.
    
    optional arguments:
      -h, --help            show this help message and exit
      -d, --dry-run         List unused kernel images available to purge(dry run)
      -n [N], --number [N]  Number of kernels to keep, default 1.
      -p, --purge           Purge Unused Kernels.
      -s, --show-autoremoval
                            Show kernel packages available for autoremoval.
      -v, --verbose         Be verbose.
      -V, --version         Print version.


Examples
--------

    List which kernel images and its dependencies would remove(dry run)
    --------------------------------------------------------------------
    # kthresher -d
    INFO: ----- DRY RUN -----
    INFO: Running kernel is linux-image-3.13.0-83-generic v[3.13.0-83.127]
    INFO: Attempting to keep 1 kernel package(s)
    INFO: Found 6 kernel image(s) installed and available for autoremoval
    INFO: Pre-sorting: ['3.16.0-60.80~14.04.1', '3.13.0-63.103', '3.13.0-79.123', '3.16.0-33.44~14.04.1', '3.13.0-77.121', '3.13.0-24.47']
    INFO: Post-sorting: ['3.13.0-24.47', '3.13.0-63.103', '3.13.0-77.121', '3.13.0-79.123', '3.16.0-33.44~14.04.1', '3.16.0-60.80~14.04.1']
    INFO:   Purging packages from version: 3.13.0-24.47
    INFO:           Purging: linux-image-3.13.0-24-generic
    INFO:   Purging packages from version: 3.13.0-63.103
    INFO:           Purging: linux-image-extra-3.13.0-63-generic
    INFO:           Purging: linux-image-3.13.0-63-generic
    INFO:   Purging packages from version: 3.13.0-77.121
    INFO:           Purging: linux-image-3.13.0-77-generic
    INFO:           Purging: linux-image-extra-3.13.0-77-generic
    INFO:   Purging packages from version: 3.13.0-79.123
    INFO:           Purging: linux-image-3.13.0-79-generic
    INFO:           Purging: linux-image-extra-3.13.0-79-generic
    INFO:   Purging packages from version: 3.16.0-33.44~14.04.1
    INFO:           Purging: linux-image-3.16.0-33-generic

    Show all kernel packages available for autoremoval
    --------------------------------------------------
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
              3.13.0-24.47 linux-image-3.13.0-24-generic
             3.13.0-63.103 linux-image-3.13.0-63-generic
             3.13.0-77.121 linux-image-3.13.0-77-generic
             3.13.0-79.123 linux-image-3.13.0-79-generic
      3.16.0-33.44~14.04.1 linux-image-3.16.0-33-generic
      3.16.0-60.80~14.04.1 linux-image-3.16.0-60-generic
             3.13.0-63.103 linux-image-extra-3.13.0-63-generic
             3.13.0-77.121 linux-image-extra-3.13.0-77-generic
             3.13.0-79.123 linux-image-extra-3.13.0-79-generic
              3.13.0.83.89 linux-image-generic

    Purge Unused Kernels, keep 4 kernels and be verbose
    ---------------------------------------------------
    # ./kthresher.py -p -n4 -v
    INFO: Running kernel is linux-image-3.13.0-83-generic v[3.13.0-83.127]
    INFO: Attempting to keep 4 kernel package(s)
    INFO: Found 5 kernel image(s) installed and available for autoremoval
    INFO: Pre-sorting: ['3.16.0-60.80~14.04.1', '3.13.0-79.123', '3.16.0-33.44~14.04.1', '3.13.0-63.103', '3.13.0-77.121']
    INFO: Post-sorting: ['3.13.0-63.103', '3.13.0-77.121', '3.13.0-79.123', '3.16.0-33.44~14.04.1', '3.16.0-60.80~14.04.1']
    INFO:   Purging packages from version: 3.13.0-63.103
    INFO:           Purging: linux-image-extra-3.13.0-63-generic
    INFO:           Purging: linux-image-3.13.0-63-generic
    Fetched 0 B in 0s (0 B/s)
    (Reading database ... 174333 files and directories currently installed.)
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
    Found linux image: /boot/vmlinuz-3.13.0-79-generic
    Found initrd image: /boot/initrd.img-3.13.0-79-generic
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
    Found linux image: /boot/vmlinuz-3.13.0-79-generic
    Found initrd image: /boot/initrd.img-3.13.0-79-generic
    Found linux image: /boot/vmlinuz-3.13.0-77-generic
    Found initrd image: /boot/initrd.img-3.13.0-77-generic
    done
    Purging configuration files for linux-image-3.13.0-63-generic (3.13.0-63.103) ...
    Examining /etc/kernel/postrm.d .
    run-parts: executing /etc/kernel/postrm.d/initramfs-tools 3.13.0-63-generic /boot/vmlinuz-3.13.0-63-generic
    run-parts: executing /etc/kernel/postrm.d/zz-update-grub 3.13.0-63-generic /boot/vmlinuz-3.13.0-63-generic


Known Issues
------------
Python3 support is currently broken due to a known disutils.LooseVersion [issue][2].


Bugs
----

Submit Bug reports, feature requests via [issues][1].


[1]: https://github.com/rackerlabs/kthresher/issues
[2]: https://bugs.python.org/issue14894
