# -*- coding: utf-8 -*-
# Copyright (c) 2014, Menno Smits
# Released subject to the New BSD License
# Please see http://en.wikipedia.org/wiki/BSD_licenses

'''
Unit tests for the response_types classes
'''

from __future__ import unicode_literals

from imapclient.response_types import Address
from imapclient.test.util import unittest
from email.utils import formataddr

class TestAddess(unittest.TestCase):

    def test_str_output(self):
        address = Address(b"name", None, b"address1", b"domain1.com")
        assert isinstance(address.__str__(), str)

    def test_str_fail_python3(self):
        # populated in the same way as in test_response_parser
        address = Address(b"name", None, b"address1", b"domain1.com")
        assert u'name <address1@domain1.com>' == address.__str__()

    def test_str_ok_python3(self):
        # populated in the same way as in test_response_parser
        address = Address(u"name", None, u"address1", u"domain1.com")
        assert u'name <address1@domain1.com>' == address.__str__()

    def test_email_util_formataddr(self):
        bbytes = b'some byte'
        assert bbytes == formataddr((None, bbytes))
