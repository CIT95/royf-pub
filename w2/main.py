print("I will guess your age")

picked_number = input("Pick a number from 1 - 9: ")
year_of_birth = input("What is your year of birth? ")

multiplied_by_two = int(picked_number) * 2

added_five = int(multiplied_by_two) + 5

multiplied_by_fifty = int(added_five) * 50

#add 1769 if you had your birthday in 2022
add_1769 = int(multiplied_by_fifty) + 1769
#add 1768 if you haven't had your birthday yet
add_1768 = int(multiplied_by_fifty) + 1768

if_you_had_your_birthday = int(add_1769) - int(year_of_birth)

havent_had_your_birthday = int(add_1768) - int(year_of_birth)

your_age_if_you_had_your_birthday = int(if_you_had_your_birthday) + 3

your_age_if_you_havent_had_your_birthday = int(havent_had_your_birthday) + 3

message = f"If you had your birthday this is your age: {your_age_if_you_had_your_birthday}, if you haven't this is your age {your_age_if_you_havent_had_your_birthday}"

print("The first number is the number you picked")

print(message)

