# Change Log
All notable changes to this project will be documented in this file.

## [Unreleased]

## [1.3.0] - 2018-01-30
### Added
- Bash completion

### Changed
- Support to most/all kernel/header packages [flavors used in Ubuntu](https://people.canonical.com/~kernel/info/kernel-version-pockets.txt)
- Using logging consistently.
- PEP8 compliant.

## [1.2.7] - 2017-03-09
### Added
- Better error handling when executing as non-root.
- Logos.

### Changed
- Regex to include linux-headers ending in -common.
- Improved the testing example on the README.

## [1.2.6] - 2017-01-30
### Added
- Support to amd64 kernels.

### Changed
- Consistency between `--show` and `--purge`.
- Sytle improvements(pep8).
- Man page update.

## [1.2.5] - 2016-11-15
### Added
- Support for nested config files through `include` setting.
- README info about how a package is marked for autoremoval.
- README info to be able to perform tests by installing kernels and headers.

### Changed
- Default config file to only include a `include` path for `/etc/kthresher.d/*.conf`

### Removed
- Debian dir and drone configs, will not live now with the code, @thebwt will maintain that now.
- Config file support for dry-run, this is now only available through command line arguments.

## [1.2.4] - 2016-09-02
### Added
- Drone config.

### Changed
- Debian configs for proper building.

### Fixed
- Typos on man page.

## [1.2.3] - 2016-07-25
### Added
- Man page.
- Changelog.
- Debian directory for .debs.

### Changed
- Flatten directory structure for .deb.
- Cron file to check if script is available prior execution.

## [1.2.2] - 2016-04-19
### Added
- Cron file cron.daily.

## [1.2.1] - 2016-04-18
### Added
- Support for old virtual kernel packages.

### Fixed
- Bug when searching for a list of installed kernel images.

## [1.2.0] - 2016-04-18
### Added
- Support to remove headers '-h'.

## [1.1.0] - 2016-04-14
### Added
- Support for config file '-c'.

### Change
- Use of '-n' or '--number' changed to '-k' or '--keep' for number of kernels to keep.

## [1.0.1] - 2016-04-11
### Added
- LICENSE.

### Change
- README to rst.

## [1.0.0] - 2016-04-06
### Added
- Support to keep a fixed amount of kernels '-n'.
- Support to '--dry-run'.

### Changed
- Previously '-v' was used for version, it was changed to '-V'.
- Use of '-v' or '--verbose' was changed to add verbosity.
- Option '-l' or '--list'  was changed to '-s' or '--show-autoremoval'.
- The use of disutils.LooseVersion broke support for Python3.

### Deprecated
- Use of '-l','-f'.

### Fixed
- Typos.

## [0.2.3] - 2015-12-14
### Fixed
- README.

## [0.2.2] - 2015-11-09
### Added
- Licencing.

### Fixed
- README.

## [0.2.1] - 2015-10-12
### Added
- Released kthresher.

---

# Contributors
- [delag](https://github.com/delag)
- [disengage00](https://github.com/disengage00)
- [jamrok](https://github.com/jamrok)
- [Jose R. Gonzalez](https://github.com/Komish)
- [Tony G.](https://github.com/tonyskapunk)
