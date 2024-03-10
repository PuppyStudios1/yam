# Target to generate the PKGBUILD
generate-pkgbuild:

    @echo "## PKGBUILD for yam-2.2" > PKGBUILD
    @echo "" >> PKGBUILD
    @echo "pkgname = yam" >> PKGBUILD
    @echo "pkgver = 2.2" >> PKGBUILD
    @echo "pkgrel = 1" >> PKGBUILD
    @echo "pkgdesc = $(shell python3 -m pip show yam.py | grep Summary: | awk '{print $2}')" >> PKGBUILD
    @echo "arch = (any)" >> PKGBUILD
    @echo "url = https://github.com/PuppyStudios1/yam" >> PKGBUILD
    @echo "license = $(shell python3 -m pip show yam.py | grep License: | awk '{print $2}')" >> PKGBUILD
    @echo "makedepends = python" >> PKGBUILD  # Add additional dependencies here if needed
    @echo "depends = $(shell python3 -m pip show yam.py | grep Requires: | awk '{print $2}')" >> PKGBUILD
    @echo "" >> PKGBUILD
    @echo "source = (yam-2.2.tar.gz)" >> PKGBUILD
    @echo "" >> PKGBUILD
    @echo "build() {" >> PKGBUILD
    @echo "    # No build step needed for a Python script" >> PKGBUILD
    @echo "}" >> PKGBUILD
    @echo "" >> PKGBUILD
    @echo "package() {" >> PKGBUILD
    @echo "    install -m 755 yam.py \$pkgdir/usr/bin/" >> PKGBUILD
    @echo "}" >> PKGBUILD
    @echo "" >> PKGBUILD
    @echo ".PHONY: clean" >> PKGBUILD
    @echo "clean:" >> PKGBUILD
    @echo "    rm -f PKGBUILD" >> PKGBUILD

# Target to create a dummy source archive (optional)
create-source-archive:

    @tar -czvf yam-2.2.tar.gz yam.py  # Include additional files if needed

.PHONY: generate-pkgbuild create-source-archive

all: generate-pkgbuild

