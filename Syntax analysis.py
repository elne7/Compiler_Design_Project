"""
Created on Wed Dec 27 17:08:11 2023

@author: A7MaD_Elne7
"""

def A(s, i):
    if i < len(s) and s[i + 1] == 'a':
        if i + 1 < len(s) and s[i + 2] == 'b':
            return i + 3
        else:
            return i + 2
    return 0

def valid():
    print("\nString is valid\n")

def invalid():
    print("\nString is invalid\n")

def main():
    print("Grammar:")
    print("S -> cAd")
    print("A -> ab/a")

    s = input("Enter the String:\n")
    i = 0

    if s[i] == 'c' and i < len(s):
        i = A(s, i)
        if i < len(s) and s[i] == 'd' and i + 1 == len(s):
            valid()
        else:
            invalid()
    else:
        invalid()

if __name__ == "__main__":
    main()