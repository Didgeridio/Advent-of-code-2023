'''
To simplify this can just work down and when you win store how many of each card you have.
Dictionary or something better?
'''

total = 0
#List that stores how many bonus copies we have of scratchcards
bonus_list = []
card_number = 0

with open("day_4.txt") as text:
    for line in text:
        print(f"Card Number: {card_number}")
        if card_number < 207:
            if bonus_list:
                ticket_number = bonus_list.pop(0) + 1
                print(f"New Bonus Tickets: {bonus_list}")
                print(f"Number of tickets: {ticket_number}")
            else:
                ticket_number = 1
            line = line.split()[2:]
            print(line)
            winning_count = 0
            winning_numbers = line[:10]
            print(f"Winning Numbers: {winning_numbers}")
            your_numbers = line[11:]
            print(f"Your Numbers: {your_numbers}")
            for number in winning_numbers:
                if number in your_numbers:
                    winning_count += 1
            print(f"Winning Count: {winning_count}")
            count = 0
            while count < winning_count:
                if 0 <= count < len(bonus_list):
                    bonus_list[count] = bonus_list[count] + ticket_number
                    print(f"Added {ticket_number} to position {count} in bonus list")
                else:
                    bonus_list.append(ticket_number)
                    print(f"Appended {ticket_number} to list")
                count += 1
            print(f"Bonus Tickets: {bonus_list}")
            total += ticket_number
            card_number += 1
    print(f"Total: {total}")
