import mainGate
import alternateEntrance

def firstSteps():
    print("")
    print("The Dungeon's Challenge")
    print("Once upon a time, in a land far away, there lived a courageous hero named Aric.")
    print("Legends spoke of a fearsome goblin king who ruled over a treacherous dungeon.")
    print("Determined to bring peace to the kingdom, Aric set forth on a perilous quest to defeat the goblin king and restore harmony to the land.")

    # Start of the story
    choice = input("Enter the dungeon through the main gate (1) or search for an alternative entrance (2): ")

    if choice == '1':
        enter_main_gate()
    elif choice == '2':
        search_alternative_entrance()
    else:
        print("Invalid choice. Please try again.")
        firstSteps()

def enter_main_gate():
    print("")
    print("Upon entering Aric was not caught with another decision! Ahead lied two paths, a well-lit path or a darkened corridor.")
    choice = input("Take the well-lit path (1) or venture into the darkened corridor (2): ")

    if choice == '1':
        mainGate.follow_well_lit_path()
    elif choice == '2':
        mainGate.venture_darkened_corridor()
    else:
        print("Invalid choice. Please try again.")
        enter_main_gate()

def search_alternative_entrance():
    print("Going around the gate Aric searched for another way in. Eventually he found a small hole to go through. \nWho knew where this tunnel would lead. Aric wondered if he should go in or keep searching.")
    choice = input("Enter the hidden passage (1) or continue searching for another alternative (2): ")

    if choice == '1':
        alternateEntrance.enter_hidden_passage()
    elif choice == '2':
        alternateEntrance.continue_searching()
    else:
        print("Invalid choice. Please try again.")
        search_alternative_entrance()
