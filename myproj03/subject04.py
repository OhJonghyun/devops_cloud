#04. 구구단 퀴즈 break 안 쓴 버전

for number in range(2, 10):
    for i in range(1, 10):
        if number >= i:
            print(f"{number} * {i} = {number * i}")