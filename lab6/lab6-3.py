def reverse(number):
  number=number[::-1]
  return number

def is_palindrome(number):
  if number==reverse(number):
    print("The number is a palindrome.")
  else:
    print("The number is not a palindrome.")

def main():
  number=input("Enter a number: ")
  is_palindrome(number)
main()