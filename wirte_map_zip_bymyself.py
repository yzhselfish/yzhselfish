"""zip传统做法

def myzip(*seqs):
    seqs = [list(S) for S in seqs]
    res = []
    while all(seqs):
        res.append(tuple(S.pop(0) for S in seqs))
    return res
"""

#每次用pop删除元素+生成器
def myzip(*seqs):
    seqs = [list(S) for S in seqs]
    while all(seqs):
        yield tuple(S.pop(0) for S in seqs)

"""
找到最短的列表用下标
def myzip(*seqs):
    minlen = min(len(S) for S in seqs)
    return [tuple(S[i] for S in seqs) for i in range(minlen)]

下标法加上生成器
def myzip(*seqs):
    minlen = min(len(S) for S in seqs)
    return (tuple(S[i] for S in seqs) for i in range(minlen))

Python2.X map传统做法

def mymappad(*seqs, pad=None):
    seqs = [list(S) for S in seqs]
    res = []
    while any(seqs):
        res.append(tuple((S.pop(0) if S else pad) for S in seqs))
    return res
"""
#每次用pop删除元素+生成器

def mymappad(*seqs, pad=None):
    seqs = [list(S) for S in seqs]
    while any(seqs):
        yield tuple((S.pop(0) if S else pad) for S in seqs)

"""
找到最长的列表然后利用下标
def mymappad(*seqs, pad=None):
    maxlen = max(len(S) for S in seqs)
    return [tuple((S[i] if len(S) > i else pad) for S in seqs) for i in range(maxlen)]

下标法加上生成器
def mymappad(*seqs, pad=None):
    maxlen = max(len(S) for S in seqs)
    return (tuple((S[i] if len(S) > i else pad) for S in seqs) for i in range(maxlen))

map传统做法
def mymap(func, *seqs):
    res = []
    for args in zip(*seqs):
        res.append(func(*args))
    return res

列表推导式
def mymap(func, *seqs):
    return [func(*args) for args in zip(*seqs)]

生成器
def mymap(func, *seqs):
    for args in zip(*seqs):
        yield func(*args)
"""
def mymap(func, *seqs):
    return (func(*args) for args in myzip(*seqs))

print(list(mymap(pow, [1, 2, 3], [1, 2, 3])))
print(list(mymappad((1, 2, 3), "jpad", pad = 85)))