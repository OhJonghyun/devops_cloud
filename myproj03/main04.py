#01.반복문을 활용하여, 효과적으로 3단/6단/9단 구구단 출력하기

for number in range(3, 10, 3):
    print("### {}단 ###".format(number))
    for i in range(1, 10):
        result = number * i
        print("{} * {} = {}".format(number, i, result))
    print("")