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
        print(f"Current numbers: {current_numbers}")
        print(f"Current symbols: {current_symbols}")
        print(f"Previous numbers: {previous_numbers}")
        print(f"Previous symbols: {previous_symbols}")
        print(f"Current numbers: {current_numbers}. Will check vs previous symbols")
        remove_list = []
        for inside_list in current_numbers:
            number = inside_list[0]
            for index in inside_list[1:]:
                if index in previous_symbols:
                    print(f"{number} found at {index} in previous_symbols so adding and removing it")
                    final_numbers.append(number)
                    remove_list.append(inside_list)
                    break
        if current_numbers != []:
            for item in remove_list:
                current_numbers.remove(item)
        print(f"New current numbers: {current_numbers}. Will now check vs current symbols")
        remove_list = []
        for inside_list in current_numbers:
            number = inside_list[0]
            for index in inside_list[1:]:
                if index in current_symbols:
                    print(f"{number} found at {index} in current_symbols so adding and removing it")
                    final_numbers.append(number)
                    remove_list.append(inside_list)
                    break
        if current_numbers != []:
            for item in remove_list:
                current_numbers.remove(item)
        print(f"New current numbers: {current_numbers}")
        print(f"Previous numbers: {previous_numbers}")
        remove_list = []
        for inside_list in previous_numbers:
            number = inside_list[0]
            for index in inside_list[1:]:
                if index in current_symbols:
                    print(f"{number} found at {index} in current_symbols so adding and removing it")
                    final_numbers.append(number)
                    remove_list.append(inside_list)
                    break
        if previous_numbers != []:
            for item in remove_list:
                previous_numbers.remove(item)
        print(f"New previous numbers: {previous_numbers}")
        print(final_numbers)
    print(final_numbers)
    for number in final_numbers:
        total += number
    sum_numbers = sum(final_numbers)
    final_numbers = []

    print(f"Total:{total}")
    print(f"Total summed:{sum_numbers}")