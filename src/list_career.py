#!/usr/bin/env python3

from src.utilities import clear, print_careers

def list_all_careers():
    print("CAREER LISTING MODE\n")
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