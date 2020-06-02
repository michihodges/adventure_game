import time
import random


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(1)


def intro(villain):
    print_pause("You find yourself in an open field, filled with grass "
                "and yellow flowers.")
    print_pause(f"Rumor has it that a {villain} is somewhere around here, "
                "and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty (but not very effective) "
                "dagger.\n")


def field(villain, items):
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print("What would you like to do?")
    house_cave(villain, items)


def house_cave(villain, items):
    select_path = input("(Please enter 1 or 2.)\n")
    if select_path == '1':
        house(villain, items)
    elif select_path == '2':
        cave(villain, items)
    else:
        house_cave(villain, items)


def house(villain, items):
    print_pause("You approach the door of the house.")
    print_pause(f"You are about to knock when the door opens and out steps a "
                f"{villain}.")
    print_pause(f"Eep! This is the {villain}'s house!")
    print_pause(f"The {villain} attacks you!")
    if 'Sword of Ogoroth' not in items:
        print_pause("You feel a bit under-prepaired for this, what with only "
                    "having a tiny dagger.")
    fight(villain, items)


def fight(villain, items):
    fight_flee = input("Would you like to (1) fight or (2) run away?")
    if fight_flee == '1':
        if 'Sword of Ogoroth' in items:
            print_pause(f"As the {villain} moves to attack, you unsheath your "
                        "new sword.")
            print_pause("The Sword of Ogoroth shines brightly in your hand as "
                        "you brace yourself for the attack.")
            print_pause(f"But the {villain} takes one look at your shiney new "
                        "toy and runs away.")
            print_pause(f"You have rid the town of the {villain}. You are "
                        "victorious!")
        else:
            print_pause("You do your best...")
            print_pause(f"but your dagger is no match for the {villain}.")
        play_again()
    elif fight_flee == '2':
        print_pause("You run back into the field. Luckily you don't seem to "
                    "have been followed.")
        field(villain, items)
    else:
        fight_flee(villain, items)


def cave(villain, items):
    print_pause("You peer cautiously into the cave.")
    if 'Sword of Ogoroth' in items:
        print_pause("You have been here before, and gotten all the good "
                    "stuff. It's just an empty cave now.")
    else:
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the Sword of Ogoroth!")
        print_pause("You discard your silly old dagger and take the sword "
                    "with you.")
        items.append('Sword of Ogoroth')
    print_pause("You walk back out to the field.\n")
    field(villain, items)


def play_again():
    replay = input("Would you like to play again? (y/n)").lower()
    if replay == 'y':
        print_pause("Excellent! Restarting the game...")
        play_game()
    elif replay == 'n':
        print_pause("Thanks for playing! See you next time.")
    else:
        play_again()


def play_game():
    list_of_villains = ['troll', 'wicked farie', 'pirate', 'dragon', 'gorgon']
    villain = random.choice(list_of_villains)
    items = []
    intro(villain)
    field(villain, items)


play_game()
