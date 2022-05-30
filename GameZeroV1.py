#--------------------------------------------------------------------------------#
# Text Based Adventure Game - "Game Zero"
#
# Copyright (c) 2022 Malkasiangroup, LLC
#
# All Rights Reserved
#
# VERSION: 1.0 Alpha (Pre-Release)
#
#--------------------------------------------------------------------------------#
#BUGS
# 1. Users can press enter in a text entry field to skip past it [FIXED - 05/23/2022]
# 2. The gender choice section needs to loop [FIXED - 05/20/2022]

#--------------------------------------------------------------------------------#
#IMPORTED LIBRARIES

import winsound



#--------------------------------------------------------------------------------#
#FUNCTIONS

#Allows to user to press enter to move to the next screen.
def pressEnter():
	print("[Press Enter]")
	blankKeyPress = input()


#Function to update the user inventory
def add(a,b):
    result = a + b
    return result

#updateInventory = ('NAME_OF_ITEM',)
#userInventory = add(userInventory, updateInventory)


#Splash screen for loosing the game.
def youLoose():
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("**************************************************************************")
        print("****************************** YOU LOST **********************************")
        print("**************************************************************************")
        print("**************************************************************************")
        print("**************************************************************************")
        print("**************************************************************************")
        print("\nUhhh ohhhh, guess what just happened...\n")
        pressEnter()
        gameCredits()

#Game credits and copyright information.
def gameCredits():
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("**************************************************************************")
        print("***************************THANKS FOR PLAYING!****************************")
        print("**************************************************************************")
        print("**************************************************************************")
        print("*****************Text Based Adventure Game - 'Game Zero'******************")
        print("**************************************************************************")
        print("**************************************************************************")
        print("*****************Copyright (c) 2022 Malkasiangroup.com********************")
        print("***************************All Rights Reserved.***************************")
        print("**************************************************************************")
        print("**************************************************************************")
        print("*************Written and developed by SPC Malkasian, Samuel.**************")
        print("**************************************************************************")
        print("******************Contact us at: malkasianGroup@gmail.com*****************")
        print("**************************************************************************")
        print("*********************VERSION: 1.0 Alpha (Pre-Release)*********************")
        print("**************************************************************************")
        print("**************************************************************************")
        print("*****************************DISCLAIMER:**********************************")
        print("**************************************************************************")
        print("***This source code is the intelectual property of MalkasianGroup, LLC.***")
        print("**********************Modifying is permitted.*****************************")
        print("*********Redistrubution under a different name is not permitted.**********")
        print("**************************************************************************")
        pressEnter()
        exit()

def youLooseDS():
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN")
        print("NNNNNNNNNNNNNNNNNNNNNNNNNNNNN @@ NNNNNNNNNNNNNNNNNNNNNNNNNNNNN")
        print("NNNNNNNNNNNNNNNNNNNNNNNN@            @NNNNNNNNNNNNNNNNNNNNNNNN")
        print("NNNNNNNNNNNNNNNNNNN@         /##\         @NNNNNNNNNNNNNNNNNNN")
        print("NNNNNNNNNNNNNNNNNNN          \##/          NNNNNNNNNNNNNNNNNNN")
        print("NNNNNNNNNNNNNNNNNN@                        @NNNNNNNNNNNNNNNNNN")
        print("NNNNNNNNNNNNNNNNNN@                        @NNNNNNNNNNNNNNNNNN")
        print("NNNNNNNNNNNNNNNNN@                          @NNNNNNNNNNNNNNNNN")
        print("NNNNNNNNNNNNNNN@                              @NNNNNNNNNNNNNNN")
        print("NNNN@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@NNNNN")
        print("NNNNNNNNNNNNNNNI                              INNNNNNNNNNNNNNN")
        print("NNNNNNNNNNNNNNNI  ''''''\            /''''''  INNNNNNNNNNNNNNN")
        print("NNNNNNNNNNNNNNNI   < @ >              < @ >   INNNNNNNNNNNNNNN")
        print("NNNNNNNNNNNNNNNI              __              INNNNNNNNNNNNNNN")
        print("NNNNNNNNNNNNNNNNI            [  ]            INNNNNNNNNNNNNNNN")
        print("NNNNNNNNNNNNNNNNNI  ----              ----  INNNNNNNNNNNNNNNNN")
        print("NNNNNNNNNNNNNNNNNNI    |              |    INNNNNNNNNNNNNNNNNN")
        print("NNNNNNNNNNNNNNNNNNNI   |              |   INNNNNNNNNNNNNNNNNNN")
        print("NNNNNNNNNNNNNNNNNNNNNI    @@@@@@@@@@    INNNNNNNNNNNNNNNNNNNNN")
        print("NNNNNNNNNNNNNNNNNNNNNNI    | ____ |    INNNNNNNNNNNNNNNNNNNNNN")
        print("NNNNNNNNNNNNNNNNNNNNNNNNI   ^^^^^^   INNNNNNNNNNNNNNNNNNNNNNNN")
        print("NNNNNNNNNNNNNNNNNNNNNNNNNININNNNININNNNNNNNNNNNNNNNNNNNNNNNNNN")
        print("NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN")
        print("***************YOU FOUND AN ANGRY DRILL SERGENT***************")
        print("")
        pressEnter()
        print("Stop playing games during class and pay attention.")
        youloose()

#Alternate storyline 2. ***Move this to an external file that python has to pull from***
def storyMode2():
	print("This story is stil in development. I didn't have time to finish it...")
	print("If you can code, feel free to add to the project. Just add your name to the copyright as an editor.")
	pressEnter()
	exit()

#Checks to make sure user enters the proper gender
def genderValidator():
        userGender = input("Please enter your gender [male/female]: ")
        while userGender not in ['male', 'female', 'exit']:
            userGender = input("Please enter a valid gender [male/female]: ")
        else:
            return userGender
        
def genderDecider(userGender):
    if userGender == 'exit':
        print("press enter to exit")
        pressEnter = input("")
        exit()
    elif userGender == 'male':
        print("")
    elif userGender == 'female':
        print("")

#Yes/No function that doesn't allow the user to enter anything else.
def yesNoValidator():
        userYesNo = input("[Yes/No]: ")
        while userYesNo not in ['yes', 'no', 'hello']:
            userYesNo = input("Please enter 'Yes' or 'No': ")
        else:
            return userYesNo
        
def yesNoDecider(userYesNo):
    if userYesNo == 'yes':
        print("")
        return userYesNo
    elif userYesNo == 'no':
        return userYesNo
    elif userYesNo == 'army':
        print("YOU FOUND AN EASTER EGG! I wish that meant you make it to the end of the game and win...but I'm a jerk...")
        youLoose()

#Function call sample:
#userChoiceYesNo = input("[yes/no]: ")
#userChoiceYesNo = yesNoDecider(yesNoValidator())


# 1, 2, 3, function. forces the user to choose only number options.
def numberChoiceValidator():
        userNumberChoice = input("Please enter choices [1], [2], or [3]: ")
        while userNumberChoice not in ['1', '2', '3']:
            print("You entered an invalid number. Please try again.\n")
            userNumberChoice = input("Please enter choices [1], [2], or [3]: ")
        else:
            return userNumberChoice
        
def numberChoiceDecider(userNumberChoice):
    if userNumberChoice == '1':
        return userNumberChoice
    elif userNumberChoice == '2':
        return userNumberChoice
    elif userNumberChoice == '3':
        return userNumberChoice

#Function call sample:
#userNumberChoice = input("\n[Choice]: ")
#userNumberChoice = numberChoiceDecider(numberChoiceValidator())


#--------------------------------------------------------------------------------#

#               *************START OF THE GAME CODE*************


print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print("**************************************************************************")
print("***************************** GAME ZERO **********************************")
print("**************************************************************************")
print("******************* Welcome to Game Zero (1.0 Alpha) *********************")
print("**************************************************************************")
print("**************************************************************************")
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print("                          Loading the game...                             ")
winsound.PlaySound("SystemHand", winsound.SND_ALIAS)
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

print("\n\nWould you like to play?")
userChoiceYesNo = yesNoDecider(yesNoValidator())
while userChoiceYesNo != "yes":
	exit()
else:
	pass
print("\n\nGreat! Let's get started!")

userName = input("\nPlease tell me your full name. [First Last]: ")

#In case the user adds a letter or invalid character.
userAge = 0
while userAge == 0:
        try:
                userAge = int(input("Enter your age: "))
        except ValueError:
                print("You entered an invalid number. Please try again")


#Sets the user money ammount
defaultGold = 10
userGold = defaultGold

if userAge < 10:
	userGold = 100
elif userAge < 20:
	userGold = 200
elif userAge < 25:
	userGold = 300
else:
	userGold = 500

userInventory = ('Bag of Gold', 'Suitcase')

print(f"\nWelcome to the game {userName}! Your gold ammount is {userGold}!")
pressEnter()
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print("\nLet's begin. This is a text based game where you will be")
print("faced with multiple decisions and will have to logically think through")
print("your choices or else you might lose the game...")
pressEnter()

#Introduction to the main game storyline
print("\n\n\n\n\n\n\n\n\n\n")
print(f"You are faced with a brand new opportunity of luxery and riches!\nYou can travel to California and start a business!")
userChoiceYesNo = yesNoDecider(yesNoValidator())
if userChoiceYesNo == "no":
	print("\nYou go home, get a boring job at Western Mikes BBQ Burgers and Shakes\nand live the rest of your time-bored and depressed.")
	pressEnter()
	print("\nAre you happy with your choice?")
	userChoiceYesNoNestOne = yesNoDecider(yesNoValidator())
	if userChoiceYesNoNestOne == "no":
		print("\nWhat would you like to do? \n[1] Move to Cali.\n[2] Try becoming store manager.\n[3] Stay working as linecook.\n")
		userNumberChoiceNestTwo = numberChoiceDecider(numberChoiceValidator())
		if userNumberChoiceNestTwo == "1":
                        print("\n\nYou go to your manager and tell him:")
                        print("[1] 'You suck. I hate this job, I hate this place. I'm leaving'")
                        print("[2] 'Sir, I don't think this job is for me. Here are my two weeks.'")
                        print("[3] 'Sir, thank you so much for this job. I see myself doing this for a long time.'")
                        userNumberChoiceNestThree = numberChoiceDecider(numberChoiceValidator())
                        if userNumberChoiceNestThree == "1":
                                print("The manager gets angry and fires you before you have time to quit. There goes a job reference...")
                                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                                print("Without a job and no references, you starve and die.")
                                pressEnter()
                                youLoose()
                        if userNumberChoiceNestThree == "2":
                                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                                print(f"The manager understands. He tells you, '{userName}, you've been a good worker. Here's a reference letter'")
                                userInventory = 'Wallet', 'Suitcase', 'Reference Letter'
                                print(f"You now have a {userInventory} in your inventory.")
                                pass
                        if userNumberChoiceNestThree == "3":
                                print("So begins your life of working for 'Western Mikes BBQ Burgers and Shakes' as a cook.")
                                storyMode2()
		elif userNumberChoiceNestTwo == "2":
                        print("\n\nThe manager tells you that he's been impressed with your work ethic...")
                        pressEnter()
                        print("but he doesn't quite think you have what it takes to be a store manager.")
                        pressEnter
                        print("Maybe give it a little more time there, guy.")
                        pressEnter()
                        print("Just a little dissapointed, you get back to work. While cleaning the fryer, you spill some oil...")
                        pressEnter()
                        print("You slip and fall and hit your head. The fryer, filled with soap and water boils over...")
                        pressEnter()
                        print("It covers you in oil residue and scalding hot water. \n\nRIP.")
                        pressEnter()
                        youLoose()
		elif userNumberChoiceNestTwo == "3":
                        storyMode2()
	elif userChoiceYesNoNestOne == "yes":
                storyMode2()
elif userChoiceYesNo == "yes":
        pass

#CALIFORNIA STORY LINE
print("\n\n\nCongradulations! You are now on your way to California!")
pressEnter()
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print("Upon arriving, you have just enough gold to get a hotel room...A rather nice one!")
print("Do you rent a hotel room?")
userChoiceYesNo = yesNoDecider(yesNoValidator())
if userChoiceYesNo == "no":
	print("\nWith no where else to go, you find a nice little spot under a bridge.")
	print("\nAre you happy with your choice?")
	userChoiceYesNoNestOne = yesNoDecider(yesNoValidator())
	if userChoiceYesNoNestOne == "no":
		print("\n\nWhat would you like to do: \n[1] Pick up the cardboard box you saw earlier.\n[2] Fight a homeless man for his tent.")
		userNumberChoiceNestTwo = numberChoiceDecider(numberChoiceValidator())
		if userNumberChoiceNestTwo == "1":
                        print("\nA cardboard box has been added to your inventory!")
                        updateInventory = ('Cardboard Box',)
                        userInventory = add(userInventory, updateInventory)
                        print(userInventory)
                        pressEnter()
                        print("With your new found cardboard box, you set it up under the bridge.")
                        print("Do you: \n[1] Go to sleep? \n[2] Decide this all was a bad idea and try to get a hotel instead.")
                        userNumberChoiceNestThree = numberChoiceDecider(numberChoiceValidator())
                        if userNumberChoiceNestThree == "1":
                                print("You begin to drift to sleep")
                                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                                print("Without a job and no references, you starve and die.")
                                pressEnter()
                                youLoose()
                        if userNumberChoiceNestThree == "2":
                                print("You leave the cardboard box for some other homeless chap and continue on your way.")
                                pressEnter()
                                print("You arrive at the hotel, talk to the attendant, and rent a room.")
                                print("What should you do next: \n[1] Ask the attendent if there are any jobs in the area. \n[2] Just go to your room. \n[3] Beat the attendant up and take his money. ")
                                userNumberChoiceNestFour = numberChoiceDecider(numberChoiceValidator())
                                if userNumberChoiceNestFour == "1":
                                        print("\nA business card with contact info has been added to your inventory!\n")
                                        updateInventory = ('Business Card',)
                                        userInventory = add(userInventory, updateInventory)
                                        print(userInventory)
                                        pressEnter()
                                if userNumberChoiceNestFour == "2":
                                        print("You take your key, thank the attendant, and go to your room.")
                                        print("The bed is comfy and you sleep well. Looks like tomorrow is a great day to start setting up a life here.")
                                        pressEnter()
                                        print("You wake up refreshed and begin your day. Time to call that number on the business card.")
                                        pass    
                                if userNumberChoiceNestFour == '3':
                                        print("You rush the attendant and punch him square in the face. Dazed, he takes a swing back. He misses you.")
                                        pressEnter()
                                        print("You swing again and make contact. He falls over knocked out cold.")
                                        print("You reach into his pocket and take his wallet. There's 100 gold pieces!")
                                        userGold = userGold + 100
                                        print(f"\nYou now have {userGold}")
                                        pressEnter()
                                        print("While you think you're slick getting away with beating up that man and stealing his gold...")
                                        pressEnter()
                                        print("You see some people near by frantically call 911 and tell them about the situation.")
                                        print("You can: \n[1] Stay right there. \n[2] Run away. \n[3] Beat up the people calling 911")
                                        userNumberChoiceNestFive = numberChoiceDecider(numberChoiceValidator())
                                        if userNumberChoiceNestFive == '1':
                                              print("You stand there as the cops arrive. They tell you to stay right there (weapons drawn).")
                                              pressEnter()
                                              print("You slowly get down onto your knees as the officers rush you.")
                                              pressEnter()
                                              print("You think about what you've just done... Is it worth running you wonder...")
                                              userChoiceYesNoNestSix = input("Do you run?")
                                              userChoiceYesNoNestSix = yesNoDecider(yesNoValidator())
                                              if userChoiceYesNoNestSix == 'yes':
                                                      print("You quickly get up and make a dash for it...")
                                                      pressEnter()
                                                      print("The officers shoot you with a taser. You colapse to the ground and have a heart attack from the shock")
                                                      youLoose()
                                              if userChoiceYesNoNestSix == 'no':
                                                      print("The officer drops you to the ground with his knee in your back.")
                                                      print("You get handcufed and put into the squad car and the officer slams the door.")
                                                      pressEnter()
                                                      youLoose()
                                        if userNumberChoiceNestFive == '2':
                                              print("You look around frantically. Seeing an exit that appears clear, you run with all your might.")
                                              pressEnter
                                              print("You bust open the door and make it outside. You scan around quickly and see a fence...")
                                              print("What if there's a dog in there?")
                                              userChoiceYesNoNestSix = input("Do you jump the fence?")
                                              userChoiceYesNoNestSix = yesNoDecider(yesNoValidator())
                                              if userChoiceYesNoNestSix == 'yes':
                                                    print("You decide to take the chance and jump the fence. You thought you heard growling...")
                                                    pressEnter()
                                                    print("... No dog.")
                                                    pressEnter()
                                                    print("You run through the yards and get a ways from the hotel. You hear sirens in the distance.")
                                                    print("\n Looks like you got away.")
                                                    print("You run far away from the place and fall asleep under a bridge.")
                                                    print("Some generous homeless lets you borrow a box.")
                                                    pressEnter()
                                                    print("You wake up somewhat rested the next morning...")
                                                    pressEnter()
                                                    pass
                                              if userChoiceYesNoNestSix == 'no':
                                                    print("You try running down the alley way and see a police car. You freeze.")
                                                    pressEnter()
                                                    print("He saw you...")
                                                    pressEnter()
                                                    print("You try to run but it's too late. He spins out of his car and points his taser...")
                                                    pressEnter()
                                                    print("You wake up dazed, in handcufs. They load you into the car and slam te door.")
                                                    pressEnter()
                                                    youLoose()        
                                        if userNumberChoiceNestFive == "3":      
                                              print("You rush the people calling 911. It's a father and a son.")
                                              print("Just as you land the first blow, the son rushes you, knocking you off your feet.")
                                              print("Dazed, you try to get up but the father comes down on you, catching you square in the face.")
                                              print("A bystander joins the fight and helps to pin you to the ground.")
                                              pressEnter()
                                              youLoose()
                                if userNumberChoiceNestThree == '3':
                                        print("So... you entered an invalid number... 3 wasn't on the list now, was it?")
                                        print("I know it wasn't... because I wrote the game.")
                                        pressEnter()
                                        youLooseDS()
		if userNumberChoiceNestTwo == '2':
                        print("Almost loosing the fight, you take the man's tent while sustaining only a few bruises.")
                        pressEnter()
                        print("\nYou set up the tent and unpack your things inside.")
                        pressEnter()
                        print("\nIt's about 8pm at night and you're starting to feel tired... so you start to fall asleep...")
                        pressEnter()
                        print("\nWhat you didn't count on was the homeless man coming back...")
                        pressEnter()
                        print("Aaand... he beats you up in your sleep.")
                        pressEnter()
                        youLoose()
		if userNumberChoiceNestTwo == '3':
                        print("So... you entered an invalid number... 3 wasn't on the list now, was it?")
                        print("I know it wasn't... because I wrote the game.")
                        pressEnter()
                        youLooseDS()
	if userChoiceYesNoNestOne == "yes":
                print("Listen, I get you think it's cool to 'break the game,' but it takes a LOT of work to write this...")
                print("So, I'm gonna make this easy for you. You tried sleeping under the bridge, it was cold, you froze to death, and died.")
                pressEnter()
                youLoose()
if userChoiceYesNo == 'yes':
        print("You arrive at the hotel, talk to the attendant, and rent a room.")
        print("What should you do next: \n[1] Ask the attendent if there are any jobs in the area. \n[2] Just go to your room. \n[3] Beat the attendant up and take his money. ")
        userNumberChoiceNestOne = numberChoiceDecider(numberChoiceValidator())
        if userNumberChoiceNestOne == "1":
                print("\nA business card with contact info has been added to your inventory!\n")
                updateInventory = ('Business Card',)
                userInventory = add(userInventory, updateInventory)
                print(userInventory)
                pressEnter()
                print("You take your key, thank the attendant, and go to your room.")
                print("The bed is comfy and you sleep well. Looks like tomorrow is a great day to start setting up a life here.")
                pressEnter()
                print("You wake up refreshed and begin your day.")
                pass
        if userNumberChoiceNestOne == "2":
                print("You take your key, thank the attendant, and go to your room.")
                print("The bed is comfy and you sleep well. Looks like tomorrow is a great day to start setting up a life here.")
                pressEnter()
                print("You wake up refreshed and begin your day.")
                pass
        if userNumberChoiceNestOne == '3':
                print("You rush the attendant and punch him square in the face. Dazed, he takes a swing back. He misses you.")
                pressEnter()
                print("You swing again and make contact. He falls over knocked out cold.")
                print("You reach into his pocket and take his wallet. There's 100 gold pieces!")
                userGold = userGold + 100
                print(f"\nYou now have {userGold}")
                pressEnter()
                print("While you think you're slick getting away with beating up that man and stealing his gold...")
                pressEnter()
                print("You see some people near by frantically call 911 and tell them about the situation.")
                print("You can: \n[1] Stay right there. \n[2] Run away. \n[3] Beat up the people calling 911")
                userNumberChoiceNestTwo = numberChoiceDecider(numberChoiceValidator())
                if userNumberChoiceNestTwo == '1':
                        print("You stand there as the cops arrive. They tell you to stay right there (weapons drawn).")
                        pressEnter()
                        print("You slowly get down onto your knees as the officers rush you.")
                        pressEnter()
                        print("You think about what you've just done... Is it worth running you wonder...")
                        userChoiceYesNoNestThree = yesNoDecider(yesNoValidator())
                        if userChoiceYesNoNestThree == 'yes':
                                print("You quickly get up and make a dash for it...")
                                pressEnter()
                                print("The officers shoot you with a taser. You colapse to the ground and have a heart attack from the shock")
                                youLoose()
                        if userChoiceYesNoNestThree == 'no':
                                print("The officer drops you to the ground with his knee in your back.")
                                print("You get handcufed and put into the squad car and the officer slams the door.")
                                pressEnter()
                                youLoose()
                if userNumberChoiceNestTwo == '2':
                        print("You look around frantically. Seeing an exit that appears clear, you run with all your might.")
                        pressEnter
                        print("You bust open the door and make it outside. You scan around quickly and see a fence...")
                        print("What if there's a dog in there?")
                        print("Do you jump the fence?")
                        userChoiceYesNoNestThree = yesNoDecider(yesNoValidator())
                        if userChoiceYesNoNestThree == 'yes':
                                print("You decide to take the chance and jump the fence. You thought you heard growling...")
                                pressEnter()
                                print("... No dog.")
                                pressEnter()
                                print("You run through the yards and get a ways from the hotel. You hear sirens in the distance.")
                                print("\n Looks like you got away.")
                                pressEnter()
                                pass
                        if userChoiceYesNoNestThree == 'no':
                                print("You try running down the alley way and see a police car. You freeze.")
                                pressEnter()
                                print("He saw you...")
                                pressEnter()
                                print("You try to run but it's too late. He spins out of his car and points his taser...")
                                pressEnter()
                                print("You wake up dazed, in handcuffs. They load you into the car and slam the door.")
                                pressEnter()
                                youLoose()        
                if userNumberChoiceNestTwo == "3":      
                        print("You rush the people calling 911. It's a father and a son.")
                        print("Just as you land the first blow, the son rushes you, knocking you off your feet.")
                        print("Dazed, you try to get up but the father comes down on you, catching you square in the face.")
                        print("A bystander joins the fight and helps to pin you to the ground.")
                        pressEnter()
                        youLoose()

print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print("**************************** [ DAY 2 ]  ********************************")
print("\n\n\n\n\n\n\n\n\n\n")
pressEnter()

print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")                    
print("It's a bright new day in California!")
pressEnter()

#Life in Cali storyline
print("New to California, you make a few phone calls to see if there's work in the area.")
print

#Keep this at the end of the game so it doesn't exit.
print("\n\n\n\n ***YOU'VE REACHED THE END OF THE CODE***")
pressEnter()
exit()


