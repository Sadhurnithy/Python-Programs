def get_element_at_index(numbers):
    try:
        index = int(input("Enter the index: "))
        element = numbers[index]
        print("Element at index {} is: {}".format(index, element))
    except IndexError:
        print("Index out of range!")
    except ValueError:
        print("Invalid index! Please enter a valid integer.")

# Example usage
n = int(input("Enter the number of elements in the list: "))
numbers = []
for i in range(n):
    number = int(input("Enter element {}: ".format(i)))
    numbers.append(number)

get_element_at_index(numbers)
