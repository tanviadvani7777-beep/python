#3. Write a program to enter marks of 4 subjects and display result (result shall include total, percentage and grade)

print("program of result")
m1= int (input("enter 1st subject Mark:"))
m2= int (input("enter 2nd subject Mark:"))
m3= int (input("enter 3rd subject Mark:"))
m4 =int (input("enter 4th subject Mark:"))
Total =(m1+m2+m3+m4)/4
if Total >= 80:
    result = "o"
    print("your Result is :", result)
elif Total >= 70:
    result = "A+"
    print("your Result is :", result)
elif Total >= 60:
    result = "A"
    print("your Result is :", result)
elif Total >= 45:
    result = "pass"
    print("your Result is :", result)
elif Total >= 35:
    result = "FAIL"
print("your Total perecentage is:" , Total)

