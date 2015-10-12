kthresher
=========

Tool to remove unused kernels that were installed automatically in Debian/Ubuntu

This tool removes those kernel packages marked as candidate for autoremoval. Those packages are generally installed via Unattended upgrade or meta-packages. By default the latest kernel and manual installations are marked to Never Auto Remove.

*thresher - A device that first separates the head of a stalk of grain from the straw, and then further separates the kernel from the rest of the head.*

Supported Operating Systems
---------------------------

* Debian (Tested on Version(s) 8)
* Ubuntu (Tested on Version(s) 14.04, 15.10)

Usage
-----

    $ kthresher
    usage: kthresher [-h] [-l] [-p] [-f] [-v]
    
    Purge Unused Kernels.
    
    optional arguments:
      -h, --help         show this help message and exit
      -l, --list-kernel  List unused kernel packages available to purge.
      -p, --purge        Purge Unused Kernels.
      -f, --force        Proceed without confirmation
      -v, --version

Examples
--------

    Listing the packages available to remove
    ----------------------------------
    # khresher -l
    ## Running kernel: linux-image-3.16.0-45-generic [3.16.0-45.60~14.04.1]
    linux-image-3.16.0-49-generic [3.16.0-49.65~14.04.1]
    linux-image-3.16.0-48-generic [3.16.0-48.64~14.04.1]
    linux-headers-3.16.0-49-generic [3.16.0-49.65~14.04.1]
    linux-headers-3.16.0-48 [3.16.0-48.64~14.04.1]
    linux-headers-3.16.0-49 [3.16.0-49.65~14.04.1]
    linux-headers-3.16.0-48-generic [3.16.0-48.64~14.04.1]
    linux-image-extra-3.16.0-49-generic [3.16.0-49.65~14.04.1]
    linux-image-extra-3.16.0-48-generic [3.16.0-48.64~14.04.1]

Bugs
----

Submit Bug reports, feature requests via [Issues][1]


[1] https://github.com/rackerlabs/kthresher/issues
