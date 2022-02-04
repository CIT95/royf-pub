import random

name = input("What is your name?\n")

days_of_week = ["Monday", "Tuesday", "Wednesday",
                "Thursday", "Friday", "Satruday", "Sunday"]

weather = ['Sunny', 'Cloudy', 'Windy', 'Rainy', 'Foggy']


for days in days_of_week:
    print(f"Hi, {name} I will be your personal assistant for today!\n")
    print(f"Today is {days}")
    Weather = random.choice(weather)
    print(f"Today's weather is {Weather}")
    if days == "Monday" or "Tuesday" or "Wednesday" or \
               "Thursday" or "Friday" or "Saturday" or "Sunday":
        print("Are you planning to go out or stay inside? ")
        plan = input("type 'go' or 'stay': \n").lower()
        if plan == 'go':
            print("What will you do? \n")
            outside = input("Go to the 'Gym', Go for a 'Walk', Ride your 'bike', Watch a 'Movie', \
Hang out with 'friends', Go 'Shopping'.\
Type whats inside the single quotes \n").lower()

            if outside == "gym":
                print("Make sure to bring water and wear a face mask!")
            elif outside == "walk":
                print("Make sure to bring water, wear a mask, \
and watch your surroundings!")
            elif outside == "bike":
                print("Bring water and watch out for moving vehicles!")
            elif outside == "movie":
                print("Don't forget to grab yourself popcorn and a drink!")
            elif outside == "friends":
                print("Enjoy hanging out with your friends!")
            else:
                print("Don\'t forget to wear a mask! and stay safe!")
        else:
            print("What are you planning to do at home? ")
            home = input("Go 'Sleep', 'Clean', 'Cook', 'Draw', 'Read'. \
Type whats inside the single quotes \n").lower()
            if home == "sleep":
                print("Enjoy your sleep!")
            elif home == "clean":
                print("Enjoy cleaning the house!")
            elif home == "cook":
                print("Good luck on making delicious food!")
            elif home == "draw":
                print("I wish you good luck on your drawing!")
            else:
                print("Enjoy reading!")

    tmr = input("Do you want to continue to the next day? 'y' or 'n' ").lower()
    if tmr == "n":
        print("Thank you for asking for help! ")

        break
