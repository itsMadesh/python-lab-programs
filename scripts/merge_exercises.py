import os
import re
_dir = "./Exercises/"
files = os.listdir(_dir)
c = []

for i in range(1, 51):
    print(i)
    if(i == 48):
        continue
    _file = ""
    for f in files:
        if re.search("^"+str(i)+"\..*", f):
            _file = f
            break
    print(_file)
    with open(_dir+_file) as fd:
        content = fd.read()
        c.append(content)

with open(_dir+"S02031_MADESHWARAN_A.py", "w") as fd:
    fd.write("\n#==============================================================================================================#\n".join(c))
