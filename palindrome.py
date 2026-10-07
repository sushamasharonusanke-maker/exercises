s = input("Enter a string: ")
print(("The string is not a palindrome.", "The string is a palindrome.")[s == s[::-1]])