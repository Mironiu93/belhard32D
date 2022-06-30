x = int(input("Введите число: "))
def dec_to_bin(x):
    return bin(x)
print(dec_to_bin(x)[2:])
x_bin = dec_to_bin(x)[2:]
def bin_to_dec(x_bin):
    bin_len = len(x_bin)
    dec_digit = 0
    for i in range (0,bin_len):
       dec_digit = dec_digit + int(x_bin[i]) * (2 ** (bin_len - i - 1))
    return dec_digit
print(bin_to_dec(x_bin))