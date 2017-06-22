# coding = utf-8
import re

# https://developers.google.com/edu/python/regular-expressions

info = 'an example word:cat'
# write pattern strings with the 'r'
match = re.search(r'word:\w\w\w', info)
# match Object or None
if match:
    print(match.group())
