#!/usr/bin/env python3

import time, subprocess, os, re
from src.utilities import clear, base_directory, active_career_file, print_careers

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