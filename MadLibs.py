#Ava Mendoza
#Mad Libs
#12-9-24
#Initalize
#Functions
def Mad_Libs_Game():
#Main
    print("Welcome To The Mad Libs Game!")
    print("Please respond to the following questions.")
    adjective = input ("Choose an adjective")
    occupation = input ("Choose an occupation")
    location = input ("Choose a location")
    noun = input ("Choose a noun")
    adjective2 = input ("choose an adjective")
    animal = input ("Choose an aminal")


    print("Once apon a time, in a land far far away, there was the most "+ str(adjective) + " princess to ever live.")
    print("However, this was no ordinary princess. She dreamed of becoming a " + str(occupation) + ".")
    print("The princess worked day and night to acheive her dreams of becoming a " + str(occupation)+ ",")
    print("But her royal parents disproved of her desires and locked her away in " + str(location) + ".")
    print("But the princess was very intelligent and was able to escape with the help of her trusty " + str(noun) + ".")
    print("Once she escaped " + str(location) + ", she found a " + str(adjective2)  + " " + str(animal) + ".")
    print("She then hopped on the " + str(animal) + " and rode far far away to follow her dreams of becoming a " + str(occupation) + ".")

Mad_Libs_Game()
