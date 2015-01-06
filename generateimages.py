#!/usr/bin/env python
from itertools import combinations, chain
import subprocess
import os
import shutil
"""
Generate all the possible combinations of substrates, and create an icon for
that combination.
"""

os.chdir("static/img/kml_icons")

def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

status = ["artificial", "natural", "other", "plankton", "rov", "scuba", "unspecified"]
status.sort()
mussels = ["both", "carb", "dbug", "dpoly", "non", "unknown", "pending"]
for mussel in mussels:
    for s in powerset(status):
        if s == ():
            continue
        filename = "../generated/" + mussel + "_" + "_".join(s) + ".png"
        files = [mussel + "_" + name + ".png" for name in s]
        if len(s) == 1:
            shutil.copyfile(files[0], filename)
        else:
            cmd = ['convert', '-background', 'transparent', '-flatten']
            cmd.extend(files)
            cmd.append(filename)
            print(" ".join(cmd))
            subprocess.call(cmd)


