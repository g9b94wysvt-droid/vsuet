def count_numbers_from_digits(n, a, b, c):
    count = 0
    digits = {str(a), str(b), str(c)}
    for num in range(100, n + 1):
        s_num = str(num)
        if all(digit in digits for digit in s_num):
            count += 1
    return count

def reverse_words_in_string(text):
return " ".join(text.split() [::-1])
