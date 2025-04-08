string = "Python is awesome"
cnt1 = 0
cnt1 += string.count('a')
cnt1 += string.count('e')
cnt1 += string.count('i')
cnt1 += string.count('o')
cnt1 += string.count('u')

cnt2 = 0
l = ['a', 'e', 'i', 'o', 'u']
for ch in string:
    if ch in l:
        cnt2 += 1

print(cnt1)
print(cnt2)
