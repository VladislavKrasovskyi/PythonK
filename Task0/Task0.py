from random import randint

# variabels
maximum_elements_in_array = 0
created_array = []
created_array_with_negative_numbers = []
max_number_in_array = 0
negative_numbers_exist = False
# variabels


while maximum_elements_in_array < 30:
    created_array.append(randint(-100, 100))

    if created_array[-1] > max_number_in_array:
        max_number_in_array = created_array[-1]

    if created_array[-1] < 0:
        created_array_with_negative_numbers.append(created_array[-1])
        negative_numbers_exist = True


    maximum_elements_in_array += 1


# Output information
print()
print()
print("Created array with numbers between -100, 100")
print(created_array)
print()
print("Maximum in array")
print(max_number_in_array)
print("Index of maximum in array (starts from zero)")
print(created_array.index(max_number_in_array))

if negative_numbers_exist:
    print("Created array with negative numbers sorted")
    print(sorted(created_array_with_negative_numbers, reverse=True) )
else:
    print("No negative numbers in array")
print()