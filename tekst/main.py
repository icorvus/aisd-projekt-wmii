import json
import sys
import string
import os
from collections import Counter

from parser import args
from kmp import replacePattern
from huffman import HuffmanTree
from nodetree import NodeTree

def main():
    if not os.path.exists("out"):
        os.makedirs("out")

    infile = args.infile
    outfile = args.outfile
    json_outfile = args.json

    if not os.path.exists(args.infile):
        print("Error: specified input file does not exist.")
        return

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

    huffman_code = HuffmanTree(nodes[0][0])

    out = ''.join(f"{huffman_code[char]}" for char in string_fixed)
    out_separated = ' '.join(f"{huffman_code[char]}" for char in string_fixed)

    if args.verbose:
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
        output.write(out)
    print("Zapisano wyjście do pliku \"" + outfile + "\".")
    
    with open(json_outfile, "w") as json_output:
        huffman_sum = dict(huffman_code)
        huffman_sum.update({v: k for k, v in huffman_code.items()})
        json.dump(huffman_sum, json_output, indent = 2)
    print("Zapisano słownik do pliku \"" + json_outfile + "\".")

if __name__ == "__main__":
    main()
