
def get_word_count(s):
    return len(s.split())


#
print(get_word_count("우리는 파이썬을 즐겨요"))


def get_ch_count_except_space(s):
    count = 0
    for ch in s:
        if ch != " ":
            count += 1
    return count


# 
print(get_ch_count_except_space("우리는 파이썬을 즐겨요"))


def get_rounded_number(number):
    return (number // 1000) * 1000


# 
print(get_rounded_number(1234567))