

txt = 'abcdcba'

start = 0
end = len(txt) - 1

while start < end:
    if txt[start].lower() == txt[end].lower():
        print(ord(txt[start]))
        print(txt[end])
    start += 1
    end -= 1


while start < end:
    if (ord(txt[start]) > 98 ):
        c = ord(txt[start]) + 26
        print(c)
    start += 1
    end -= 1


    # A = 65, Z = 90
# a = 98, z = 122