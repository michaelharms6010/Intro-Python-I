def leadingZeroRemover(s):
    if s[0] == "0":
        return leadingZeroRemover(s[1:])
    return s

def minutes_to_seconds(time):
    l = time.split(":")
    print(l)
    minutes = int(l[0])

    seconds = int(l[1])
    return minutes * 60 + seconds

print(minutes_to_seconds("01:00"))


