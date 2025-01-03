line = 1

with open("log.txt") as f:
    lines = f.readline()

lineno = 1
for line in lines:
    if("python" in line ):
        print("Yes python is present. Line no: {lineno}")
        break
        lineno += 1
else:
    print("No python is not present")