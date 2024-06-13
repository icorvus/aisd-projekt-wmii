def HuffmanTree(node, left=True, binString=''):
    if type(node) is str:
        return {node: binString}
    (l, r) = node.children()
    d = dict()
    d.update(HuffmanTree(l, True, binString + '0'))
    d.update(HuffmanTree(r, False, binString + '1'))
    return d
