#Reverse the number with user input

n=int(input("Enter the number="))
rev=0
while n > 0:
    avg = n % 10
    rev = rev * 10 + avg
    n = n // 10
print("Reverse number=",rev)
