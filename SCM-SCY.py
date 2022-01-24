#Dictionary of event distance and conversion factors
scm_conversion_factors = {"400": 1.143, "800": 1.143, "1500": 1.003, "else": 0.896}

#Prompt user to insetrt distance of event
scm_distance = input("Insert the SCM-distance to be converted into SCY --> ")
while scm_distance != "50" and scm_distance != "100" and scm_distance != "200" and scm_distance != "400" and scm_distance != "800" and scm_distance != "1500":
    scm_distance = input("""Please insert a SCM-distance from the list below:
    - 50
    - 100
    - 200
    - 400
    - 800
    - 1500
    --> """)

#Prompt user to insert time to be converted
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

#Convert from SCM to SCY
if scm_distance == "400" or scm_distance == "800" or scm_distance == "1500":
    scy_time = scm_time * scm_conversion_factors[scm_distance]
else:
    scy_time = scm_time * scm_conversion_factors["else"]

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
if scy_minutes > 0 and scm_distance != "400" and scm_distance != "800" and scm_distance != "1500":
    print("Your time is estimated to be equal to " + str(scy_minutes) + "," + str(scy_seconds) + " in yards")
elif scm_distance != "400" and scm_distance != "800" and scm_distance != "1500":
    print("Your time is estimated to be equal to " + str(scy_seconds) + " in yards")
elif scm_distance == "400":
    print("A 400 meter race is usually compared to a 500 yard race")
    print("Your 400m time is estimated to be equal to " + str(scy_minutes) + "," + str(scy_seconds) + " for a 500 yard event")
elif scm_distance == "800":
    print("A 800 meter race is usually compared to a 1000 yard race")
    print("Your 800m time is estimated to be equal to " + str(scy_minutes) + "," + str(scy_seconds) + " for a 1000 yard event")
elif scm_distance == "1500":
    print("A 1500 meter race is usually compared to a 1650 yard race")
    print("Your 1500m time is estimated to be equal to " + str(scy_minutes) + "," + str(scy_seconds) + " for a 1650 yard event")

quit = input("Press enter to exit the program")