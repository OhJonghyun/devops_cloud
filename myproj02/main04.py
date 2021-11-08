# 숫자 퀴즈
# 랜덤 숫자를 맞춰보세요.

# hint random.randint를 통해 1이상 100이하의 랜덤수를 만든다

#유저에게 10회의 기회를 준다. for/range
# 그 숫자를 정확히 맞췄다면, 몇 번 만에 맞췄는지 출력
# 입력한 숫자가 랜덤수보다 작다면, "더 큰 수를 입력해주세요", 라고 출력
# 입력한 숫자가 랜덤수보다 크다면, "작은 수를 입력해주세요", 라고 출력
# 횟수를 초과했다면, "다음 기회에 ..." 라고 출력

import random

number = random.randint(1, 100)

trials = 0
while trials < 10:
    user = int(input("숫자를 입력해 주세요"))
    trials += 1
    if user == number:
        print("정답! 시도 횟수는 %d회입니다." % trials)
        break
    if user < number:
        print("더 큰 수를 입력해주세요")
    if user > number:
        print("더 작은 수를 입력해주세요")

else:
    print("다음 기회에...")

    



