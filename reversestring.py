def reverseWords(s):
    return " ".join(reversed(s.split()))

s = "attack on titan"
rs=reverseWords(s)
print(rs)
