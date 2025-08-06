import string


def is_palindrome(text):
    """palindrome"""
    punkt = string.punctuation + ' '
    format_tex = ''.join(i for i in text.lower() if i not in punkt)
    return format_tex == format_tex[::-1]


assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")
