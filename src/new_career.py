#!/usr/bin/env python3

import sys, os, subprocess, re
from src.utilities import clear, base_directory, count_file

def create_new_career():

    print("CAREER CREATION MODE\n")

    name_career = input("CAREER NAME:\n\t-> ")
    club_career = input("CLUB:\n\t-> ")
    league_career = input("LEAGUE:\n\t-> ")
    league_season = input("STARTING SEASON:\n\t-> ")
    manager_name = input("MANAGER NAME:\n\t-> ")

    with open(count_file, "r") as f:
        x = f.readlines()[0].strip()

    career_directory = os.path.join(base_directory, f"career{x}")
    try:
        subprocess.run(["mkdir", career_directory], check=True)
        players_directory = os.path.join(career_directory, "players")
        subprocess.run(["mkdir", players_directory], check=True)
        seasons_directory = os.path.join(career_directory, "seasons")
        subprocess.run(["mkdir", seasons_directory], check=True)
        first_season = os.path.join(seasons_directory, league_season.strip().split("/")[1])
        subprocess.run(["mkdir", first_season], check=True)
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

        with open(os.path.join(career_directory, "availableSeasons"), "w") as f:
            f.write(f"{league_season.strip()}\n")

        with open(os.path.join(career_directory, "accomplishments"), "w") as f:
            f.write("")

        clear()

        print("Successfully created new career\n")
    except subprocess.CalledProcessError as e:
        print("Something failed when creating directories", e)
        sys.exit(1)

    return