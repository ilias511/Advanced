def palindrome(str,ind):
    if ind == len(str)//2:
        return f'{str} is a palindrome'

    if str[ind] != str[len(str) - ind - 1]:
        return f'{str} is not a palindrome'

    return palindrome(str,ind+1)


print(palindrome("abcba", 0))
print(palindrome("peter", 0))