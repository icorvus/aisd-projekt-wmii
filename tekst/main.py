import json
import sys

filename = sys.argv[1]

def swap_words(text):
    # to nie dziala, trzeba poprawic
    swap_candidates = {"poli": "boli", "\n": " "}

    # zamiana wystapien ze slownika
    for cos, costam in swap_candidates.items():
        text_fixed = text.replace(cos, costam)
    return text_fixed

with open(filename) as f:
    string = f.read().strip()
    string_fixed = swap_words(string)

class NodeTree(object):

    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return (self.left, self.right)

    def nodes(self):
        return (self.left, self.right)

    def __str__(self):
        return '%s_%s' % (self.left, self.right)

def huffman_tree(node, left=True, binString=''):
    if type(node) is str:
        return {node: binString}
    (l, r) = node.children()
    d = dict()
    d.update(huffman_tree(l, True, binString + '0'))
    d.update(huffman_tree(r, False, binString + '1'))
    return d

freq = {}
for c in string_fixed:
    if c in freq:
        freq[c] += 1
    else:
        freq[c] = 1

freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

nodes = freq

while len(nodes) > 1:
    (key1, c1) = nodes[-1]
    (key2, c2) = nodes[-2]
    nodes = nodes[:-2]
    node = NodeTree(key1, key2)
    nodes.append((node, c1 + c2))
    nodes = sorted(nodes, key=lambda x: x[1], reverse=True)

huffman_code = huffman_tree(nodes[0][0])

print("Na podstawie pliku \"" + filename + "\" (" + str(len(string_fixed)) + " znaków):")
print(' Znak | Odpowiednik w sensie Huffmana ')
print('-' * 38)
for (char, frequency) in freq:
    print(' %-4r |%20s' % (char, huffman_code[char]))

print()
out = ''.join(f"{huffman_code[char]}" for char in string_fixed)
print()
print(out)
print()
out_separated = ' '.join(f"{huffman_code[char]}" for char in string_fixed)
print(out_separated)
print()

print("Koszta zapisu:")
print('pięciobitowego | kodem zmiennej dł.')
print('-' * 35)
print('%-14r | %9s' % (len(string_fixed) * 5, len(out)))

with open("output.txt", "w") as out:
    out.write(out_separated)

with open("huffman.json", "w") as json_out:
    json.dump(huffman_code, json_out, indent = 2)
