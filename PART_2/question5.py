'''Write a program to find the simple interest when the value of principle, rate of interest and time period is provided by the user.'''
principal=int(input("Enter the principal"))
time=int(input("Enter the time"))
rate=int(input("Enter the rate"))
SI=(principal*time*rate)/100
print("The simple interest is:",SI)