keep_running = True

while keep_running == True:
    day = input("Enter a day(or type'exit'to quit): ")
    
    if day == "exit":
        print("Goodbye! see you on monday at IIST.")
        keep_running = False

    elif day == "Monday":
        print("8:00 - Math | 9:00 - Physics | 10:00 - Civil | 10:50 - Mechanical")

    elif day == "Tuesday":
        print("8:00 - Civil | 9:00 - Mechanical | 10:00 - BCE | 10:50 - Physics") 

    else:
        print("That's not a weekday, or it's a holiday!")
