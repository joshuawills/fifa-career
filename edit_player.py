#!/usr/bin/env python3

import time 
import sys, os, glob, subprocess, re
from utilities import clear, base_directory, active_career_file, get_career_directory, get_competitions, get_players, get_accomplishments, get_seasons

def add_player():
  clear()

  print("Welcome to the add player feature!")

  name = input("NAME (surname, firstname)\n\t-> ")
  dob = input("DOB (dd/mm/yyyy)\n\t-> ")
  date_of_transfer = input("DATE ACQUIRED (dd/mm/yyyy)\n\t-> ")
  position = input("POSITION\n\t-> ")
  source = input("PREVIOUS CLUB\n\t-> ")
  wage = input("WAGE\n\t-> ")
  transfer_fee = input("TRANSFER FEE\n\t-> ")
  player_add_ons = input("OTHER CONDITIONS\n\t-> ")

  x = -1
  with open(active_career_file, "r") as f:
    x = f.readlines()[0].strip()

  career_directory = os.path.join(get_career_directory(), "players")
  answer = input("\nAre you sure you want to add this player? (Y/N) ")

  if answer.strip().upper() != "Y":
    print("Gracefully exiting early")
    return

  with open(os.path.join(career_directory, name.split(',')[0].strip().upper()), "w") as f:
    f.write(f"NAME: {name.strip()}\n")
    f.write(f"DOB: {dob.strip()}\n")
    f.write(f"DATE OF SIGNING: {date_of_transfer.strip()}\n")
    f.write(f"POSITION: {position.strip()}\n")
    f.write(f"SOURCE: {source.strip()}\n")
    f.write(f"WAGE: {wage.strip()}\n")
    f.write(f"TRANSFER FEE: {transfer_fee.strip()}\n")
    f.write(f"PLAYER ADD ONS: {player_add_ons.strip()}\n")
    f.write(f"STATUS: ACTIVE\n")


  print("Player succesfully logged to the database")
  return

def change_player_status():
  
  clear()

  print("Welcome to the change player status")
  print("First select, the player whose status you want to change: \n\n")

  career_directory = os.path.join(get_career_directory(), "players")
  players = get_players()
  print(', '.join(players))

  answer = input("Type the name of one of the above players? ")
  while  answer.strip() not in files:
    print("Invalid name, try again.")
    answer = input("Type the name of one of the above players? ")

  options = ["WAGE", "STATUS (active|retired|sold)", "Return to previous menu"]
  string = "Select an option: \n\n"
  for i, x in enumerate(options):
      string += f"\t[{i+1}]: {x}\n"
  string += "\n"

  while True:
    x = int(input(string))
    if x == 1:
      new_wage = input("\nWhat is the new wage? ")
      current_state = []
      with open(os.path.join(career_directory, answer.upper()), "r") as f:
        current_state = f.readlines()

      for n, x in enumerate(current_state):
        if x.startswith("WAGE:"):
          current_state[n] = f"WAGE: {new_wage}\n"

      with open(os.path.join(career_directory, answer.upper()), "w") as f:
        for x in current_state:
          f.write(x)

    elif x == 2:

      new_status = input("\nWhat is the new status? ")
      with open(os.path.join(career_directory, answer.upper()), "r") as f:
        current_state = f.readlines()

      for n, x in enumerate(current_state):
        if x.startswith("STATUS:"):
          current_state[n] = f"STATUS: {new_status.upper()}\n"

      with open(os.path.join(career_directory, answer.upper()), "w") as f:
        for x in current_state:
          f.write(x)

    elif x == 3:
      return 


def add_game():
  clear()
  print("Welcome to the add game section\n")

  seasons = ", ".join([x.strip() for x in get_seasons()])
  season_selection = input(f"Select seasons: {seasons}\n\t-> ")

  competition = ", ".join([x.strip() for x in get_competitions()])
  competition_selection = input(f"Select competition: {competition}\n\t-> ")

  opponent = input("Select opponent:\n\t-> ")
  home_or_away = input("H or A:\n\t-> ")


  

def add_accomplishment():
  clear()
  print("Welcome to the add accomplishements status\n")
  print("Here are all your current accomplishments registered\n")
  current_accomplishments = get_accomplishments()
  print("".join(current_accomplishments))

  while True:
    x = input("What is the new accomplishement you want to register? (sesason:trophy) (EXIT to leave) ")

    if x.upper() == "EXIT":
      with open(os.path.join(get_career_directory(), "accomplishments"), "w") as f:
        for x in current_accomplishments:
          f.write(x)
      return

    current_accomplishments.append(x.strip() + "\n")


def add_season():
  clear()
  print("Welcome to the add seasons status\n")
  print("Here are all your current seasons registered:")

  current_seasons = get_seasons()
  print("".join(current_seasons))

  while True:
    x = input("What is the new season you want to register? (EXIT to leave) ")

    if x.upper() == "EXIT":

      with open(os.path.join(get_career_directory(), "seasons"), "w") as f:
        for x in current_seasons:
          f.write(x)

      return

    current_seasons.append(x.strip() + "\n")

def add_competition():

  clear()
  print("Welcome to the add competitions status\n")
  print("Here are all your current competitions registered:")
  current_competitions = get_competitions()
  print("".join(current_competitions))

  while True:
    x = input("What is the new competition you want to register? (EXIT to leave) ")

    if x.upper() == "EXIT":

      with open(os.path.join(get_career_directory(), "competitions"), "w") as f:
        for x in current_competitions:
          f.write(x)

      return

    current_competitions.append(x.strip() + "\n")
    

