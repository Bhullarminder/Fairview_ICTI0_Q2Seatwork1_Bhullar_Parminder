from pyscript import display, document


x = ["name", "age", "section"]
y = ["parme", "15", "Saph"]
display(x + y)

x.insert(2, "switz")
display(x)

# del- deletes by index, del fruits[1]
# .remove() removes item fruits.remove("orng")
# .pop() removes and returns item(by index or last if none) fruits.pop(3)
fruits = ["apl", "bana", "Mng", "orng" ]
fruits.pop(3)
display(fruits)


fruits.sort()
display(fruits)

fruits.reverse()
display(fruits)

numbers = [3, 1, 2]
display(sorted(numbers))
display(numbers)

a = ["mnd", "tue", "wed", "thur", "fri"]

display("sun" in a)
display(len(a))
display(a.count("wed"))
a_update = a.copy()
display(a)


# a.sort()
# display(a)

# a.reverse()
# display(a)

display(sorted(a))
display(a)

# Import document and display


def adding_numbers(e):  # 'e' is used for the event handler
    # Get the value from the first input field and convert it to a float
    num1 = float(document.getElementById("input1").value)

    # Get the value from the second input field and convert it to a float
    num2 = float(document.getElementById("input2").value)

    # Adds the two numbers together
    result = num1 + num2

    # Display the result in the element with the ID "output1"
    display(result, target="output1")


# A tuple can store multiple values in one variable
# This tuple contains the numbers 1, 2, and 3
sample_tuple = 1, 2, 3

# Another way to create a tuple is by using parentheses
sample_tuple2 = ('one', 'two', 'three')

# Tuple unpacking:
# a gets 'one', b gets 'two', and c gets 'three'
a, b, c = sample_tuple2

display(type(sample_tuple))
# Indexing a tuple:
# [0] gets the first item because Python starts counting at 0
display(sample_tuple2[0])  # Displays 'one'

# 'b' contains the second value from the tuple
display(b)  # Displays 'two'


# A list can store multiple values and uses square brackets []
superhero_list = ['Captain America', 'Captain Marvel', 'Thor']

# Convert the list into a tuple using tuple()
superhero_tuple = tuple(superhero_list)

# Check the data type of the original list
display(type(superhero_list))  # <class 'list'>

# Check the data type after converting it to a tuple
display(type(superhero_tuple))  # <class 'tuple'>