from string import ascii_uppercase

def make_diamond(letter):
    lines = []
    length = ascii_uppercase.index(letter) + 1
    for l in range(length):
        spaces = [' '] * length
        spaces[l] = ascii_uppercase[l]
        lines.append(''.join(list(reversed(spaces)) + spaces[1:]))
    return '\n'.join(lines[:-1] + list(reversed(lines))) + '\n'

print(make_diamond('S'))