#Dictionaries of event distance and LCM conversion factors
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

#Dictionary of event distance and SCM conversion factors
scm_conversion_factors = {"400": 1.143, "800": 1.143, "1500": 1.003, "else": 0.896}

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
scm_distance = input("Insert distance --> ")
if lcm_stroke == "freestyle":
    while scm_distance != "50" and scm_distance != "100" and scm_distance != "200" and scm_distance != "400" and scm_distance != "800" and scm_distance != "1500":
        scm_distance = input("""Insert a distance from the list:
        - 50
        - 100
        - 200
        - 400
        - 800
        - 1500
        --> """)
elif lcm_stroke == "medley":
    while scm_distance != "200" and scm_distance != "400" and scm_distance:
        scm_distance = input("""Insert a distance from the list:
        - 200
        - 400
        --> """)
elif lcm_stroke == "freestyle relay":
    while scm_distance != "100" and scm_distance != "200":
        scm_distance = input("""Insert a distance from the list:
        - 100
        - 200
        --> """)
elif lcm_stroke == "medley relay":
    scm_distance = "100"
else:
    while scm_distance != "100" and scm_distance != "200" and scm_distance:
        scm_distance = input("""Insert a distance from the list:
        - 100
        - 200
        --> """)

lcm_distance = scm_distance

#Prompt user to insert a gender
lcm_gender = input("Insert your gender --> ")
while lcm_gender != "male" and lcm_gender != "female":
    lcm_gender = input("""Insert a gender from the list:
    - male
    - female
    --> """)

#Prompt user for a time to be converted
#Minutes
scm_minutes = input("Insert minutes --> ")
try:
    int(scm_minutes)
    it_is = True
except ValueError:
    it_is = False
while it_is == False:
    scm_minutes = input("Insert minutes in the form of an integer --> ")
    try:
        int(scm_minutes)
        it_is = True
    except ValueError:
        it_is = False
#Seconds
scm_seconds = input("Insert seconds --> ")
try:
    int(scm_seconds)
    it_is = True
except ValueError:
    it_is = False
while it_is == False:
    scm_seconds = input("Insert seconds in the form of an integer --> ")
    try:
        int(scm_seconds)
        it_is = True
    except ValueError:
        it_is = False
#Hundreds
scm_hundreds = input("Insert hundreds --> ")
try:
    int(scm_hundreds)
    it_is = True
except ValueError:
    it_is = False
while it_is == False:
    scm_hundreds = input("Insert hundreds in the form of an integer --> ")
    try:
        int(scm_hundreds)
        it_is = True
    except ValueError:
        it_is = False

#Convert time into seconds
scm_min_sec = int(scm_minutes) * 60
scm_hun_sec = int(scm_hundreds) * 0.01
scm_time = int(scm_min_sec) + int(scm_seconds) + scm_hun_sec

#Convert from SCM to LCM
if scm_distance == "400" or scm_distance == "800" or scm_distance == "1500":
    temp_time = scm_time * scm_conversion_factors[scm_distance]
else:
    temp_time = scm_time * scm_conversion_factors["else"]

lcm_event = {}
if lcm_gender == "male":
    lcm_event = lcm_male
else:
    lcm_event = lcm_female

lcm_base = lcm_event[lcm_stroke]
lcm_basetime = lcm_base[lcm_distance]

lcm_time = temp_time * lcm_basetime

if scm_minutes > 0 and lcm_distance != "400" and lcm_distance != "800" and lcm_distance != "1500":
    print("Your " + lcm_distance + " short course meters time is estimated to be equal to " + str(scm_minutes) + "," + str(scm_seconds) + " in long course meters")
elif lcm_distance != "400" and lcm_distance != "800" and lcm_distance != "1500":
    print("Your " + lcm_distance + " short course meters time is estimated to be equal to " + str(scm_seconds) + " in long course meters")
elif lcm_distance == "400":
    print("Your 400 meter short course time is estimated to be equal to " + str(scm_minutes) + "," + str(scm_seconds) + " in long course meters")
elif lcm_distance == "800":
    print("Your 800 meter short course time is estimated to be equal to " + str(scm_minutes) + "," + str(scm_seconds) + " in long course meters")
elif lcm_distance == "1500":
    print("Your 1500 meter short course time is estimated to be equal to " + str(scm_minutes) + "," + str(scm_seconds) + " in long course meters")

quit = input("Press enter to exit the program")