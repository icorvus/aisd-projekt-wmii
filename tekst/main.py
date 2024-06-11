import sys

filename = sys.argv[1]

def swap_words(text):
    # co nalezy zmienic na co
    # jesli bedzie potrzeba zmienic cos jeszcze, dodajemy to tutaj
<<<<<<< HEAD
    
    swap_candidates = {"poli": "boli"}
=======
    swap_candidates = {
        "poli" : "boli"
    }

    text.translate(swap_candidates)

    # zamiana wystapien ze slownika
>>>>>>> 661e4120db46d524502c3bf37b0bab0791969caa
    for cos, costam in swap_candidates.items():
        text_fixed = text.replace(cos, costam)
    text_fixed = text_fixed.replace("\n", " ")
    return text_fixed

<<<<<<< HEAD
with open(filename) as f:
    print("Na podstawie pliku \"" + filename + "\":")
    string = f.read().strip()
    string_fixed = swap_words(string)
=======
with open("2.txt", "r") as file:
    text = file.read()
    text = swap_words(text.replace('\n', ' '))

    print(text)
>>>>>>> 661e4120db46d524502c3bf37b0bab0791969caa

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

for char in string_fixed:
    print(char + " ---> " + huffman_code[char])
