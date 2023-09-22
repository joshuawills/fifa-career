#!/usr/bin/env python3

import sys, os, glob, subprocess, re


global base_directory, count_file, active_career_file
base_directory = os.path.expanduser("~/.fifacareer")
count_file = os.path.join(base_directory, "careerCount")
active_career_file = os.path.join(base_directory, "activeCareer")


def clear():
    os.system("clear" if os.name == "posix" else "cls")

def num_active_careers():
	return len([f for f in os.listdir(base_directory) if os.path.isdir(os.path.join(base_directory, f))])

def print_careers():

	careers = [f for f in os.listdir(base_directory) if os.path.isdir(os.path.join(base_directory, f))]

	for i, x in enumerate(careers):
		print(f"\nCareer Number {i}:")

		career_directory = os.path.join(base_directory, x)
		print("\t", end="")
		with open(os.path.join(career_directory, "keyInfo"), "r") as f:
			data = [x.strip() for x in f.readlines()]
			print("\n\t".join(data))

	return len(careers)

def get_career_directory():
	x = -1
	with open(active_career_file, "r") as f:
		x = f.readlines()[0].strip()
	return os.path.join(base_directory, f"career{x}")

def get_competitions():
	with open(os.path.join(get_career_directory(), "competitions"), "r") as f:
		current_competitions = f.readlines()

	return current_competitions

def get_accomplishments():
	with open(os.path.join(get_career_directory(), "accomplishments"), "r") as f:
		accomplishments = f.readlines()

	return accomplishments

def get_players():
  career_directory = os.path.join(get_career_directory(), "players")
  return [f for f in os.listdir(career_directory) if os.path.isfile(os.path.join(career_directory, f))] 

def get_seasons():
	with open(os.path.join(get_career_directory(), "availableSeasons"), "r") as f:
		current_seasons = f.readlines()
	return current_seasons