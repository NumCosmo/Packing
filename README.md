Packing
=======

Several packing configurations. Support for rpm, deb and ArchLinux pacman. 

Packages are automatically compiled in [openSUSE Build Service](https://build.opensuse.org/project/show/home:vitenti).

For manual package creation, see below.

Directories:
------------
* `rpm/` Spec file for rpm creation.
* `deb/` Files for debian package creation.
* `arch/` PKGBUILD file for pacman packaging.
* `macosx/` MacPort packaging files.

OpenSUSE
--------

OpenSUSE rpm instructions ...

Debian and Ubuntu
-----------------

Debian and Ubuntu instructions ...

ArchLinux
---------

Arch Linux instructions ...

MacPort
-------

NumCosmo can be installed in a MacOSX using the MacPorts. 
To this end the user must first make a clone of the [NumCosmo/Packing](https://github.com/NumCosmo/Packing) 
repository. The local repository will be in Packing/macosx/ports, this directory must be [added to the
list of local repositories](https://guide.macports.org/#development.local-repositories). 

After added the local repository the command: `port install numcosmo`, will install NumCosmo and all its
dependencies.

[Problems/Suggestions](https://github.com/NumCosmo/NumCosmo/issues).
