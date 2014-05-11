PROJECTNAME=encdev
BINFILES=encdev

bindir=/usr/bin

.PHONY: all install clean

all:

install:
	install -d $(DESTDIR)$(bindir)
	install -m 755 $(BINFILES) $(DESTDIR)$(bindir)

clean:

