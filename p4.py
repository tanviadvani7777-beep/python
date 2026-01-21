#4. Write a program to enter 10 numbers and display all armstrong numbers from those numbers.
Check_Armstrong_number = int(input("Enter a number: "))
num = Check_Armstrong_number
digit, armstrong_sum = 0, 0

length = len(str(num))
for i in range(length):
    digit = num % 10
    num = num // 10
    armstrong_sum += pow(digit, length)

if armstrong_sum == Check_Armstrong_number:
    print("It's an Armstrong number:", Check_Armstrong_number)
else:
    print("Not an Armstrong number:", Check_Armstrong_number)
