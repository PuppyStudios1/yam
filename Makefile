# Target to generate the PKGBUILD
generate-pkgbuild:

pkgname = yam
pkgver = 2.2
pkgrel = 1

# Get license information from project source (replace with actual command if needed)
license = $(shell grep -i License yam.py | head -n 1 | awk '{print $2}')

# Check for shebang line (adjust build step if needed)
has_shebang = $(shell grep -q '^#!' yam.py; echo $$?)

# Define build step conditionally
build() {
  if [ "$has_shebang" -eq 0 ]; then
    # Install as executable if shebang line exists
    cp -v yam.py src/
    makepkg -sri
  fi
}

# Package installation step
package() {
  install -m 755 yam.py \$pkgdir/usr/bin/
}

# Define clean target
.PHONY: clean
clean:
  rm -f PKGBUILD

all: generate-pkgbuild

# This target is not required for Python scripts installable via pip
# create-source-archive:
#   @tar -czvf yam-2.2.tar.gz yam.py
