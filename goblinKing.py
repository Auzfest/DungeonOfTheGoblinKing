def start_fight_normal():
    print("")
    print("Aric enters a big chamber, in the middle the infamous goblin king!")
    print("Aric quickly unsheathed his sword! What way should he attack?")
    choice = input("Charge the front! (1) go behind! (2): ")

    if choice == '1':
        charge()
    elif choice == '2':
        behind()
    else:
        print("Invalid choice. Please try again.")
        start_fight_normal()

def charge():
    print("")
    print("Aric lunged straight at the goblin king! At the same time the king goes for a punch!")
    print("The two collided with each other. Next thing Aric was forced through th ceiling and outside back to where he started.")
    print("In complete pain he sat there rethinking what he had just went through.")
    print("Once he had strength to get up he decided he wasn't the hero for this job, then turned around to go home.")
    print("The Sad End")

def behind():
    print("")
    print("Aric used his speed to get behind the goblin king as it tried to hit him.")
    print("The goblin king was now vulnerable for Aric to attack! What should he do?")
    choice = input("Cgo for the head! (1) go for the arm! (2): ")

    if choice == '1':
        go_for_the_head()
    elif choice == '2':
        go_for_arm()
    else:
        print("Invalid choice. Please try again.")
        start_fight_energy_sword()

def go_for_the_head():
    print("")
    print("Aric leaped and sliced at the head of the goblin king!")
    print("The goblin king was defeated! Aric went back home praised a hero throughout the land, with promise to continue to protect his kingdom.")
    print("The End")

def go_for_arm():
    print("")
    print("Aric sliced the arm of the goblin king right off! In pain the Goblin King went into a rage!")
    print("It turned and swung it's other arm at Aric before he could respond. Aric got hit into the wall.")
    print("The goblin king proceed to swing again and ended the fight.")
    print("The Terrible End")

    



def start_fight_energy_sword():
    print("Aric enters a big chamber, in the middle the infamous goblin king!")
    print("Aric quickly unsheathed his sword! It glows brughtly filling Aric with power!")
    print("What way should he attack?")
    choice = input("Charge the front! (1) go behind! (2): ")

    if choice == '1':
        charge_es()
    elif choice == '2':
        behind_es()
    else:
        print("Invalid choice. Please try again.")
        start_fight_energy_sword()

def charge_es():
    print("")
    print("Aric lunged straight at the goblin king! At the same time the king goes for a punch!")
    print("The sword and fist collided as a bright light filled the room.")
    print("When the light faded the two stared for a moment not knowing who won.")
    print("Then the goblin king fell, Aric had won in one blow!")
    print("Aric went back to the kingdom and was praised for his heroics, with his sword he continued to become a mighty hero!")
    print("The Great End 1")

def behind_es():
    print("")
    print("Aric dashed behind the goblin king as it was too slow to grab him. He thenswung up with his new sword.")
    print("His swing cause a great beam of energy to shoot up and through the goblin king!")
    print("The goblin king collapsed. Aric did it! However his slice has made the chamber start to crumble!")
    choice = input("Run! (1) Hide! (2): ")

    if choice == '1':
        run()
    elif choice == '2':
        hide()
    else:
        print("Invalid choice. Please try again.")
        start_fight_energy_sword()

def run():
    print("")
    print("Aric ran as fast as he could out of the chamber. Avoiding falling rockes Aric got out of the dungeon as it collapsed!")
    print("After dusting off he went back to the kingdom and was praised for his heroics\nwith his sword he continued to become a mighty hero!")
    print("The Exciting Good End")

def hide():
    print("")
    print("Aric went and hid under some cover to avoid the rockfall. The chamber collapsed in on itself and trapped Aric!")
    print("Crushed in and running out of breath Aric smiled knowing that though he would not make it back.")
    print("The kingdom would once again be safe, all thanks to him.")
    print("The Good Sad End")



def boulder_ending():
    print("")
    print("Aric pushed the boulder with all his might! The boulder started to roll and fell off the edge below.")
    print("Below a screech is heard! Looking down Aric found that the goblin king was squashed! Now the kingdom would not have to fear the goblin king again!")
    print("The Easy End")