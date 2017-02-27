# Looping over a range of numbers

for i in [0, 1, 2, 3, 4, 5]:
    print i**2

for i in range(6):
    print i**2


## Pythonic 
for i in xrange(6):
    print i**2


# Looping over a collection 
colors = ['red', 'green', 'blue', 'yellow']

for i in range(len(colors)):
    print colors[i]

# Pythonic
for color in colors:
    print color


# Looping backwards

colors = ['red', 'green', 'blue', 'yellow']

for i in range(len(colors) - 1, -1, -1):
    print colors[i]

# Pythonic 
for color in reversed(colors):
    print color


# Looping over a collection and indices
colors = ['red', 'green', 'blue', 'yellow']

for i in range(len(colors)):
    print i, '-->', colors[i]

## Pythonic
for i, color in enumerate(colors):
    print i, '-->', color


# Looping over two collections
names = ['raymond', 'rachel', 'matthew']
colors = ['red', 'green', 'blue', 'yellow']

n = min(len(colors), len(names))
for i in range(n):
    print names[i], '-->', colors[i]

## Pythonic
for name, color in zip(names, colors):
    print name, '-->', color

from itertools import izip
for name, color in izip(names, colors):
    print name, '-->', color


# Looping in sorted order
colors = ['red', 'green', 'blue', 'yellow']

for color in sorted(colors):
    print color

for color in sorted(colors, reverse=True):
    print color


# Custom sort order
colors = ['red', 'green', 'blue', 'yellow']

def compare(c1, c2):
    if len(c1) < len(c2): return -1
    if len(c1) > len(c2): return 1
    return 0

print sorted(colors, cmp=compare) 
# Function compare is called O(nlogn) times

## Pythonic 
print sorted(colors, key=len)   
# Faster than previous one, function is called only number of items times


# Call a function until a sentinel value

blocks = []
while True:
    block = f.read(32)
    if block == '':
        break
    blocks.append(block)

## Pythonic
blocks = []
for block in iter(partial(f.read, 32), ''):
    blocks.append(block)


# Distinguishing multiple exit points in loops

def find(seq, target):
    found = False
    for i, value in enumerate(seq):
        if value == target:
            found = True
            break
    if not found:
        return -1
    return i


## Pythonic
def find(seq, target):
    for i, value in enumerate(seq):
        if value == target:
            break
    else:
        return -1
    return i

