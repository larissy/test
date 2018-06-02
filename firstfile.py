"""Goal: A user enters their name, and if they have a text file they can enter notes, then close.
If not, a new file is created for them to enter information into. A file is held for each user."""

person_name: str = input('Hi! What\'s your name? ')

print(f'Hello {person_name}!')

"""look for file with this name+'s_details.txt'. If it exists, say that a file exists, 
 ask if they would like to view their notes (if yes then read else next),
 ask if they want to make some notes in it (if yes append else next), 
 ask if they want to keep their existing notes (if no, delete), say bye.
 If the name does not exist, then move onto following questions"""

person_age = input('It\'s nice to meet you. How old are you? ')

print(f'You must have learned many interesting things in your {person_age} years, {person_name}. '
      f'I\'ve made a notebook for you, so you can write everything down if you like.')

f = open(f'{person_name}s_details.txt', 'w+')

f.write(f'{person_name}, {person_age}. Happy writing!')

print(f'Would you like to make some notes, {person_name}?')

"""If yes, then the below, else bye"""

print('That\'s great! Type them here, and I\'ll save them for you.')

f.close()


