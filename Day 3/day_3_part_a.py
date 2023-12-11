'''
Initial plan for program

Go through each line one at a time

Run through the line checking for numbers. If you find a digit then check for digit until it
returns false and then add each to a string then convert to int
Add each number to a dictionary, the key is the number and the value is its positions + 1 either side. (Same as symbol)
Set this dictionary to current number dict

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

