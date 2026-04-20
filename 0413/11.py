files = input().split()

ext_count = {}

for name in files:
    if "." in name:
        ext = name.split(".")[-1]
        if ext in ext_count:
            ext_count[ext] += 1
        else:
            ext_count[ext] = 1

for ext in sorted(ext_count):
    print(ext, ext_count[ext])
    #123