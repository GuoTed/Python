import re

# practice the regex
sample_1 = 'ApplebannaTree[te]ctree'

# search if has the decribed pattern
res = re.search("t[t,r]ee", sample_1, re.I)
if res:
    print(res.group()) # Tree

# search all decribed pattern
res = re.findall("t[t,r]ee", sample_1, re.I)
print(res) # ['Tree', 'tree']

sample_2 = '----------abc123---------'
res = re.sub("[a-z0-9]", "|", sample_2)
print(res) # ----------||||||---------
res = re.sub("[^a-z0-9]", "*", res)
print(res) # *************************
