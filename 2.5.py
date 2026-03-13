#Write a program to read a file and display its contents. At the end it shall also display no. of words availabcount = 0
count = 0

file = open("sample.txt", "r")

for line in file:
    print(line, end="")      # display file contents
    words = line.split()     # split line into words
    count += len(words)      # count words

file.close()

print("\nTotal number of words:", count)
