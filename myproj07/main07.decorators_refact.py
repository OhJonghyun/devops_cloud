import time

# 인자에 대한 리턴값을 저장
# - key : 인자 값에 대한 튜플
# - value : 그 인자로 함수를 수행했을 때의 리턴값
# cached = {}  # 전역변수 (가급적 지양해야 합니다.)

# def mysum2(x, y):
#     key = (x, y)
#     if key not in cached:
#         time.sleep(1)  # 1초간 대기
#         cached[key] = x + y + 10
#     return cached[key]


def memoize(fn):
    cached = {}

    def wrap(x, y):
        key = (x, y)
        if key not in cached:
            cached[key] = fn(x, y)
        return cached[key]

    return wrap


@memoize
def mysum2(x, y):
    time.sleep(1)
    return x + y + 10


# mysum2 = memoize(mysum2)
# mysum2(1, 2)


@memoize
def mymultiply2(x, y):
    time.sleep(1)
    return x * y + 10


mymultiply2 = memoize(mymultiply2)


print(mysum2(1, 2))
print(mysum2(1, 3))
print(mysum2(1, 3))
print(mysum2(1, 2))
print(mysum2(1, 2))

print(mymultiply2(1, 2))
print(mymultiply2(1, 2))
print(mymultiply2(1, 3))
print(mymultiply2(1, 3))


# def base(base_number):
#     def fn(x, y):
#         return x + y + base_number

#     return fn


# base_10 = base(10)
# base_20 = base(20)
# print(base_10(1, 2))
# print(base_20(1, 2))

# name = "Tom"
# mysum = lambdax, y: x +y

# other_name = name
# other_fn = mysum

# def fn(x):
#     y = "Hello"
#     return y

# fn(name)
