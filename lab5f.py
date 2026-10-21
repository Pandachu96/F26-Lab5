# Add comments before you do anything else.
#!/usr/bin/env python3
# Author: Zebang Yang
# Date: 10/21/2026
# Purpose: Catch ZeroDivisionError
# Usage: ./lab5f.py

# TO DO 1: Complete the given functions.

def safe_divide(a,b):
  # divide a by b
  # Add an exception block to raise the error if error occurs because of a zero denominator.
  # Except block should display the appropriate error messages
  try:
    result = a / b
    print(f"The result of {a} divided by {b} is: {result}")
  except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

  except Exception as e:
    print(f"Error: {e}")

def main():
  safe_divide(10,5)  # works
  safe_divide(10,0)  # exception : Zero Division Error


if __name__ == "__main__":
  main()