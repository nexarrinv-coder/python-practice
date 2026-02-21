# name  = input("What is your name? ")
# activity  = input("What is your favorite activity? ")

# print(f'\n{name.capitalize()} likes {activity.capitalize()}!')

# print(len(""))

# first_name = input("What is your first name? ")
# last_name = input("What is your last name? ")
# print(f'😒😒\nYour first name is {len(first_name)} letters long\nyour last name is {len(last_name)} letters long')

# name = input("What is your name? ")
# feeling = input("How are you feeling? ")

# print(f'\nHello {name.capitalize()} \nAm glad your feeling {feeling.lower()}!')

# x=1
# print(x, type(x))

# print "Hello World" // common mistake in python 3, should be print("Hello World")

# string_int = "100"
# print(string_int, type(string_int))
# try_adding_10 = string_int + 10
# print(try_adding_10)

# display the foods of the customer
# foods = input('Enter the foods you want to have\n(separate these with a comma",") : ')
# index = 1
# for (each) in (foods.split(',')):
#   print(f'#{index} : {each.strip()}')
#   index = index + 1

def lister ():
  index = 1
  items_list = input('Enter the foods you want to have\n(separate these with a comma",") : ')
  for (each) in (items_list.split(',')):
    print(f'#{index} : {each.strip()}')
    index += 1

lister()