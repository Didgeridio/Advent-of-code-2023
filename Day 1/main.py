def find_all(main_string, substring):
    occurrences = []
    start_index = 0

    while True:
        index = main_string.find(substring, start_index)
        if index == -1:
            break  # No more occurrences found
        index += 1
        occurrences.append(index)
        start_index = index + 1
    return occurrences

with open("day_1_text.txt") as text:
    lines = [line.strip() for line in text]
    final_count = 0
    for test in lines:
        print(test)
        one = find_all(test, 'one')
        for digit in reversed(one):
            if digit != -1:
                test = list(test)
                test.insert(digit, "1")
                test = ''.join(test)
        two = find_all(test, 'two')
        for digit in reversed(two):
            if digit != -1:
                test = list(test)
                test.insert(digit, "2")
                test = ''.join(test)
        three = find_all(test, 'three')
        for digit in reversed(three):
            if digit != -1:
                test = list(test)
                test.insert(digit, "3")
                test = ''.join(test)
        four = find_all(test, 'four')
        for digit in reversed(four):
            if digit != -1:
                test = list(test)
                test.insert(digit, "4")
                test = ''.join(test)
        five = find_all(test,'five')
        for digit in reversed(five):
            if digit != -1:
                test = list(test)
                test.insert(digit, "5")
                test = ''.join(test)
        six = find_all(test, 'six')
        for digit in reversed(six):
            if digit != -1:
                test = list(test)
                test.insert(digit, "6")
                test = ''.join(test)
        seven = find_all(test,'seven')
        for digit in reversed(seven):
            if digit != -1:
                test = list(test)
                test.insert(digit, "7")
                test = ''.join(test)
        eight = find_all(test,'eight')
        for digit in reversed(eight):
            if digit != -1:
                test = list(test)
                test.insert(digit, "8")
                test = ''.join(test)
        nine = find_all(test,'nine')
        for digit in reversed(nine):
            if digit != -1:
                test = list(test)
                test.insert(digit, "9")
                test = ''.join(test)
        temp_numbers = list()
        print(test)
        for character in test:
            if character.isdigit() == True:
                temp_numbers.append(character)
        print(temp_numbers)
        if len(temp_numbers) == 1:
            number_value = int(temp_numbers[0] + temp_numbers[0])
            print(f"Value of single one is {number_value}")
        else:
            number_value = int(temp_numbers[0] + temp_numbers[-1])
            print(f"value of multiple one is {number_value}")
        final_count += number_value
        print(f"current final count: {final_count}")
    print(final_count)
