import json
import sys
import string
import os
from collections import Counter

from parser import args
from huffman import huffmanTree, encode, decode

def main():
    if not os.path.exists("out"):
        os.makedirs("out")

    infile = args.infile
    outfile = args.outfile
    json = args.json

    if not os.path.exists(args.infile):
        print("Error: specified input file does not exist.")
        return

    if args.verbose:
        verbose = True

    action = int(input("Wybierz działanie: "))
    print("1. Zakoduj")
    print("2. Dekoduj")
    print("3. Wyjdź")
    match action:
        case 1:
            encode(infile, verbose, outfile, json)
        case 2:
            decode(infile, json)
        case 3:
            quit()
        case _:
            print("Nie rozpoznano działania")

if __name__ == "__main__":
    main()
