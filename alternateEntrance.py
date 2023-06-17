import goblinKing
import theBeginning
import mainGate

def enter_hidden_passage():
    print("")
    print("Aric slide into the small hole. Cramped in he crawled through the dirt.")
    print("After going for a bit Aric was blinded by the darkness. He started to feel the ground cracking.")
    print("A part of Aric feared that the the hole might cave in. But he had come so far he had to know where it led!")
    print("Aric sat and pondered what he should do.")
    choice = input("Go onward! (1) or go back (2): ")
    if choice == '1':
        print("with his might Aric moved forward! Just a step forward after he fell through the floor! Before he knew it")
        goblinKing.start_fight_normal()
    elif choice == '2':
        continue_searching()
    else:
        print("Invalid choice. Please try again.")
        enter_hidden_passage()

def continue_searching():
    print("")
    print("After some more searching Aric came upon a cave. Like the hole it could lead anywhere.")
    print("At this point Aric needed to commit and go in or just go back to the main gate.")
    choice = input("enter the cave (1) or go back to the main gate (2): ")
    if choice == '1':
        enter_cave()
    elif choice == '2':
        print('Aric walked back to the main gate.')
        theBeginning.enter_main_gate()
    else:
        print("Invalid choice. Please try again.")
        continue_searching()

def enter_cave():
    print("")
    print("As Aric ventured into the cave he ran into a group of spiders! They surrounded him as they swayed in a methodic way. Almost as a dance.")
    print("Were they challenging him to fight or dance? Either way he could not run.")
    choice = input("fight them! (1) mimic their dance! (2) run away! (3): ")
    if choice == '1':
        fight_spiders()
    elif choice == '2':
        dance_spiders()
    elif choice == "3":
        run_anyway()
    else:
        print("Invalid choice. Please try again.")
        continue_searching()

def fight_spiders():
    print("")
    print("Aric pulled his sword and charged the spiders! He hacked and slashed through them until they scattered from fear.")
    print("Aric then pushed deeper into the cave to find a cliff. A dead end!\n He looked down below and to his amazement saw his foe!")
    print("The goblin king! Just sitting there picking his nose! It was to far to jump down to face the monster so Aric looked around")
    print("All he could find was a boulder a ways off. Aric knew that if he could push the boulder he might just crush the goblin king.")
    print("Or he could miss and risk being revealed. Not knowing if it would work Aric debated if he should risk it or just go back to square one.")
    choice = input("push the boulder (1) or go back to the start (2): ")
    if choice == '1':
        goblinKing.boulder_ending()
    elif choice == '2':
        theBeginning.enter_main_gate()
    else:
        print("Invalid choice. Please try again.")
        enter_hidden_passage()

def dance_spiders():
    print("")
    print("Aric started to sway with the spiders. Maybe by trying to blend in they would let him go.")
    print("The spiders seemed to like this dancing so Aric slowly started to back up.")
    print("Then... He tripped! The spiders went into a rage and attacked! On the floor Aric was defenseless and couldn't withstand them\nhis adventure was over.")
    print("The End")

def run_anyway():
    print("")
    print("Aric dashed away as fast as he could. But apparently eight legs are faster then two.")
    print("Before he could reach the end of the cave the spiders had caught up. Causing his demise.")
    print("The End")