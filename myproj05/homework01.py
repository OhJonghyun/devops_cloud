from random import randint

number = randint(1, 100)
# is_pass = False  # plauge 변수
for retry in range(1, 11):
    line = input(f"[{retry}] try guess number : ")
    answer = int(line.strip() or 0)
    #  try:
    #     # answer = int(line.strip() or 0)
    #     answer = int(line.strip())
    # except ValueError:
    #     print("잘못된 값을 입력하셨습니다.")
    #     continue
    if answer == number:
        print(f"{retry}회 시도에 성공.")
    elif answer < number:
        print("더 큰 수를 입력해주세요")
    else:
        print(print("더 작은 수를 입력해주세요"))

else:
    # if is_pass == False:
    print("다음 기회에...")
