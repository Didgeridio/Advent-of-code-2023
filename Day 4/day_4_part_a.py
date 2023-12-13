total = 0

with open("day_4.txt") as text:
    for line in text:
        winning_count = 0
        line = line.split()
        line = line[2:]
        print(line)
        winning_numbers = line[:10]
        print(f"Winning Numbers: {winning_numbers}")
        your_numbers = line[11:]
        print(f"Your Numbers: {your_numbers}")
        for number in winning_numbers:
            if number in your_numbers:
                print(f"Winning number found: {number}")
                winning_count += 1
        print(f"Winning Count: {winning_count}")
        if winning_count == 1:
            total += 1
        elif winning_count > 1:
            points = pow(2, (winning_count -1))
            print(points)
            total += points
        print(total)
    print(f"Total: {total}")
