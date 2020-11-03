dic = {1: 11, 2: 10, 3: 9}
dic1 = {k: v for k, v in sorted(dic.items(), key=lambda a: a[1])}
print(dic1)
