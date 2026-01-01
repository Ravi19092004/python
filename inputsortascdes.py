def sort_numbers():
    numbers = input("Enter a list of numbers separated by spaces: ").split()
    numbers = [int(num) for num in numbers]

    order = input("Enter 'asc' for ascending or 'desc' for descending order: ")

    if order.lower() == 'asc':
        sorted_numbers = sorted(numbers)
    elif order.lower() == 'desc':
        sorted_numbers = sorted(numbers, reverse=True)
    else:
        print("Invalid input for order. Please enter 'asc' or 'desc'.")
        return

    print(f"Sorted numbers in {order} order: {sorted_numbers}")

# Run the function
sort_numbers()