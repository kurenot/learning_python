def counter(max_num: int):
    i = max_num
    hundreds = []
    sevens = {}
    while i > 0:
        if i % 2 == 1:
            print("number:", i)
        if i % 100 == 0:
            hundreds.append(i * i)
        if i % 7 == 0:
            sevens[i] = i * i
        i -= 1 # i = i + 1
    for num in hundreds:
        print("hundreds:", num)
    for key, value in sevens.items():
        print(key, value)

counter(1000)
