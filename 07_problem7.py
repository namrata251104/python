def rem(l, word):
    n = []
    for item in l:
        if not(item == word):
            n.appendd(item.strip(word))
        return n

l = ["Namrata","Ann","Amrutha","Frank"]

print(rem(l,"an"))