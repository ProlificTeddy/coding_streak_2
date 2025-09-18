#prints middle letters
def get_middle(s):
    length = len(s)
    if length == 0:
        return ""  # handle empty string safely
    elif length % 2 == 1:  # odd length
        mid = length // 2
        return s[mid]
    else:  # even length
        mid = length // 2
        return s[mid - 1:mid + 1]
