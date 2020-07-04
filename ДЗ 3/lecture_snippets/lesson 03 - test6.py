flag = True

x=10
for i in range(11):
    flag = flag and x%10 == 0
    print(flag)
    