# Copyright (c) 2014, Menno Smits
# Released subject to the New BSD License
# Please see http://en.wikipedia.org/wiki/BSD_licenses

'''
Unit tests for the response_types classes
'''

from __future__ import unicode_literals

from imapclient.response_types import imapbytes
from imapclient.test.util import unittest
from imapclient import six

class TestImapbytes(unittest.TestCase):

    def test_imapbytes_is_bytes(self):
        somebytes = b"hey !"
        someimapbytes = imapbytes(somebytes)
        assert isinstance(somebytes, bytes)
        assert isinstance(somebytes, six.binary_type)
        assert not isinstance(somebytes, imapbytes)
        assert isinstance(someimapbytes, bytes)
        assert isinstance(someimapbytes, six.binary_type)
        assert somebytes == someimapbytes

    def test_equals(self):
        assert imapbytes(b'we are bytes') == imapbytes(b'we are bytes')
        assert imapbytes(b'we are bytes') != imapbytes(b'we are bytes but diffents')

    def test_decoded(self):
        simplebytes = imapbytes(b'simple encoded bytes')
        assert simplebytes.decoded() == u'simple encoded bytes'

        emailutf8encoded = imapbytes(b"=?utf-8?B?VsOpbMO0VG91bG91c2U=?=")
        assert emailutf8encoded.decoded() == u'VélôToulouse'

    def test_did_we_broke_python_api(self):
        try:
            b'okayyy'.decoded()
        except AttributeError as e:
            # were good, function doesnt exist
            pass
        else:
            # were not, if were failing here, deprecate imapbytes.decoded()
            # make this test pass and choose a new name !
            totest = b'simple encoded bytes'
            assert totest.decoded() == imapbytes(totest).decoded()
            totest = b'=?utf-8?B?VsOpbMO0VG91bG91c2U=?='
            assert totest.decoded() == imapbytes(totest).decoded()
