import re

# practice the regex
sample_1 = 'ApplebannaTree[te]ctree'

# form: re.search(pattern, string, flags)
res = re.search("t[t,r]ee", sample_1, re.I)
print(res)
if res:
    print(res.group())

sample_2 = '----------abc123---------'
res = re.sub("[a-z0-9]", "|", sample_2)
print(res)
res = re.sub("[^a-z0-9]", "*", res)
print(res)
