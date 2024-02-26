class Node:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def walk(self, path='', code=None):
        if code is None:
            code = {}
        
        if isinstance(self.left, str):
            code[self.left] = path + '0'
        else:
            self.left.walk(path + '0', code)
        
        if isinstance(self.right, str):
            code[self.right] = path + '1'
        else:
            self.right.walk(path + '1', code)

text = 'abcde'
letters = set(text)
frequencies = []

for letter in letters:
    frequencies.append((text.count(letter), letter))

print(frequencies)

while len(frequencies) > 1:
    frequencies = sorted(frequencies, key=lambda x: x[0], reverse=True)
    first = frequencies.pop()
    second = frequencies.pop()
    freq = first[0] + second[0]
    frequencies.append((freq, Node(first[1], second[1])))
    print(frequencies)

huffman_tree = frequencies[0][1]
code = {letter: '' for letter in letters}
huffman_tree.walk(code=code)

print(code)