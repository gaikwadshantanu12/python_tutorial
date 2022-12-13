# WAP to try following
"""
If input string is 'aaaabbbcc' then output should be a4b3c2
"""

import collections as clt
s = "aaaabbbcc"
d = dict(clt.Counter(s))
s = ""
for k,v in d.items():
    s = s + k + str(v)

print(s)
