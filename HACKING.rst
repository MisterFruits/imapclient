This file contains information for those wishing to modify IMAPClient
and contribute back to the project.

Source Code
-----------
The official source code repository for IMAPClient can be found on
bitbucket at: https://bitbucket.org/mjs0/imapclient/

Any major feature branches will also be found on bitbucket as forks of
this repository.

Branches
--------
[Note that the branching scheme discussed here started to be used as
of the 0.9.2 release of IMAPClient]

The project uses two named branches: default and stable. New feature
development will always happen on the default branch.

The stable branch will always reflect the last released version. Small
bug fixes to the stable release will occur on this branch and should be
merged back in the the default branch.

Releases will always be created from the stable branch. Before a major
release changes will be merged from the default branch to the stable
branch.

This branching approach is used by various projects including the
Mercurial project. See this blog article for more information:
http://stevelosh.com/blog/2010/05/mercurial-workflows-stable-default/

Release Tags
------------
Each released version is available in the IMAPClient repository
as a Mercurial tag (e.g. "0.9.1"). Release tags will always be created
on the stable branch (as described above).

Unit Tests
----------
There are comprehensive unit tests for the server response parser and
a number of other parts of the code. These tests use the unittest2
package which is also included as the standard unittest package in
Python 2.7 and 3.2.

To run the tests run::

     python setup.py test

from the root of the package source. This will install any
dependencies required by the tests if they aren't already installed.

Where unittest2 is included in the standard library (eg. Python 2.7
and 3.2) you can also run all unit tests like this (from the root
directory of the IMAPClient source)::

     python -m unittest discover

Alternatively, if unittest2 is installed separately use the unit2
script (for Unix-like systems) or the unit2.py script::

     unit2 discover
     unit2.py discover


"Live" Tests
------------
This script runs a series of functional tests which exercise
IMAPClient against a live IMAP account. It is useful for ensuring
compatibility with a given IMAP server implementation. livetest.py
must be used with an account with write access.

WARNING: As of version 0.9, livetest limits it's activity to a folder
it creates and subfolders of that folder. It *should* be safe to use
with any IMAP account. That said, some of the operations used by
livetest are destructive and could cause unintended loss of non-test
data. Please don't run the live test against a truly important IMAP
account.

Run livetest.py with the --help option to see usage.

Please send the output of livetest.py to the mailing list if it fails
to run successfully against a particular IMAP server. Reports of
successful runs are also welcome.  Please include the type and version
of the IMAP server, if known.

The livetest functionality can also be accessed like this::

    python -m imapclient.livetest ...

Contributing To The Project
---------------------------
The best way to contribute changes to IMAPClient is to fork the
official repository on bitbucket, make changes to your personal fork
and then submit a pull request.

Discussion on the mailing list before undertaking development is
highly encouraged for potentially major changes.

Although not essential, it will make the project maintainer a much
happier person if change submissions include appropriate updates to
unit tests and the live tests. Please ask if you're unsure how of how
the tests work.