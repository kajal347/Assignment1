'''Write a program that prompts the user for two integer values and displays the results of the first number divided by the second, with exactly two decimal places displayed.'''
a=int(input ("Enter the 1st number"))
b=int(input("Enter the 2nd number"))
c=a/b
value=round(c,2)
print(value)