def check_digits(game):
    number_string = ''
    for character in game:
        if character.isdigit() == True:
            number_string = number_string + character
    return int(number_string)

with open("day_2_text.txt") as text:
    lines = [line.strip() for line in text]
    count = 1
    total_sum = 0
    power_sum = 0
    for line in lines:
        minimum_red = 0
        minimum_blue = 0
        minimum_green = 0
        print(line)
        print(count)
        line = line.split(':')
        line = line[1]
        print(line)
        line = line.split(';')
        print(line)
        game_pass = False
        for game in line:
            single_game = game.split(',')
            print(f"Single game is {single_game}")
            for game in single_game:
                red = 0
                blue = 0
                green = 0
                game = game.strip()
                if 'red' in game:
                    red = check_digits(game)
                    if minimum_red == 0:
                        minimum_red = red
                    elif red > minimum_red:
                        minimum_red = red
                elif 'blue' in game:
                    blue = check_digits(game)
                    if minimum_blue == 0:
                        minimum_blue = blue
                    elif blue > minimum_blue:
                        minimum_blue = blue
                elif 'green' in game:
                    green = check_digits(game)
                    if minimum_green == 0:
                        minimum_green = green
                    elif green > minimum_green:
                        minimum_green = green
        print(f"The minimum values are red = {minimum_red}, green = {minimum_green} and blue = {minimum_blue}")
        power = minimum_green * minimum_blue * minimum_red
        print(f"Power of game is {power}")
        power_sum += power
        print(f"Current power sum is {power_sum}")
        if game_pass == True:
            total_sum += count
        count += 1



check_digits("20 blue")


