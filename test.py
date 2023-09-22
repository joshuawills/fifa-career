#!/usr/bin/env python3

import os, re
from utilities import get_career_directory

seasons_directory = os.path.join(get_career_directory(), "seasons")
current_season = os.path.join(seasons_directory, "22")

for x in os.listdir(current_season):
    print(x)

fresh_competition = "la liga  ".strip().upper()
regex = fr"^{fresh_competition}"
counter = len([x for x in os.listdir(current_season) if re.search(regex, x)])
print(counter)
