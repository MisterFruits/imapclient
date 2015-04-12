Continuing to use your lib, noticed strange behaviour of the ```Address.__str__``` method. Just testing it the way it is used in other tests breaks.
The first one fail on python 3.4 while the second is OK. Python 2.7 wont fail at all.

```python
def test_str_fail_python3(self):
    # populated in the same way as in test_response_parser
    address = Address(b"name", None, b"address1", b"domain1.com")
    assert u'name <address1@domain1.com>' == str(address)

def test_str_ok_python3(self):
    # populated in the same way as in unicode
    address = Address(u"name", None, u"address1", u"domain1.com")
    assert u'name <address1@domain1.com>' == str(address)
```

The first one fail because python 3.4 doesn't allow concatenation with bytes and unicode.

Here's the ```__str__``` method:

```python
def __str__(self):
    return formataddr((self.name, self.mailbox + '@' + self.host))
```

