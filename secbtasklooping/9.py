items = ["red", "blue", "green", "red", "yellow"]
emptylist = []
for item in items:
    if item in emptylist:
        print("Duplicate item found:", item)
    else:
        emptylist.append(item)