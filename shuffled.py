import json
from random import shuffle
with open("parsed_psyd.json",encoding='utf-8',mode='r') as f:
    shuf = json.load(f)

shuf2 = shuf[250:]
shuf3 = []
base = []
for i in range(len(shuf2)):
    
    base.append(shuf2[i])
    if(i % 10  == 0):
        shuf3.append(base)
        base = []

shuffle(shuf3)

shuf = shuf[:250]
for s in shuf3:
    shuf += s

with open("shuffled_psyd.json",encoding="utf-8", mode='w') as f:
    f.write(json.dumps(shuf, ensure_ascii=False))
