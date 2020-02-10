def randomCssColor(flt):
    l = []
    for i in str(flt).replace(".",""):
        l.append(i)

    val1 = int(l.pop()) * 28
    val2 = int(l.pop()) * 28
    val3 = int(l.pop()) * 28

    return f"rgb({val1}, {val2}, {val3})"

print(randomCssColor(5.444))