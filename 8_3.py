# a = input()
# b = input()
#
# while i in a:
#     count_a = 0
#     new_str_a = a[::1]
#     count_a += 1
# for j in b:
#     str_b = b.count(new_str_a,0)
# print(str_b)

def counter(text_1: str, text_2: str) -> int:
    min_len = min([len(text_1), len(text_2)])
    counter_equal_letters: int = 0
    for i in range(min_len):
        if text_1[i] == text_2[i]:
            counter_equal_letters += 1
    return counter_equal_letters
