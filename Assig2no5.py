#To check the string is palindrome or not

def palindrome(check):
    check1 =check[::-1]
    if check == check1:
        return "true"
    else:
        return "false"

stringtocheck = input("enter the string: ")
text=palindrome(stringtocheck)
print(f"The result is {text}")
