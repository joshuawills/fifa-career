#!/usr/bin/env python3

from src.utilities import clear, print_careers, num_active_careers, base_directory, active_career_file

def set_active_career():
    print("SET ACTIVE CAREER MODE\n\t\t")

    if (num_active_careers == 0):
        print("NO CURRENT CAREERS\n")
        while True:
            answer = input("Type Y when ready to clear: ")
            if answer.upper() == "Y":
                break
        clear()
        return

    while True:
        print_careers()
        answer = input("\nSELECT VALID DIGIT: (EXIT)\n\t-> ").strip()

        if answer.upper() == "EXIT": break

        if not re.search(r"^[0-9]+$", answer):
            clear()
            print("ONLY PROVIDE DIGITS")
            continue
        if not os.path.isdir(os.path.join(base_directory, f"career{answer}")):
            clear()
            print("NON-EXISTENT DIRECTORY")
            continue

        break

    with open(active_career_file, "w") as f:
        f.write(answer)

    clear()
    print(f"NEW ACTIVE CAREER: '{answer}'\n")
    return