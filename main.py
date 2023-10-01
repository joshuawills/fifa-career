#!/usr/bin/env python3

import sys, os, subprocess, re

from src.utilities import clear, num_active_careers, print_careers, base_directory, count_file, active_career_file
from src.edit_career import add_accomplishment, add_game, add_player, add_season, change_player_status, add_competition
from src.new_career import create_new_career
from src.delete_career import delete_old_career
from src.list_career import list_all_careers
from src.set_career import set_active_career

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
                print("Returned to main menu\n")
                return

        clear()


def view_career():
    pass

def main():

    clear()
    initial_options = ["CREATE CAREER", "DELETE CAREER", "EDIT CAREER", 
    "LIST CAREERS", "VIEW CAREER", "SET CAREER", "EXIT"]

    string = "SELECT AN OPTION: \n\n"
    for i, x in enumerate(initial_options):
        string += f"\t[{i+1}]: {x}\n"
    string += "\n\t"

    while True:
        active_file = ""
        with open(active_career_file, "r") as f:
            active_file_number = f.readlines()

        if not (len(active_file_number) == 0 or active_file_number[0].strip() == ""):
            print("ACTIVE CAREER: ", end="")
            career_directory = os.path.join(base_directory, f"career{active_file_number[0]}")
            with open(os.path.join(career_directory, "keyInfo"), "r") as f:
                data = f.readlines()[0].replace("CAREER_NAME: ", "").strip()
                print(data)

        answer = int(input(string))
        if answer <= 0 or answer > len(initial_options):
            clear()
            print("Please provide a valid option")
            continue
            
        clear()
        match answer:
          case 1: create_new_career()
          case 2: delete_old_career()
          case 3: edit_existing_career()
          case 4: list_all_careers()
          case 5: view_career() ## TO DO
          case 6: set_active_career()
          case 7:
            clear()
            sys.exit(0)
          case _: pass

if __name__ == "__main__":
    main()
