# Dictionaries of events and short course base times
sc_freestyle_women = {"50": 22.93, "100": 50.25, "200": 110.43, "400": 233.92, "800": 479.34, "1500": 918.01}
sc_freestyle_men = {"50": 20.24, "100": 44.94, "200": 99.37, "400": 212.25, "800": 443.42, "1500": 848.06}
sc_backstroke_women = {"50": 25.67, "100": 54.89, "200": 119.23}
sc_backstroke_men = {"50": 22.22, "100": 48.88, "200": 105.63}
sc_breaststroke_women = {"50": 28.56, "100": 62.36, "200": 134.57}
sc_breaststroke_men = {"50": 25.25, "100": 55.61, "200": 120.16}
sc_butterfly_women = {"50": 24.38, "100": 54.61, "200": 119.61}
sc_butterfly_men = {"50": 21.75, "100": 48.08, "200": 108.24}
sc_medley_women = {"100": 56.51, "200": 121.86, "400": 258.94}
sc_medley_men = {"100": 50.26, "200": 109.63, "400": 234.81}
sc_freesyle_relay_women = {"50":93.91, "100": 206.53, "200": 452.85}
sc_freesyle_relay_men = {"50": 81.80, "100": 183.03, "200": 406.81}
sc_4x50_medley_women = {"50": 102.38, "100": 225.20}
sc_4x50_medley_men = {"50": 90.44, "100": 199.16}

#Dictionaries connecting event:basetime to string title
sc_female = {"freestyle": sc_freestyle_women, "backstroke": sc_backstroke_women, "breaststroke": sc_breaststroke_women, "butterfly": sc_butterfly_women, "medley": sc_medley_women, "freestyle relay": sc_freesyle_relay_women, "medley relay": sc_4x50_medley_women}
sc_male = {"freestyle": sc_freestyle_men, "backstroke": sc_backstroke_men, "breaststroke": sc_breaststroke_men, "butterfly": sc_butterfly_men, "medley": sc_medley_men, "freestyle relay": sc_freesyle_relay_men, "medley relay": sc_4x50_medley_men}

#Prompt user to insert a stroke
sc_stroke = input("Insert stroke --> ")
while sc_stroke != "freestyle" and sc_stroke != "backstroke" and sc_stroke != "butterfly" and sc_stroke != "breaststroke" and sc_stroke != "medley" and sc_stroke != "freestyle_relay" and sc_stroke != "medley_relay":
    sc_stroke = input("""You have to insert a stroke from the list:
    - butterfly
    - backstroke
    - breaststroke
    - freestyle
    - medley
    - freestyle relay
    - medley relay
    --> """)

#Prompt user to insert a distance
sc_distance = input("Insert distance --> ")
if sc_stroke == "freestyle":
    while sc_distance != "50" and sc_distance != "100" and sc_distance != "200" and sc_distance != "400" and sc_distance != "800" and sc_distance != "1500":
        sc_distance = input("""Insert a distance from the list:
        - 50
        - 100
        - 200
        - 400
        - 800
        - 1500
        --> """)
elif sc_stroke == "medley":
    while sc_distance != "100" and sc_distance != "200" and sc_distance != "400" and sc_distance:
        sc_distance = input("""Insert a distance from the list:
        - 100
        - 200
        - 400
        --> """)
else:
    while sc_distance != "50" and sc_distance != "100" and sc_distance != "200" and sc_distance:
        sc_distance = input("""Insert a distance from the list:
        - 50
        - 100
        - 200
        --> """)

#Prompt user to insert a gender
sc_gender = input("Insert your gender --> ")
while sc_gender != "male" and sc_gender != "female":
    sc_gender = input("""Insert a gender from the list:
    - male
    - female
    --> """)

#Prompt user for a time to be converted
#Minutes
sc_minutes = input("Insert minutes --> ")
try:
    int(sc_minutes)
    it_is = True
except ValueError:
    it_is = False
while it_is == False:
    sc_minutes = input("Insert minutes in the form of an integer --> ")
    try:
        int(sc_minutes)
        it_is = True
    except ValueError:
        it_is = False
#Seconds
sc_seconds = input("Insert seconds --> ")
try:
    int(sc_seconds)
    it_is = True
except ValueError:
    it_is = False
while it_is == False:
    sc_seconds = input("Insert seconds in the form of an integer --> ")
    try:
        int(sc_seconds)
        it_is = True
    except ValueError:
        it_is = False
#Hundreds
sc_hundreds = input("Insert hundreds --> ")
try:
    int(sc_hundreds)
    it_is = True
except ValueError:
    it_is = False
while it_is == False:
    sc_hundreds = input("Insert hundreds in the form of an integer --> ")
    try:
        int(sc_hundreds)
        it_is = True
    except ValueError:
        it_is = False

#Convert time into seconds
sc_min_sec = int(sc_minutes) * 60
sc_hun_sec = int(sc_hundreds) * 0.01
sc_time = int(sc_min_sec) + int(sc_seconds) + sc_hun_sec

#Calculate points from time
sc_event = {}
if sc_gender == "male":
    sc_event = sc_male
else:
    sc_event = sc_female

sc_base = sc_event[sc_stroke]
sc_basetime = sc_base[sc_distance]

sc_points = int(1000*(sc_basetime/int(sc_time))**3)

print(sc_points)

quit = input("Press enter to exit the program")
