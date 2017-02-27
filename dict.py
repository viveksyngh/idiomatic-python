d = { 'matthew': 'blue', 'rachel': 'green', 'raymond': 'red'}

# Looping over keys
for k in d:
    print k


# Looping over dict while mutating dict
for k in d.keys():
    if k.startswith('r'):
        del d[k]


# Dict comprehension
d = { k : d[k] for k in d if not k.startswith('r') }


# Looping over a dictionay keys and values
for k in d:
    print k, '--->', d[k]

# Better
for key, value in d.items():
    print key, '--->', value

for key, value in d.iteritems():
    print key, '--->', value


# Constructing dictionaries
colors = ['red', 'green', 'blue']
names = ['raymond', 'rachel', 'mathhew']

from itertools import izip
d = dict(izip(names, colors))
print d

d = dict(enumerate(names))
print d


# Counting with dictionaries
colors = ['red', 'green', 'red', 'blue', 'green', 'red']
d = {}
for color in colors:
    if color not in d:
        d[color] = 0
    d[color] += 1
print d

# Pythonic
d = {}
for color in colors:
    d[color] = d.get(color, 0) + 1
print d

from collections import defaultdict
d = defaultdict(int)
for color in colors:
    d[color] += 1
print d


# Grouping with dictonaries
names = ['raymond', 'rachel', 'mathhew', 'roger', 'betty', 'melissa', 'judith', 'charlie',]
d = {}

## Non Pythonic
for name in names:
    key = len(name)
    if key not in d:
        d[key] = []
    d[key].append(name)
print d

## Better
d = {}
for name in names:
    key = len(name)
    d.setdefault(key, []).append(name)
print d

d = defaultdict(list)
for name in names:
    key = len(name)
    d[key].append(name)
print d


# Dictionay pop item
d = { 'matthew': 'blue', 'rachel': 'green', 'raymond': 'red'}

while d:
    key, value = d.popitem() # Thread Safe
    print key, value
