# Palindrome

def Palindrome(a):
    a=a.replace(" "," ").lower()
    if (a==a[::-1]):
        return "Palindrome"
    else:
        return "Not Palindrome"

a=input("Enter String")
print(Palindrome(a))
