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


def makeSentence(main_words, scheme_words):
    if scheme_type[0] is '^':
        return f"{main_words}{scheme_words[1:]}"
    else:
        return f"{main_words} {scheme_words}"

def writeSentences(file, cluster, sentences, count):
    if len(selected_sentences) > count:
        sentences = random.sample(sentences, count)

    for sentence in sentences:
        file.write(f"{cluster}\t{sentence}")


def selectSentences(sentences, scheme_words):
    output_sentneces = []
    for sentence in sentences:
        output_sentneces.append(makeSentence(sentence, random.choice(scheme_words)))
    return output_sentneces


if __name__ == '__main__':
#    f = open(sys.argv[1], 'r')
#    g = open(sys.argv[2], 'r')
#    h = open(sys.argv[3], 'w')
#    count = sys.argv[4]

    f = open('/home/lychan/eclipse-workspace/DataGenerator/data/tradeportal-LC-2/portal&LC.csv', 'r')
    g = open('/home/lychan/eclipse-workspace/DataGenerator/data/tradeportal-LC-2/scheme.csv', 'r')
    h = open('/home/lychan/eclipse-workspace/DataGenerator/data/tradeportal-LC-2/portal-LC.txt', 'w')
    count = 30

    f.readline()
    g.readline()

    scheme = defaultdict(list)

    for line in g.readlines():
        k, v = line.split(',')
        scheme[k].append(v)

    cluster = ''
    permuted_words = []
    selected_sentences = []

    while True:
        data = f.readline()
        if data == '':
            writeSentences(h, cluster, selected_sentences, count)
            break

        current_type, current_cluster, current_words = data.strip().split(',', 2)

        if cluster is '':
            cluster = current_cluster

        if current_cluster != cluster:
            writeSentences(h, cluster, selected_sentences, count)
            selected_sentences.clear()
            cluster = current_cluster

        for scheme_type in scheme[current_type]:
            h.write(f"{current_cluster}\t{makeSentence(current_words, scheme_type)}")

        else:
            selected_sentences.extend(selectSentences(exportPermutedSentence(current_words, count), scheme[current_type]))
