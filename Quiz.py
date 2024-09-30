#SeamusEvans-Sept29th-Quiz Generator 

correct_count = 0

U_input = int(input("Question 1- \nWhat was the release year of Kings Field? \n").strip())
if U_input == 1994: 
    print("Correct")
    correct_count += 1
else:
    print("Incorrect")

U_input = int(input("Question 2- \nWhen was Armored Core released? \n").strip())
if U_input == 1997:
    print("Correct")
    correct_count += 1
else:
    print("Incorrect")

U_input = input("Question 3- \nWhat was FromSoftware's 2009 hit title named? \n").lower()
if U_input == "demon's souls":
    print("Correct")
    correct_count += 1
else:
    print("Incorrect")

U_input = input("Question 4- \nWhich game series is known for its difficulty and includes the titles Dark Souls, Bloodborne, and Elden Ring? \n").lower()
if U_input == "soulsborne":
    print("Correct")
    correct_count += 1
else:
    print("Incorrect")

U_input = input("Question 5- \nWhat is the name of the director famous for his work on the Dark Souls and Bloodborne series? \n").lower()
if U_input == "hidetaka miyazaki":
    print("Correct")
    correct_count += 1
else:
    print("Incorrect")

U_input = int(input("Question 6- \nIn which year was Bloodborne released? \n"
                    "1. 2013\n"
                    "2. 2014\n"
                    "3. 2015\n"
                    "4. 2016\n"
                    "Your answer: ").strip())
if U_input == 2:  
    print("Correct")
    correct_count += 1
else:
    print("Incorrect")

U_input = int(input("Question 7- \nWhich game marked FromSoftware's first entry into the mech-combat genre? \n"
                     "1. Metal Wolf Chaos\n"
                     "2. Armored Core\n"
                     "3. Chromehounds\n"
                     "4. Steel Battalion\n"
                     "Your answer: ").strip())
if U_input == 2: 
    print("Correct")
    correct_count += 1
else:
    print("Incorrect")

U_input = int(input("Question 8- \nWhich of these games was developed by FromSoftware? \n"
                     "1. Bloodborne\n"
                     "2. Devil May Cry\n"
                     "3. Resident Evil\n"
                     "4. Final Fantasy\n"
                     "Your answer: ").strip())
if U_input == 1:
    print("Correct")
    correct_count += 1
else:
    print("Incorrect")

U_input = int(input("Question 9- \nWhat is the name of the main character in Sekiro: Shadows Die Twice? \n"
                     "1. Jin Sakai\n"
                     "2. Wolf\n"
                     "3. Geralt\n"
                     "4. Arthur Morgan\n"
                     "Your answer: ").strip())
if U_input == 2:
    print("Correct")
    correct_count += 1
else:
    print("Incorrect")

U_input = int(input("Question 10- \nWhich of these games is NOT part of the Dark Souls series? \n"
                     "1. Dark Souls\n"
                     "2. Dark Souls II\n"
                     "3. Elden Ring\n"
                     "4. Dark Souls III\n"
                     "Your answer: ").strip())
if U_input == 3:
    print("Correct")
    correct_count += 1
else:
    print("Incorrect")

U_input = input("Question 11- \nThe 2022 open-world action RPG developed by FromSoftware is called ____________. \n").lower().strip()
if U_input == "elden ring":
    print("Correct")
    correct_count += 1
else:
    print("Incorrect")

U_input = input("Question 12- \nThe multiplayer component of the Dark Souls series is known as ____________. \n").lower().strip()
if U_input == "summoning":
    print("Correct")
    correct_count += 1
else:
    print("Incorrect")

U_input = input("Question 13- \nThe kingdom where Dark Souls takes place is called ____________. \n").lower().strip()
if U_input == "lordran":
    print("Correct")
    correct_count += 1
else:
    print("Incorrect")

U_input = input("Question 14- \nThe famous 'moonlight sword' appears in many FromSoftware games, first appearing in ____________. \n").lower().strip()
if U_input == "king's field":
    print("Correct")
    correct_count += 1
else:
    print("Incorrect")

U_input = input("Question 15- \nIn Bloodborne, the player hunts beasts in the city of ____________. \n").lower().strip()
if U_input == "yharnam":
    print("Correct")
    correct_count += 1
else:
    print("Incorrect")

total_questions = 15
grade_percentage = (correct_count / total_questions) * 100

print(f"\nYou got {correct_count}! correct answers out of {total_questions}.")
print(f"Your grade is: {grade_percentage:.2f}%!!")
