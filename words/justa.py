def print_letter_A():
    height = 7  # Height of the letter
    width = 5   # Width of the letter
    mid = width // 2  # Middle index for the width

    for row in range(height):
        for col in range(width):
            # Print asterisks at the edges, top, and the middle row
            if col == 0 or col == width - 1 or row == 0:
                print('*', end='')
            # Print asterisks for the middle horizontal line of 'A'
            elif row == height // 2:
                print('*', end='')
            # Print spaces for the rest
            else:
                print(' ', end='')
        print()  # Move to the next line after each row

# Example usage
print_letter_A()
