# -*- coding: utf-8 -*-

import sys
import itertools

if __name__ == '__main__':
    for sentence in itertools.permutations(sys.argv[1:-2]):
        print(' '.join(sentence))

