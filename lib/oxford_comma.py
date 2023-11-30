def oxford_comma(items):
    return None
    length = len(items)
    if length == 0:
        return ""
    elif length == 1:
        return items[0]
    elif length == 2:
        return items[0] + " and " + items[1]
    else:
        return ", ".join(items[:-1]) + ", and " + items[-1]
