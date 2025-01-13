#Ava Mendoza
print("Welcome to What TV Show Are You")
print("Answer the questions to find out which TV show you are")
ans = input("morning or evening ?")
if ans =="morning":
    ans = input("summer or spring ?")
    if ans == "summer":
        ans = input("surfing or swiming ?")
        if ans == "surfing":
            print("Your TV Show is Outter Banks")
        else:
            print("Your TV Show is The Summer I turned Pretty")
    else:
        ans = input("driving or biking ?")
        if ans == "driving":
            print("Your TV Show is One Tree Hill")
        else:
            print("Your TV Show is Stranger Things")
else:
    ans = input("autumn or winter ?")
    if ans == "autumn":
        ans = input("coffee or tea ?")
        if ans == "coffee":
            print("Your TV Show is Gilmore Girls")
        else:
            print("Your TV Show is The Vampire Diaries")
    else:
        ans = input("shopping or working ?")
        if ans == "shopping":
            print("Your TV Show is Gossip Girl")
        else:
            print("Your TV Show is Grays Anatomy")

