'''4.	Write a program to accept an input string from the user and determine the vowels in the string and calculate the number of vowels. (Hint: Use filter method.)
Example:
Input: quintessential
Output: ['u', 'i', 'e', 'e', 'i', 'a']; 6
'''
name = input("enter the name:")
lst = ["a","e","i","o","u"]
ls = list(filter(lambda x : x in lst,name))
print(ls)
print(len(ls))