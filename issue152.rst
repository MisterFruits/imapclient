Hello

I've been playing with imap and python, and use IMAPClient for little project. I'm trying to get out of encoding problems in Enveloppe structure. I wish I could have an easier way to access decoded string, here's what i have in mind.

```python
output = parse_fetch_response([envelope_str])

subject = output[76920][b'ENVELOPE'].subject
assert subject == b'=?utf-8?B?VsOpbMO0VG91bG91c2U=?='
assert subject.decoded() == u'VélôToulouse'
```

One possible way to do that would be by subclassing the `bytes` type:

```python
class imapbytes(bytes):
    def decoded(self, imap_encoding='us-ascii'):
        pass
```

with the following specifications so the current api is not broken:

```python
somebytes = b"hey !"
someimapbytes = imapbytes(somebytes)
assert isinstance(somebytes, bytes)
assert not isinstance(somebytes, imapbytes)
assert isinstance(someimapbytes, bytes)
assert somebytes == someimapbytes
```

I forked your repo so i can test a bit further the idea. I'm not used to Mercurial so I couldn't push my changes on bitbuket but I managed to push them on github on the [decode_imap_bytes branch](https://github.com/maxiimou/imapclient/tree/decode_imap_bytes). It seems to work the expected way on both python 2.7 and 3.4.

Could you tell me what you think of this improvement ? I wish I could contribute here =)
