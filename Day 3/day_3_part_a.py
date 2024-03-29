'''
Initial plan for program

Go through each line one at a time

Run through the line checking for numbers. If you find a digit then check for digit until it
returns false and then add each to a string then convert to int
Add each number to a dictionary, the key is the number and the value is its positions + 1 either side. (Same as symbol)
Set this dictionary to current number dict

Cant use dictionaries as it doesnt accept multiple of the same number

Go through each character in the line first checking for symbols. Put their position in a list
that contains their position and the one lower and one above.
Set this list to current symbol list


Now you run through for the line and check what symbol positions overlap with the number positions in the dictionary
If they do overlap you remove them from the list and add them to the total

Moving to the next line you get the numbers and set current list (dict) to previous list
and new numbers to current

You then get the symbols and again set list to old list and new ones to current.

Then you go through old numbers and check them versus new symbols.
Again if they match remove from dict and add to total.

Now you go through the current numbers checking them against the old symbols.
If they match you remove them from the dictionary and add to the total

Then you check current numbers versus current symbols
Match = remove from dict and add to total

Then you move to next line and repeat the process.

You then check if new numbers are in contact with old symbols etc

'''

def set_number(number_string, number_position_list, current_numbers):
    if number_string != '':
        number = int(number_string)
        number_list = [number]
        for index in number_position_list:
            number_list.append(index)
        current_numbers.append(number_list)



with open("day_3.txt") as text:
    lines = [line.strip() for line in text]
    print(lines)
    current_numbers = []
    previous_numbers = []
    number_position_list = []
    current_symbols = []
    previous_symbols = []
    number_string = ''
    final_numbers = []
    final_numbers_remove = []
    total = 0
    for line in lines:
        print(line)
        line = f".{line}."
        print(line)
        character_index = 0
        previous_symbols = current_symbols
        current_symbols = []
        previous_numbers = current_numbers
        current_numbers = []
        for character in line:
            if character == ".":
                set_number(number_string, number_position_list, current_numbers)
                number_string = ''
                number_position_list = []
                character_index += 1
                continue
            elif character.isdigit() == True:
                number_string += str(character)
                number_position_list.append(character_index)
                character_index += 1
            else:
                #character must be a symbol
                if character_index != 0:
                    minus_index = character_index - 1
                else:
                    minus_index = 0
                plus_index = character_index + 1
                current_symbols.append(minus_index)
                current_symbols.append(character_index)
                current_symbols.append(plus_index)
                set_number(number_string, number_position_list, current_numbers)
                number_string = ''
                number_position_list = []
                character_index += 1
        remove_list = []
        for inside_list in current_numbers:
            number = inside_list[0]
            for index in inside_list[1:]:
                if index in previous_symbols:
                    final_numbers.append(number)
                    remove_list.append(inside_list)
                    break
        if current_numbers != []:
            for item in remove_list:
                current_numbers.remove(item)
        remove_list = []
        for inside_list in current_numbers:
            number = inside_list[0]
            for index in inside_list[1:]:
                if index in current_symbols:
                    final_numbers.append(number)
                    remove_list.append(inside_list)
                    break
        if current_numbers != []:
            for item in remove_list:
                current_numbers.remove(item)
        remove_list = []
        for inside_list in previous_numbers:
            number = inside_list[0]
            for index in inside_list[1:]:
                if index in current_symbols:
                    final_numbers.append(number)
                    remove_list.append(inside_list)
                    break
        if previous_numbers != []:
            for item in remove_list:
                previous_numbers.remove(item)
    for number in final_numbers:
        total += number
    sum_numbers = sum(final_numbers)
    final_numbers = []

    print(f"Total:{total}")
    print(f"Total summed:{sum_numbers}")