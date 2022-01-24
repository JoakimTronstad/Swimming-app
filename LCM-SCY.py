#Dictionaries of event distance and conversion factors
lcm_freestyle_women = {"50": 0.871, "100": 0.874, "200": 0.874, "400": 1.112, "800": 1.120, "1500": 0.975}
lcm_freestyle_men = {"50": 0.860, "100": 0.863, "200": 0.865, "400": 1.105, "800": 1.105, "1500": 0.965}
lcm_backstroke_women = {"100": 0.853, "200": 0.857}
lcm_backstroke_men = {"100": 0.835, "200": 0.849}
lcm_breaststroke_women = {"100": 0.870, "200": 0.878}
lcm_breaststroke_men = {"100": 0.856, "200": 0.858}
lcm_butterfly_women = {"100": 0.877, "200": 0.881}
lcm_butterfly_men = {"100": 0.868, "200": 0.866}
lcm_medley_women = {"200": 0.867, "400": 0.876}
lcm_medley_men = {"200": 0.857, "400": 0.865}
lcm_freesyle_relay_women = {"100": 0.874, "200": 0.874}
lcm_freesyle_relay_men = {"100": 0.863, "200": 0.867}
lcm_medley_relay_women = {"100": 0.868}
lcm_medley_relay_men = {"100": 0.856}

#Dictionary connecting event:conversion factor to string title
lcm_female = {"freestyle": lcm_freestyle_women, "backstroke": lcm_backstroke_women, "breaststroke": lcm_breaststroke_women, "butterfly": lcm_butterfly_women, "medley": lcm_medley_women, "freestyle relay": lcm_freesyle_relay_women, "medley relay": lcm_medley_relay_women}
lcm_male = {"freestyle": lcm_freestyle_men, "backstroke": lcm_backstroke_men, "breaststroke": lcm_breaststroke_men, "butterfly": lcm_butterfly_men, "medley": lcm_medley_men, "freestyle relay": lcm_freesyle_relay_men, "medley relay": lcm_medley_relay_men}

#Prompt user to insert a stroke
lcm_stroke = input("Insert stroke --> ")
while lcm_stroke != "freestyle" and lcm_stroke != "backstroke" and lcm_stroke != "butterfly" and lcm_stroke != "breaststroke" and lcm_stroke != "medley" and lcm_stroke != "freestyle relay" and lcm_stroke != "medley relay":
    lcm_stroke = input("""You have to insert a stroke from the list:
    - butterfly
    - backstroke
    - breaststroke
    - freestyle
    - medley
    - freestyle relay
    - medley relay
    --> """)

#Prompt user to insert a distance
lcm_distance = input("Insert distance --> ")
if lcm_stroke == "freestyle":
    while lcm_distance != "50" and lcm_distance != "100" and lcm_distance != "200" and lcm_distance != "400" and lcm_distance != "800" and lcm_distance != "1500":
        lcm_distance = input("""Insert a distance from the list:
        - 50
        - 100
        - 200
        - 400
        - 800
        - 1500
        --> """)
elif lcm_stroke == "medley":
    while lcm_distance != "200" and lcm_distance != "400" and lcm_distance:
        lcm_distance = input("""Insert a distance from the list:
        - 200
        - 400
        --> """)
elif lcm_stroke == "freestyle relay":
    while lcm_distance != "100" and lcm_distance != "200":
        lcm_distance = input("""Insert a distance from the list:
        - 100
        - 200
        --> """)
elif lcm_stroke == "medley relay":
    lcm_distance = "100"
else:
    while lcm_distance != "100" and lcm_distance != "200" and lcm_distance:
        lcm_distance = input("""Insert a distance from the list:
        - 100
        - 200
        --> """)

#Prompt user to insert a gender
lcm_gender = input("Insert your gender --> ")
while lcm_gender != "male" and lcm_gender != "female":
    lcm_gender = input("""Insert a gender from the list:
    - male
    - female
    --> """)

#Prompt user for a time to be converted
#Minutes
lcm_minutes = input("Insert minutes --> ")
try:
    int(lcm_minutes)
    it_is = True
except ValueError:
    it_is = False
while it_is == False:
    lcm_minutes = input("Insert minutes in the form of an integer --> ")
    try:
        int(lcm_minutes)
        it_is = True
    except ValueError:
        it_is = False
#Seconds
lcm_seconds = input("Insert seconds --> ")
try:
    int(lcm_seconds)
    it_is = True
except ValueError:
    it_is = False
while it_is == False:
    lcm_seconds = input("Insert seconds in the form of an integer --> ")
    try:
        int(lcm_seconds)
        it_is = True
    except ValueError:
        it_is = False
#Hundreds
lcm_hundreds = input("Insert hundreds --> ")
try:
    int(lcm_hundreds)
    it_is = True
except ValueError:
    it_is = False
while it_is == False:
    lcm_hundreds = input("Insert hundreds in the form of an integer --> ")
    try:
        int(lcm_hundreds)
        it_is = True
    except ValueError:
        it_is = False

#Convert time into seconds
lcm_min_sec = int(lcm_minutes) * 60
lcm_hun_sec = int(lcm_hundreds) * 0.01
lcm_time = int(lcm_min_sec) + int(lcm_seconds) + lcm_hun_sec

#Convert from LCM to SCY
lcm_event = {}
if lcm_gender == "male":
    lcm_event = lcm_male
else:
    lcm_event = lcm_female

lcm_base = lcm_event[lcm_stroke]
lcm_basetime = lcm_base[lcm_distance]

scy_time = lcm_time * lcm_basetime

#Convert time from seconds-format to minute-format
scy_minutes = int(int(scy_time)/60)

scy_time -= scy_minutes * 60

scy_seconds = int(scy_time)

scy_time -= scy_seconds

scy_time = scy_time * 100

scy_hundreds = int(scy_time)

scy_hundreds = scy_hundreds/100 

scy_seconds += scy_hundreds

if scy_seconds < 10:
    scy_seconds = "0" + str(scy_seconds)

#Print output
if scy_minutes > 0 and lcm_distance != "400" and lcm_distance != "800" and lcm_distance != "1500":
    print("Your long course meters time is estimated to be equal to " + str(scy_minutes) + "," + str(scy_seconds) + " in short course yards")
elif lcm_distance != "400" and lcm_distance != "800" and lcm_distance != "1500":
    print("Your long course meters time is estimated to be equal to " + str(scy_seconds) + " in yards")
elif lcm_distance == "400":
    print("A 400 meter race is usually compared to a 500 yard race")
    print("Your 400m long course time is estimated to be equal to " + str(scy_minutes) + "," + str(scy_seconds) + " for a 500 yard short course event")
elif lcm_distance == "800":
    print("A 800 meter race is usually compared to a 1000 yard race")
    print("Your 800m long course time is estimated to be equal to " + str(scy_minutes) + "," + str(scy_seconds) + " for a 1000 yard short course event")
elif lcm_distance == "1500":
    print("A 1500 meter race is usually compared to a 1650 yard race")
    print("Your 1500m long course time is estimated to be equal to " + str(scy_minutes) + "," + str(scy_seconds) + " for a 1650 yard short course event")

quit = input("Press enter to exit the program")