f1, f2, count = 0, 1, 0
while f2 < 10000000:
    count += 1
    if count > 27:
        print('Итераций больше, чем 27. Прерываюсь.')
        break
    f1, f2 = f2, f1 + f2
    if f2 < 1000:
        continue
    print(f2)
else:
    print('Было', count, 'итераций')