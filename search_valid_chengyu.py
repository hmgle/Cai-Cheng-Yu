#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Add description here.
"""

# Copyright © 2013 Qiaoyong Zhong <solary.sh@gmail.com>
# Last modified: Aug 14, 2013

import pickle
import sys

txt_file = 'chengyu.txt'
pickle_file = 'chengyu.pickle'

def serialize_data():
    chengyu = []
    with open(txt_file, 'r') as f:
        for line in f:
            chengyu.append(line.rstrip())

    print('{} words with duplication'.format(len(chengyu)))
    chengyu = set(chengyu) # Remove duplication
    print('{} words without duplication'.format(len(chengyu)))

    with open(pickle_file, 'wb') as f:
        pickle.dump(chengyu, f)

    return chengyu

def load_data():
    try:
        with open(pickle_file, 'rb') as f:
            chengyu = pickle.load(f)
    except:
        print('Serializing data in {0}'.format(pickle_file))
        chengyu = serialize_data()

    return chengyu

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print('Usage: {0} keywords'.format(sys.argv[0]))
        print('Example: {0} 狐虎'.format(sys.argv[0]))
        sys.exit()
    else:
        keywords = '，'
        for v in sys.argv[1:]:
            keywords += v.strip()

    chengyu = load_data()

    for word in chengyu:
        validity = True
        for cha in word:
            if cha not in keywords:
                validity = False
                break

        if validity:
            print(word)
