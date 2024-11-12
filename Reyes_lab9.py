numrow = int(input("Enter the number of rows for the triangle: ")) # Get the user to input the number of rows
counter = 1  # Initialize a counter

for i in range(1, numrow + 1):        # Loops and printing the triangle
    for b in range(i):
        print(counter, end=" ")
        counter += 1
    print()