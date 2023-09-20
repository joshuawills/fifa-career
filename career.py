#!/usr/bin/env python3

import sys, os, glob, subprocess, re

from utilities import clear, num_active_careers, print_careers, base_directory, count_file, active_career_file
from edit_player import add_accomplishment, add_game, add_player, add_season, change_player_status, add_competition

def create_new_career():

    print("CAREER CREATION MODE\n\t\t")

    name_career = input("\tWhat do you want the name of your career to be? ")
    club_career = input("\tWhat club have you started out as? ")
    league_career = input("\tWhat league are you playing in? ")
    league_season = input("\tWhat is your starting league season e.g. 21/22? ")
    manager_name = input("\tWhat is your manager name? ")

    with open(count_file, "r") as f:
        x = f.readlines()[0].strip()

    career_directory = os.path.join(base_directory, f"career{x}")
    try:
        subprocess.run(["mkdir", career_directory], check=True)
        players_directory = os.path.join(career_directory, "players")
        subprocess.run(["mkdir", players_directory], check=True)
        subprocess.run(["touch", os.path.join(career_directory, "keyInfo")], check=True)

        with open(count_file, "w") as f:
            x = str((int(x) + 1))
            f.write(x)

        with open(os.path.join(career_directory, "keyInfo"), "w") as f:
            f.write(f"CAREER_NAME: {name_career.strip()}\n")
            f.write(f"CLUB_NAME: {club_career.strip()}\n")
            f.write(f"LEAGUE_NAME: {league_career.strip()}\n")
            f.write(f"MANAGER_NAME: {manager_name.strip()}\n")

        with open(os.path.join(career_directory, "competitions"), "w") as f:
            f.write(f"{league_career.strip()}\n")

        with open(os.path.join(career_directory, "seasons"), "w") as f:
            f.write(f"{league_season.strip()}\n")

        with open(os.path.join(career_directory, "accomplishments"), "w") as f:
            f.write("")

        clear()

        print("Successfully created new career\n")
    except subprocess.CalledProcessError as e:
        print("Something failed when creating directories", e)
        sys.exit(1)

    return


def delete_old_career():
    
    while True:
        if print_careers() == 0:
            print("No current careers to delete\n")
            return

        answer = input("\nSelect a valid digit for the career to be deleted: ").strip()
        if not re.search(r"^[0-9]+$", answer):
            clear()
            print("Only provide digits")
            continue

        if not os.path.isdir(os.path.join(base_directory, f"career{answer}")):
            clear()
            print("Directory doesn't exist")
            continue

        break

    try:
        subprocess.run(["rm", "-rf", os.path.join(base_directory, f"career{answer}")], check=True)

        with open(count_file, "r") as f:
            x = str(int(f.readlines()[0].strip()) - 1)

        with open(count_file, "w") as f:
            f.write(x)

        with open(active_career_file, "r") as f:
            active_career = f.readlines()

        if len(active_career) != 0 and active_career[0].strip() == answer:
            with open(active_career_file, "w") as f:
                f.write("")

        clear()
        print(f"Successfully deleted career {answer}\n")

    except subprocess.CalledProcessError as e:
        print("Something failed when creating directories", e)
        sys.exit(1)

    return 


def edit_existing_career():

    print("MAKE SURE YOU HAVE AN ACTIVE CAREER")

    edit_options = ["Add player", "Change player status", "Add game", "Add accomplishment",
    "Add competition", "Add season", "Return to main menu"]

    string = "Select an option: \n\n"
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
        
        if answer == 1:
            add_player()
        elif answer == 2:
            change_player_status()
        elif answer == 3:
            add_game()
        elif answer == 4:
            add_accomplishment()
        elif answer == 5:
            add_competition()
        elif answer == 6:
            add_season()
        elif answer == 7:
            clear()
            print("Returned to main menu\n")
            return

        clear()


def list_all_careers():

    print("CAREER LISTING MODE\n\t\t")

    if print_careers() == 0:
        print("No current careers\n")

        while True:
            answer = input("Type Y when ready to clear: ")
            if answer.upper() == "Y":
                break

        clear()
        return
    
    print()
    answer = input("Type Y when ready to clear: ")
    if answer.upper() == "Y":
        clear()
    return

def view_career():
    pass

def set_active_career():
    print("SET ACTIVE CAREER MODE\n\t\t")

    if (num_active_careers == 0):
        print("No current careers\n")
        while True:
            answer = input("Type Y when ready to clear: ")
            if answer.upper() == "Y":
                break
        clear()
        return

    while True:
        print_careers()
        answer = input("\nSelect a valid digit for the career to be selected: ").strip()
        if not re.search(r"^[0-9]+$", answer):
            clear()
            print("Only provide digits")
            continue
        if not os.path.isdir(os.path.join(base_directory, f"career{answer}")):
            clear()
            print("Directory doesn't exist")
            continue

        break

    with open(active_career_file, "w") as f:
        f.write(answer)

    clear()
    print(f"Successfully set active career to '{answer}'\n")
    return


def main():

    clear()
    initial_options = ["Create new career", "Delete old career", "Edit Existing Career", 
    "List All Careers", "View Career", "Set Active Career", "Exit Program"]

    string = "Select an option: \n\n"
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
        if answer == 1:
            create_new_career()
        elif answer == 2:
            delete_old_career()
        elif answer == 3:
            edit_existing_career()
        elif answer == 4:
            list_all_careers()
        elif answer == 5:
            view_career()
        elif answer == 6:
            set_active_career()
        elif answer == 7:
            clear()
            print("Gracefully exiting program")
            sys.exit(0)

            
        

if __name__ == "__main__":
    main()