import json
import sys
import string
import os
from collections import Counter


from nodetree import NodeTree
from kmp import replacePattern

def huffmanTree(node, left=True, binString=''):
    if type(node) is str:
        return {node: binString}
    (l, r) = node.children()
    d = dict()
    d.update(huffmanTree(l, True, binString + '0'))
    d.update(huffmanTree(r, False, binString + '1'))
    return d

def encode(infile, verbose, outfile, json_outfile):

    string = ""
    string_fixed = ""
    with open(infile) as f:
        string = f.read()
        string_fixed = replacePattern(string, 'poli', 'boli')
        string_fixed = replacePattern(string_fixed, '\n', ' ').strip()

    freq = Counter(string_fixed)
    freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    print(freq)
    nodes = freq

    while len(nodes) > 1:
        (key1, c1) = nodes[-1]
        (key2, c2) = nodes[-2]
        nodes = nodes[:-2]
        node = NodeTree(key1, key2)
        nodes.append((node, c1 + c2))
        nodes = sorted(nodes, key=lambda x: x[1], reverse=True)

    huffman_code = huffmanTree(nodes[0][0])

    out = ''.join(f"{huffman_code[char]}" for char in string_fixed)
    out_separated = ' '.join(f"{huffman_code[char]}" for char in string_fixed)

    if verbose:
        print("ANALIZA PLIKU \"" + infile + "\" (" + str(len(string_fixed)) + " ZNAKÓW):")
        print()

        print(' Znak | Odpowiednik w sensie Huffmana ')
        print('-' * 38)
        for (char, frequency) in freq:
            print(' %-4r |%20s' % (char, huffman_code[char]))
        print()

        print("ZAWARTOŚĆ \"" + infile + "\":")
        print(string.strip())
        print()
        print("PLIK Z PODMIENIONĄ MELODIĄ:")
        print(string_fixed)
        print()
        print("PLIK ZAKODOWANY:")
        print(out)
        print()
        print("PLIK ZAKODOWANY (ze spacjami):")
        print(out_separated)
        print()

        print("BITÓW POTRZEBNYCH DO ZAPISU:")
        print('pięciobitowego | kodem zmiennej dł.')
        print('-' * 35)
        print('%-14r | %9s' % (len(string_fixed) * 5, len(out)))

    with open(outfile, "w") as output:
        output.write(out_separated)
    print("Zapisano wyjście do pliku \"" + outfile + "\".")
    
    with open(json_outfile, "w") as json_output:
        huffman_sum = dict(huffman_code)
        huffman_sum.update({v: k for k, v in huffman_code.items()})
        json.dump(huffman_sum, json_output, indent = 2)
    print("Zapisano słownik do pliku \"" + json_outfile + "\".")

def decode(code, json_in):
    d = {}
    out = ""
    with open(json_in, "r") as f:
        d.update(json.load(f))
    print(d)

    with open(code, "r") as f:
        words = f.read().strip().split()
        out_separated = ''.join(f"{d[word]}" for word in words)

    with open("out/out_decoded.txt", "w") as f:
        f.write(out_separated)
        print("Zapisano dekodowany plik do \"out/out_decoded.txt\".")
