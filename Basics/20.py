def pattern20(n):
    # Initializing the spaces
    spaces = 2 * n - 2

    # Outer loop for printing rows
    for i in range(1, 2 * n):
        # Stars for the first half
        stars = i

        # Stars for the second half
        if i > n:
            stars = 2 * n - i

        # Printing the stars
        for j in range(stars):
            print("*", end="")

        # Printing the spaces
        for j in range(spaces):
            print(" ", end="")

        # Printing the stars
        for j in range(stars):
            print("*", end="")

        # Move to the next line
        print()

        # Adjusting spaces for the next row
        if i < n:
            spaces -= 2
        else:
            spaces += 2

# Example usage
N = 5
pattern20(N)
