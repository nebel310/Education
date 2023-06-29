def is_palindrome(s):
    return s == s[::-1]

input_str = input("Введите строку: ")
print(is_palindrome(input_str))
