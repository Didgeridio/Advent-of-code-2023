'''
Could I loop through the gears instead and for each one check if one of the values(coordinates) match up with a number
If they do add one to count and then run through again. If count is 2 at the end then multiply the numbers
Will need to do future numbers too
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
    twice_previous_numbers = []
    number_position_list = []
    current_symbols = []
    number_string = ''
    final_numbers = []
    final_numbers_remove = []
    total = 0
    line_count = 0
    for line in lines:
        line_count += 1
        line = f".{line}."
        print(line)
        character_index = 0
        previous_symbols = current_symbols.copy()
        current_symbols = []
        twice_previous_numbers = previous_numbers
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
            elif character == "*":
                #Gear
                current_symbols.append(character_index)
                set_number(number_string, number_position_list, current_numbers)
                number_string = ''
                number_position_list = []
                character_index += 1
            else:
                character_index += 1
        if line_count == 1:
            print(f"Twice previous numbers: {twice_previous_numbers}")
            print(f"Previous numbers: {previous_numbers}")
            print(f"Current numbers: {current_numbers}")
            print(f"Current symbols (what we use): {current_symbols}")
            for gear in current_symbols:
                gear_minus = gear -1
                gear_plus = gear + 1
                gears = [gear_minus, gear, gear_plus]
                match_count = 0
                number_list = []
                for sublist in twice_previous_numbers:
                    if any(gear in sublist[1:] for gear in gears):
                        match_count += 1
                        number_list.append(sublist[0])
                for sublist in previous_numbers:
                    if any(gear in sublist[1:] for gear in gears):
                        match_count += 1
                        number_list.append(sublist[0])
                for sublist in current_numbers:
                    if any(gear in sublist[1:] for gear in gears):
                        match_count += 1
                        number_list.append(sublist[0])
                if match_count == 2:
                    print(f"Found a match!")
                    print(f"The two numbers are {number_list}")
        else:
            print(f"Twice previous numbers: {twice_previous_numbers}")
            print(f"Previous numbers: {previous_numbers}")
            print(f"Current numbers: {current_numbers}")
            print(f"Previous symbols (what we use): {previous_symbols}")
            for gear in previous_symbols:
                print(gear)
                gear_minus = gear - 1
                gear_plus = gear + 1
                gears = [gear_minus, gear, gear_plus]
                match_count = 0
                number_list = []
                for sublist in twice_previous_numbers:
                    if any(gear in sublist[1:] for gear in gears):
                        match_count += 1
                        number_list.append(sublist[0])
                for sublist in previous_numbers:
                    if any(gear in sublist[1:] for gear in gears):
                        match_count += 1
                        number_list.append(sublist[0])
                for sublist in current_numbers:
                    if any(gear in sublist[1:] for gear in gears):
                        match_count += 1
                        number_list.append(sublist[0])
                if match_count == 2:
                    print(f"Found a match!")
                    print(f"The two numbers are {number_list}")
                    sum = number_list[0] * number_list[1]
                    total += sum
    print(f"Total:{total}")