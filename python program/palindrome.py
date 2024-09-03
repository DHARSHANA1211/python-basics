#CHECK FOR PALINDROME
def is_palindrome(s):
    return s==s[::-1]
string=input("Enter a String:")
if is_palindrome(string):
    print("palindrome")
else:
    print("Not a palindrome")

