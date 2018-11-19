import os
from glob import glob
import fileinput
from collections import defaultdict

filenames = glob('*-x-*')
dd = defaultdict(list)
for filename in filenames:
    name, ext = os.path.splitext(filename)
    dd[tuple(name.split('-x-')[:3])].append(filename)

for key, fnames in dd.iteritems():
    for line in fileinput.FileInput(fnames):
        pass # do something with lines from files with same key