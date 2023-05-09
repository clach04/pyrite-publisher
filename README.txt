Pyrite Publisher (formerly Doc Toolkit)
Version 2.1.1
Content Creation Tools for Palm Computing Platform Users

Copyright 1998-2002 Rob Tillotson <rob@pyrite.org>
All Rights Reserved

Permission to use, copy, modify, and distribute this software and
its documentation for any purpose and without fee or royalty is
hereby granted, provided that the above copyright notice appear in
all copies and that both the copyright notice and this permission
notice appear in supporting documentation or portions thereof,
including modifications, that you you make.

THE AUTHOR ROB TILLOTSON DISCLAIMS ALL WARRANTIES WITH REGARD TO
THIS SOFTWARE, INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY
AND FITNESS.  IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
SPECIAL, INDIRECT OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER
RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF
CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN
CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE!

* What Is Pyrite Publisher?

Pyrite Publisher is a data converter for Palm Computing Platform
users.  At the moment it is focused on producing e-books for use with
standard document readers.  It has the following features, and maybe
more:

  - converts text and HTML documents to the standard Doc format or the
    new high-compression zTXT format
  - gathers input from local files or from http/ftp URLs
  - produces rich text markup for RichReader or TealDoc
  - detects and reflows paragraphs in text files
  - automatically bookmarks HTML headers and named anchors
  - automatically bookmarks regular expressions in text files
  - supports zTXT annotations and both compression modes
  - annotates and/or footnotes HTML link targets
  - converts between Doc and zTXT while preserving bookmarks
  - converts Doc or zTXT back to text
  - processes Doc or zTXT content as if it is a regular text file
  - most behavior is configurable
  - architecture is extensible to allow addition of more kinds of
    document markup, more input formats, and even handling entirely
    new types of data
    

* Requirements

Pyrite Publisher requires Python 2.1 or above.

A C compiler is optional; Pyrite Publisher contains an extension
module to do Doc compression, but it will use a slower pure-Python
compressor if the compiled module isn't available.  (The speed
difference is obvious, but on reasonably modern hardware the Python
version is usually fast enough.)

Linux users should note that in many cases the Python module building
libraries are in a package called "python-dev"; if you are having
problems building the Doc compression module, make sure it is
installed.

Pyrite Publisher has not been tested on any non-Unix platforms, but it
will probably work wherever there is a full Python installation.

* Installation

Pyrite Publisher uses the standard Python Distutils.  To install it,
you simply need to unpack the Doc Toolkit archive, find the "setup.py"
file, and type:

    python setup.py install

at the command line.

For more installation options, please see the "Installing Python
Modules" document in the Python distribution, or on www.python.org.


* Usage

A users manual and manpage can be found in the "doc" directory of the
package.  A HTML version of the manual is in doc/pyrite-publisher; the
LaTeX source is in doc/pyrite-publisher.tex.

The users manual is also provided in several different variations of
the Doc format:

    doc/pyrite-publisher.pdb       -- Plain text
    doc/pyrite-publisher-ztxt.pdb  -- zTXT
    doc/pyrite-publisher-rich.pdb  -- RichReader-enhanced
    doc/pyrite-publisher-teal.pdb  -- TealDoc-enhanced

Note that all of these have the same database title, so you can only
have one of them installed at a time.  All of these were converted
using Pyrite Publisher, of course.


* Usage Examples:

These are examples of some of the ways you can use Pyrite Publisher:

Convert a local text file to a Doc with some auto-created bookmarks:
  $ pyrpub -r '^CHAPTER [IVX]+' foo.txt
Convert a local HTML file to a Doc:
  $ pyrpub foo.html
Convert a remote HTML webpage to a Doc:
  $ pyrpub http://somedomain.com/foo.html
Convert a remote HTML webpage to a RichReader document:
  $ pyrpub -P RichReader http://somedomain.com/foo.html
Convert a remote HTML webpage to a zTXT:
  $ pyrpub -P zTXT http://somedomain.com/foo.html
Read a Doc or zTXT:
  $ pyrpub -P CopyDoc,TextOutput foo.pdb | less
Convert a Doc or zTXT to a text file:
  $ pyrpub -P CopyDoc,TextOutput -o foo.txt foo.pdb
Convert a Doc to a zTXT, preserving title and bookmarks:
  $ pyrpub -P CopyDoc,zTXT -o zfoo.pdb foo.pdb
Reflow and auto-bookmark an existing Doc:
  $ pyrpub -r '^CHAPTER [IVX]+' -o newfoo.pdb foo.pdb
Convert an Iambic or Mobipocket Doc to a plain Doc:
  $ pyrpub -P HTML -o newfoo.pdb foo.pdb
Convert an Iambic or Mobipocket Doc to a RichReader Doc:
  $ pyrpub -P HTML,RichReader -o newfoo.pdb foo.pdb

... and so forth.




Local Variables:
mode: outline
End:
