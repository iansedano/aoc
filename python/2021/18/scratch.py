import json

import snail

s = snail.S_num(1, 2)

print(list(s))

print(s[0])
print(s[1])

print(json.dumps(s))
