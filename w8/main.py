colors = {
    "Clear":
    {'Clear': """If you have a clear urine, \
you have been drinking too much water. """},
    "Yellow":
    {'Yellowish to amber': """If you have a yellowish to \
amber urine, that is perfectly normal. """},
    "Red":
    {'Red or Pink': """If you have a red or pink urine, \
you might have ate/drank red/dyed things, etc. """},
    "Orange":
    {'Orange': """If you have an orange urine, \
it could be dehydration. """},
    "Green":
    {'Blue or Green': """If you have a blue or green urine, \
it is most likely connected to something that you ate. \
This is very rare. In rare cases, \
it could mean a bacterial infection. """},
    "Darkbrown":
    {'Dark Brown': """If you have a dark brown urine, \
it might be because of dehydration, diet related, etc. """},
    "Cloudy":
    {'Cloudy': """If you have a cloudy urine, It might be \
because of dehydration, urinary tract infection (UTI), etc. """}
}


def final():
    print("Welcome to the Urine Color Checker \n")

    name = input("What is the user's name?: ").title()
    for COLORS in colors:
        print(COLORS)

    color = input(f"{name} what is the color of your urine?: ").title()

    urine = True
    while urine:

        def test():
            if color == "Clear":
                print(colors["Clear"])
                return f"\t{name}, you need to lessen your \
drinking of water by a little. \n"
            elif color == "Yellow":
                print(colors["Yellow"])
                return f"\t{name}, keep drinking \
enough water every day to maintain this. \n"
            elif color == "Red":
                print(colors["Red"])
                return f"\t{name}, you need to get enough water each day. \
Try to avoid drinks or food with dyes in it. \
If you get worried try to make an appointment and get a urine check. \n"
            elif color == "Orange":
                print(colors["Orange"])
                return f"\t{name}, you need to drink a lot \
of water at least 8 glasses a day. \n"
            elif color == "Green":
                print(colors["Green"])
                return f"\t{name}, blue or green urine is very rare and it could be just with \
something you ate/drink. If you have this try to \
get it checked so you could know what to do. \n"
            elif color == "Darkbrown":
                print(colors["Darkbrown"])
                return f"\t{name}, you need to drink a lot \
of water at least 8 glasses a day and also try to get this checked. \n"
            elif color == "Cloudy":
                print(colors["Cloudy"])
                return f"\t{name}, you have to drink plenty of water to flush the \
bacteria. Try to avoid coffee, alcohol, and \
soft drinks until it fully goes back to normal. \n"

        answer = test()

        print(answer)

        Continue = input(f"Type 'y' to restart, \
or type 'n' to stop: ").lower()

        if Continue == "y":
            final()
        else:
            urine = False

final()
