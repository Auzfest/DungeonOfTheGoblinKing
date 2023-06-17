import goblinKing

def follow_well_lit_path():
    print("")
    print("Aric cautiously followed the well-lit path, hoping it would lead him closer to the goblin king's lair. \nAs he progressed, he stumbled upon a room with two doors:")
    choice = input("Choose the door on the left (1) or the door on the right (2): ")

    if choice == '1':
        choose_left_door()
    elif choice == '2':
        choose_right_door()
    else:
        print("Invalid choice. Please try again.")
        follow_well_lit_path()

def choose_left_door():
    print("")
    print("Aric pushed open the door on the left and discovered a hidden treasure chest. \nAs he opened it the chest attacked! It was a mimic! The mimic grabbed Aric with its tongue reeling him in. Aric could either slice the tongue or try to slice the mimic itself.")
    choice = input("slice the tongue (1) or go for the mimic (2): ")
    if choice == '1':
        slice_tongue()
    elif choice == '2':
        slice_mimic()
    else:
        print("Invalid choice. Please try again.")
        choose_left_door()

def slice_tongue():
    print("")
    print("Aric sliced the tongue off and freed himself. In doing so the Mimic writhed in pain as it died. \nAric inspecting the dead mimic finds a glowing orange sword. He takes it and feels the power of the sword in his hand.")
    print("He then back tracked to the right door where a gang of goblins with swords and bows awaited him. With his new weapon he sliced through the goblins with ease.")
    goblinKing.start_fight()

def slice_mimic():
    print("")
    print("Aric let the mimic reel him close and when to stab its body. His weapon bounced of the thick wood like skin. \nBefore he realized his mistake the mimic pounced upon him.")
    print("The End")




def choose_right_door():
    print("")
    print("As Aric went through the right door he found a gang of goblins in front of him. \nSome brandished their rusty swords while others prepared their bows. Clearly it was time to fight. Aric had to decide a strategy.")
    choice = input("Choose to attack the archers (1) or the sword goblins (2): ")
    if choice == '1':
        attack_archers()
    elif choice == '2':
        attack_swordsman()
    else:
        print("Invalid choice. Please try again.")
        choose_right_door()

def attack_archers():
    print("")
    print("Aric dashed past the goblins with swords toward the archers. He went through them swiftly hacking them down in a blur. \nHe turned toward the rest ready to fight them just  to find they had ran. He shrugged and pushed forward.")
    goblinKing.start_fight_normal()

def attack_swordsman():
    print("")
    print("Aric attacked the goblin with the swords. He hacked through one, then two, \nand right before he could finish the third he got shot by an arrow. Then another. Soon it was too many for him to handle.")
    print("The End")



def venture_darkened_corridor():
    print("")
    print("As Aric went down the dark corridor he soon found himself in pitch black unable to see. \nHearing skittering around him he debates his choice and considers whether to continue or go back.")
    choice = input("Continue down the darkened corridor (1) or go back and take the well-lit path (2): ")

    if choice == '1':
        continue_darkened_corridor()
    elif choice == '2':
        follow_well_lit_path()
    else:
        print("Invalid choice. Please try again.")
        venture_darkened_corridor()

def continue_darkened_corridor():
    print("")
    print("Aric pushed bravely forward! Sadly it would be to his demise. \nThe skittering around him were hungry big rats. Once Aric got closed they fed on their new meal.")
    print("The End")