import os
import sys
import optparse
#text = """<p><img src="@X@EmbeddedFile.requestUrlStub@X@sessions/1/2/7/2/7/3/2/session/5e375969b2e640fb9d6c1d981e09ffc6/Distance%20sketch%20Figure%204%20for%20DL%2717%20T2.jpg" width="300" height="129" style="border: 0px; cursor: default; margin: 0px; padding: 0px; outline: black solid 1px; font-weight: normal; font-style: normal; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 13px; vertical-align: middle; max-width: 100%; height: auto; color: #000000; font-variant-ligatures: normal; font-variant-caps: normal; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; text-decoration-style: initial; text-decoration-color: initial;"></p>"""
text = "abcd"
try:
    if text.find("a") is -1:
        print "yes"

except Exception as e:
    print "expceiton"