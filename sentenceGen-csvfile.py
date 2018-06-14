# -*- coding: utf-8 -*-

import sys
from collections import defaultdict
import itertools
import random
import math

def exportPermutedSentence(words, count):
    selected_permuted_words = []
    max_count = math.factorial(len(words.strip().split(' ')))

    if max_count >= count:
        for permuted in itertools.permutations(words.split(' ')):
            if random.randint(1, max_count) <= count:
                selected_permuted_words.append(' '.join(permuted))
    else:
        for i in range(int(count/max_count)):
            for permuted in itertools.permutations(words.split(' ')):
                selected_permuted_words.append(' '.join(permuted))
        if count % max_count:
            selected_permuted_words.append(
                random.sample(selected_permuted_words, count % max_count))

    return selected_permuted_words


if __name__ == '__main__':
#    f = open(sys.argv[1], 'r')
#    g = open(sys.argv[2], 'r')
#    h = open(sys.argv[3], 'w')
#    count = sys.argv[4]

    f = open('/home/lychan/eclipse-workspace/DataGenerator/data/tradeportal-LC-2/portal&LC.csv', 'r')
    g = open('/home/lychan/eclipse-workspace/DataGenerator/data/tradeportal-LC-2/scheme.csv', 'r')
    h = open('/home/lychan/eclipse-workspace/DataGenerator/data/tradeportal-LC-2/portal-LC.txt', 'w')
    count = 100

    f.readline()
    g.readline()

    scheme = defaultdict(list)

    for line in g.readlines():
        k, v = line.split(',')
        scheme[k].append(v)

    permuted_words = []

    while True:
        data = f.readline()
        if data == '':
            break

        current_type, current_cluster, current_words = data.strip().split(',', 2)

        permuted_words = exportPermutedSentence(current_words, count)
        permuted_words.append(current_words)

        for sentence in permuted_words:
            scheme_type = random.choice(scheme[current_type])
            if scheme_type[0] is '^':
                h.write(f"{current_cluster}\t{sentence}{random.choice(scheme[current_type])[1:]}")
            else:
                h.write(f"{current_cluster}\t{sentence} {random.choice(scheme[current_type])}")
