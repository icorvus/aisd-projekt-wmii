import argparse


parser = argparse.ArgumentParser(
        prog = "Problem 2.",
        description = "Rozwiązanie problemu 2. w języku Python"
        )

verbose = False

parser.add_argument('-i', '--infile', help="file to read from").default = "in/infile.txt"
parser.add_argument('-o', '--outfile', help="file to write to").default = "out/outfile.txt"
parser.add_argument('-j', '--json', help="file to write the mappings to").default = "out/mappings.json"
parser.add_argument('-v', '--verbose', help="increase output verbosity", action="store_true")

args = parser.parse_args()
if args.verbose:
    verbose = True
