#Dictionaries of event distance and conversion factors
scy_freestyle_women = {"50": 0.871, "100": 0.874, "200": 0.874, "400": 1.112, "800": 1.120, "1500": 0.975}
scy_freestyle_men = {"50": 0.860, "100": 0.863, "200": 0.865, "400": 1.105, "800": 1.105, "1500": 0.965}
scy_backstroke_women = {"100": 0.853, "200": 0.857}
scy_backstroke_men = {"100": 0.835, "200": 0.849}
scy_breaststroke_women = {"100": 0.870, "200": 0.878}
scy_breaststroke_men = {"100": 0.856, "200": 0.858}
scy_butterfly_women = {"100": 0.877, "200": 0.881}
scy_butterfly_men = {"100": 0.868, "200": 0.866}
scy_medley_women = {"200": 0.867, "400": 0.876}
scy_medley_men = {"200": 0.857, "400": 0.865}
scy_freesyle_relay_women = {"100": 0.874, "200": 0.874}
scy_freesyle_relay_men = {"100": 0.863, "200": 0.867}
scy_medley_relay_women = {"100": 0.868}
scy_medley_relay_men = {"100": 0.856}

#Dictionary connecting event:conversion factor to string title
scy_female = {"freestyle": scy_freestyle_women, "backstroke": scy_backstroke_women, "breaststroke": scy_breaststroke_women, "butterfly": scy_butterfly_women, "medley": scy_medley_women, "freestyle relay": scy_freesyle_relay_women, "medley relay": scy_medley_relay_women}
scy_male = {"freestyle": scy_freestyle_men, "backstroke": scy_backstroke_men, "breaststroke": scy_breaststroke_men, "butterfly": scy_butterfly_men, "medley": scy_medley_men, "freestyle relay": scy_freesyle_relay_men, "medley relay": scy_medley_relay_men}

#Prompt user to insert a stroke
scy_stroke = input("Insert stroke --> ")
while scy_stroke != "freestyle" and scy_stroke != "backstroke" and scy_stroke != "butterfly" and scy_stroke != "breaststroke" and scy_stroke != "medley" and scy_stroke != "freestyle relay" and scy_stroke != "medley relay":
    scy_stroke = input("""You have to insert a stroke from the list:
    - butterfly
    - backstroke
    - breaststroke
    - freestyle
    - medley
    - freestyle relay
    - medley relay
    --> """)

#Prompt user to insert a distance
scy_distance = input("Insert distance --> ")
if scy_stroke == "freestyle":
    while scy_distance != "50" and scy_distance != "100" and scy_distance != "200" and scy_distance != "400" and scy_distance != "800" and scy_distance != "1500":
        scy_distance = input("""Insert a distance from the list:
        - 50
        - 100
        - 200
        - 400
        - 800
        - 1500
        --> """)
elif scy_stroke == "medley":
    while scy_distance != "200" and scy_distance != "400" and scy_distance:
        scy_distance = input("""Insert a distance from the list:
        - 200
        - 400
        --> """)
elif scy_stroke == "freestyle relay":
    while scy_distance != "100" and scy_distance != "200":
        scy_distance = input("""Insert a distance from the list:
        - 100
        - 200
        --> """)
elif scy_stroke == "medley relay":
    scy_distance = "100"
else:
    while scy_distance != "100" and scy_distance != "200" and scy_distance:
        scy_distance = input("""Insert a distance from the list:
        - 100
        - 200
        --> """)

#Prompt user to insert a gender
scy_gender = input("Insert your gender --> ")
while scy_gender != "male" and scy_gender != "female":
    scy_gender = input("""Insert a gender from the list:
    - male
    - female
    --> """)

#Prompt user for a time to be converted
#Minutes
scy_minutes = input("Insert minutes --> ")
try:
    int(scy_minutes)
    it_is = True
except ValueError:
    it_is = False
while it_is == False:
    scy_minutes = input("Insert minutes in the form of an integer --> ")
    try:
        int(scy_minutes)
        it_is = True
    except ValueError:
        it_is = False
#Seconds
scy_seconds = input("Insert seconds --> ")
try:
    int(scy_seconds)
    it_is = True
except ValueError:
    it_is = False
while it_is == False:
    scy_seconds = input("Insert seconds in the form of an integer --> ")
    try:
        int(scy_seconds)
        it_is = True
    except ValueError:
        it_is = False
#Hundreds
scy_hundreds = input("Insert hundreds --> ")
try:
    int(scy_hundreds)
    it_is = True
except ValueError:
    it_is = False
while it_is == False:
    scy_hundreds = input("Insert hundreds in the form of an integer --> ")
    try:
        int(scy_hundreds)
        it_is = True
    except ValueError:
        it_is = False

#Convert time into seconds
scy_min_sec = int(scy_minutes) * 60
scy_hun_sec = int(scy_hundreds) * 0.01
scy_time = int(scy_min_sec) + int(scy_seconds) + scy_hun_sec

##Convert from SCY to LCM
scy_event = {}
if scy_gender == "male":
    scy_event = scy_male
else:
    scy_event = scy_female

scy_base = scy_event[scy_stroke]
scy_basetime = scy_base[scy_distance]

lcm_time = scy_time / scy_basetime

#Convert time from seconds-format to minute-format
lcm_minutes = int(int(lcm_time)/60)

lcm_time -= lcm_minutes * 60

lcm_seconds = int(lcm_time)

lcm_time -= lcm_seconds

lcm_time = lcm_time * 100

lcm_hundreds = int(lcm_time)

lcm_hundreds = lcm_hundreds/100 

lcm_seconds += lcm_hundreds

if lcm_seconds < 10:
    lcm_seconds = "0" + str(lcm_seconds)

#Print output
if lcm_minutes > 0 and scy_distance != "500" and scy_distance != "1000" and scy_distance != "1650":
    print("Your " + scy_distance + " yards time is estimated to be equal to " + str(lcm_minutes) + "," + str(lcm_seconds) + " in long course meters")
elif scy_distance != "500" and scy_distance != "1000" and scy_distance != "1650":
    print("Your " + scy_distance + " yards short course time is estimated to be equal to " + str(lcm_seconds) + " in long course meters")
elif scy_distance == "500":
    print("A 500 yard race is usually compared to a 400 meter race")
    print("Your 500 yard short course time is estimated to be equal to " + str(lcm_minutes) + "," + str(lcm_seconds) + " for a 400m long course event")
elif scy_distance == "1000":
    print("A 1000 yard race is usually compared to a 800 meter race")
    print("Your 1000 yard short course time is estimated to be equal to " + str(lcm_minutes) + "," + str(lcm_seconds) + " for a 800m long course event")
elif scy_distance == "1650":
    print("A 1650 yard race is usually compared to a 1500 meter race")
    print("Your 1650 yard short course time is estimated to be equal to " + str(lcm_minutes) + "," + str(lcm_seconds) + " for a 1500m long course event")

quit = input("Press enter to exit the program")