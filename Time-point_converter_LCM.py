# Dictionaries of events and long course base times
lc_freestyle_women = {"50": 23.67, "100": 51.71, "200": 112.98, "400": 236.46, "800": 484.79, "1500": 920.48}
lc_freestyle_men = {"50": 20.91, "100": 46.91, "200": 102.00, "400": 220.07, "800": 452.12, "1500": 871.02}
lc_backstroke_women = {"50": 26.98, "100": 57.57, "200": 123.35}
lc_backstroke_men = {"50": 24.00, "100": 51.85, "200": 111.92}
lc_breaststroke_women = {"50": 29.40, "100": 64.13, "200": 139.11}
lc_breaststroke_men = {"50": 25.95, "100": 56.88, "200": 126.12}
lc_butterfly_women = {"50": 24.43, "100": 55.48, "200": 121.81}
lc_butterfly_men = {"50": 22.27, "100": 49.50, "200": 110.73}
lc_medley_women = {"200": 126.12, "400": 266.36}
lc_medley_men = {"200": 114.00, "400": 243.84}
lc_freesyle_relay_women = {"100": 210.05, "200": 461.50}
lc_freesyle_relay_men = {"100": 188.24, "200": 418.24}
lc_medley_relay_women = {"100": 230.40}
lc_medley_relay_men = {"100": 207.28}

#Dictionaries connecting event:basetime to string title
lc_female = {"freestyle": lc_freestyle_women, "backstroke": lc_backstroke_women, "breaststroke": lc_breaststroke_women, "butterfly": lc_butterfly_women, "medley": lc_medley_women, "freestyle relay": lc_freesyle_relay_women, "medley relay": lc_medley_relay_women}
lc_male = {"freestyle": lc_freestyle_men, "backstroke": lc_backstroke_men, "breaststroke": lc_breaststroke_men, "butterfly": lc_butterfly_men, "medley": lc_medley_men, "freestyle relay": lc_freesyle_relay_men, "medley relay": lc_medley_relay_men}

#Prompt user to insert a stroke
lc_stroke = input("Insert stroke --> ")
while lc_stroke != "freestyle" and lc_stroke != "backstroke" and lc_stroke != "butterfly" and lc_stroke != "breaststroke" and lc_stroke != "medley" and lc_stroke != "freestyle relay" and lc_stroke != "medley relay":
    lc_stroke = input("""You have to insert a stroke from the list:
    - butterfly
    - backstroke
    - breaststroke
    - freestyle
    - medley
    - freestyle relay
    - medley relay
    --> """)

#Prompt user to insert a distance
lc_distance = input("Insert distance --> ")
if lc_stroke == "freestyle":
    while lc_distance != "50" and lc_distance != "100" and lc_distance != "200" and lc_distance != "400" and lc_distance != "800" and lc_distance != "1500":
        lc_distance = input("""Insert a distance from the list:
        - 50
        - 100
        - 200
        - 400
        - 800
        - 1500
        --> """)
elif lc_stroke == "medley":
    while lc_distance != "200" and lc_distance != "400" and lc_distance:
        lc_distance = input("""Insert a distance from the list:
        - 200
        - 400
        --> """)
elif lc_stroke == "freestyle relay":
    while lc_distance != "100" and lc_distance != "200":
        lc_distance = input("""Insert a distance from the list:
        - 100
        - 200
        --> """)
elif lc_stroke == "medley relay":
    lc_distance = "100"
else:
    while lc_distance != "50" and lc_distance != "100" and lc_distance != "200" and lc_distance:
        lc_distance = input("""Insert a distance from the list:
        - 50
        - 100
        - 200
        --> """)

#Prompt user to insert a gender
lc_gender = input("Insert your gender --> ")
while lc_gender != "male" and lc_gender != "female":
    lc_gender = input("""Insert a gender from the list:
    - male
    - female
    --> """)

#Prompt user for a time to be converted
#Minutes
lc_minutes = input("Insert minutes --> ")
try:
    int(lc_minutes)
    it_is = True
except ValueError:
    it_is = False
while it_is == False:
    lc_minutes = input("Insert minutes in the form of an integer --> ")
    try:
        int(lc_minutes)
        it_is = True
    except ValueError:
        it_is = False
#Seconds
lc_seconds = input("Insert seconds --> ")
try:
    int(lc_seconds)
    it_is = True
except ValueError:
    it_is = False
while it_is == False:
    lc_seconds = input("Insert seconds in the form of an integer --> ")
    try:
        int(lc_seconds)
        it_is = True
    except ValueError:
        it_is = False
#Hundreds
lc_hundreds = input("Insert hundreds --> ")
try:
    int(lc_hundreds)
    it_is = True
except ValueError:
    it_is = False
while it_is == False:
    lc_hundreds = input("Insert hundreds in the form of an integer --> ")
    try:
        int(lc_hundreds)
        it_is = True
    except ValueError:
        it_is = False

#Convert time into seconds
lc_min_sec = int(lc_minutes) * 60
lc_hun_sec = int(lc_hundreds) * 0.01
lc_time = int(lc_min_sec) + int(lc_seconds) + lc_hun_sec

#Calculate points from time
lc_event = {}
if lc_gender == "male":
    lc_event = lc_male
else:
    lc_event = lc_female

lc_base = lc_event[lc_stroke]
lc_basetime = lc_base[lc_distance]

lc_points = int(1000*(lc_basetime/float(lc_time))**3)

print(lc_points)

quit = input("Press enter to exit the program")
