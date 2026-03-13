# Open the file
with open("numbers.txt", "r") as file:
    numbers = []

    # Read each line and convert to integer
    for line in file:
        numbers.append(int(line.strip()))

# Calculate results
total = sum(numbers)
maximum = max(numbers)
minimum = min(numbers)

# Display results
print("Total =", total)
print("Maximum =", maximum)
print("Minimum =", minimum)
