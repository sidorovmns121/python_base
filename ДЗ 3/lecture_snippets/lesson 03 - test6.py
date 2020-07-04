flag = True

x=10
for i in range(12):
    flag = flag and x%10 == 0
    print(flag)
    