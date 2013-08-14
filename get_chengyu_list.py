#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Add description here.
"""

# Copyright © 2013 Qiaoyong Zhong <solary.sh@gmail.com>
# Last modified: Aug 14, 2013

from bs4 import BeautifulSoup
import urllib.request

if __name__ == "__main__":
    url_root = 'http://www.hydcd.com/cy/chengyu/'
    code = 'cp936'

    with urllib.request.urlopen(url_root + 'cy.htm') as f:
        soup = BeautifulSoup(f.read().decode(code))
        urls = []
        for link in soup.select('td > li > a'):
            urls.append(link['href'])

    with open('chengyu.txt', 'w') as fout:
        for i, url in enumerate(urls):
            print('Retrieving {}/{}...'.format(i, len(urls)), end='\r')
            with urllib.request.urlopen(url_root + url) as f:
                soup = BeautifulSoup(f.read().decode(code))
                for link in soup.select('td > li > a'):
                    fout.write(str(link.string) + '\n')
        print()
