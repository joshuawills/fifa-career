#!/usr/bin/env python3

from src.edit_career_utils import add_accomplishment, add_game, add_player, add_season, change_player_status, add_competition

def edit_existing_career():
    print("MAKE SURE YOU HAVE AN ACTIVE CAREER")
    edit_options = ["Add player", "Change player status", "Add game", "Add accomplishment",
    "Add competition", "Add season", "Return to main menu"]

    string = "SELECT AN OPTION: \n\n"
    for i, x in enumerate(edit_options):
        string += f"\t[{i+1}]: {x}\n"
    string += "\n\t"

    while True:
        print("CAREER EDITING MODE\n\t\t")
        answer = int(input(string))
        if answer <= 0 or answer > len(edit_options):
            clear()
            print("Please provide a valid option")
            continue
       
        match answer:
            case 1: add_player()
            case 2: change_player_status()
            case 3: add_game()
            case 4: add_accomplishment()
            case 5: add_competition()
            case 6: add_season()
            case 7:
                clear()
                print("RETURNED TO MAIN MENU\n")
                return

        clear()