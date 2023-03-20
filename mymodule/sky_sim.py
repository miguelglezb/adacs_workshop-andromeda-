"""
Determine Andromeda location in ra/dec degrees
"""

import random
from math import cos,pi

# from wikipedia
RA = '00:42:44.3'
# ^- Constant name "ra" doesn't conform to UPPER_CASE naming style (invalid-name)
DEC = '41:16:09'
# ^- Constant name "dec" doesn't conform to UPPER_CASE naming style (invalid-name)

d, m, s = DEC.split(':')
dec = int(d)+int(m)/60+float(s)/3600

h, m, s = RA.split(':')
ra = 15*(int(h)+int(m)/60+float(s)/3600)
ra = ra/cos(dec*pi/180)

NSRC = 1_000_000
# ^- Constant name "nsrc" doesn't conform to UPPER_CASE naming style (invalid-name)

# make 1000 stars within 1 degree of Andromeda
ras = []
decs = []
for i in range(NSRC):
    ras.append(ra + random.uniform(-1,1))
    decs.append(dec + random.uniform(-1,1))


# now write these to a csv file for use by my other program

with open ('catalog.csv','w', encoding="utf-8") as f:

    print("id,ra,dec", file=f)
    for i in range(NSRC):
        print(f"{0:07d}, {1:12f}, {2:12f}", file=f)
