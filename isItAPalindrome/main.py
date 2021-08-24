# Write function that checks if a given string (case insensitive) is a palindrome.

def is_palindrome(s):
    for i in range(len(s)//2):
        print(s[-i-1].lower(), i)
        if s[-i-1].lower() != s[i].lower():
            return False
    return True



print(is_palindrome("gbvsrfeg"))