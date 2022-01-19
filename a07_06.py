def dreh(lst):
    "Reverses a list and returns the resulting list"
    if len(lst) == 0:
        return []
    return [lst[-1]] + dreh(lst[:-1])

print(dreh(['B', 'a', 'e', 'r', 'e', 'n', 's', 'p', 'a', 's', 's']))