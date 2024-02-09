outer = 5


def total():
    inner = 4
    global outer
    outer = 7
    return inner + outer


inner = total()
print("Inner: ", inner)
print("Outer: ", outer)
