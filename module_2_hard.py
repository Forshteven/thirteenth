list_1 = []
list_2 = []
for i in range(3, 21):
    for k in range(1, 20):
        for n in range(1, 20):
            if i == k + n and i%(k+n) == 0 and k != n:
                list_1.append(i)
                list_2.append(sorted([k, n]))
            else:
                pass

vicpats = [(i,p) for i,p in zip(list_1,list_2)]

vicpats_original = []
for i in vicpats:
    if i not in vicpats_original:
        vicpats_original.append(i)

dict_ = {}
for x,y in vicpats_original:
    dict_.setdefault(x,[]).append(y)


print(list_1)
print(list_2)
print(vicpats)
print(vicpats_original)
print(dict_)

for i, v in enumerate(dict_.items(), start=1):
    print(i, v)
