#!/usr/bin/env python3

"""
Pandoc filter to change each relative URL to absolute
"""

from panflute import run_filter, Str, Header, Image, Math
import sys
import re

base_raw_url = 'https://raw.githubusercontent.com/illinois-cs241/coursebook/master/'

class NoAltTagException(Exception):
    pass

def change_base_url(elem, doc):
    if type(elem) == Image:
        alt_length = len(elem._content)
        if alt_length == 0:
            raise NoAltTagException(elem.url)
        elem.url = base_raw_url + elem.url
        return elem

    if isinstance(elem, Math):
        elem.text = re.sub(r'_([A-Za-z0-9])\b', r'<sub>\g<1></sub>', elem.text)
        elem.text = re.sub(r'\^([A-Za-z0-9])\b', r'<sup>\g<1></sup>', elem.text)
        return elem


def main(doc=None):
    return run_filter(change_base_url, doc=doc)

if __name__ == "__main__":
    main()
