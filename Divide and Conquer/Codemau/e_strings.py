def is_equal(a, b):
    if a == b:
        return True

    m = len(a) // 2
    a1, b1 = a[:m], b[:m]
    a2, b2 = a[m:], b[m:]
    if len(a1) != len(a2) or len(b1) != len(b2):
        return False

    if is_equal(a1, b1) and is_equal(a2, b2):
        return True
    if is_equal(a1, b2) and is_equal(a2, b1):
        return True

    return False


a = input().strip()
b = input().strip()
if is_equal(a, b):
    print("YES")
else:
    print("NO")