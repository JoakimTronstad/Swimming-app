#Dictionary of event distance and conversion factors
scy_conversion_factors = {"500": 1.143, "1000": 1.143, "1650": 1.003, "else": 0.896}

#Prompt user to insetrt distance of event
scy_distance = input("Insert the SCY-distance to be converted into SCM --> ")
while scy_distance != "50" and scy_distance != "100" and scy_distance != "200" and scy_distance != "500" and scy_distance != "1000" and scy_distance != "1650":
    scy_distance = input("""Please insert a SCY-distance from the list below:
    - 50
    - 100
    - 200
    - 500
    - 1000
    - 1650
    --> """)

#Prompt user to insert time to be converted
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

#Convert from SCY to SCM
if scy_distance == "500" or scy_distance == "1000" or scy_distance == "1650":
    scm_time = scy_time / scy_conversion_factors[scy_distance]
else:
    scm_time = scy_time / scy_conversion_factors["else"]

#Convert time from seconds-format to minute-format
scm_minutes = int(int(scm_time)/60)

scm_time -= scm_minutes * 60

scm_seconds = int(scm_time)

scm_time -= scm_seconds

scm_time = scm_time * 100

scm_hundreds = int(scm_time)

scm_hundreds = scm_hundreds/100 

scm_seconds += scm_hundreds

if scm_seconds < 10:
    scm_seconds = "0" + str(scm_seconds)

#Print output
if scm_minutes > 0 and scy_distance != "500" and scy_distance != "1000" and scy_distance != "1650":
    print("Your " + scy_distance + " yards time is estimated to be equal to " + str(scm_minutes) + "," + str(scm_seconds) + " in meters")
elif scy_distance != "500" and scy_distance != "1000" and scy_distance != "1650":
    print("Your " + scy_distance + " yards time is estimated to be equal to " + str(scm_seconds) + " in meters")
elif scy_distance == "500":
    print("A 500 yard race is usually compared to a 400 meter race")
    print("Your 500 yard time is estimated to be equal to " + str(scm_minutes) + "," + str(scm_seconds) + " for a 400m event")
elif scy_distance == "1000":
    print("A 1000 yard race is usually compared to a 800 meter race")
    print("Your 1000 yard time is estimated to be equal to " + str(scm_minutes) + "," + str(scm_seconds) + " for a 800m event")
elif scy_distance == "1650":
    print("A 1650 yard race is usually compared to a 1500 meter race")
    print("Your 1650 yard time is estimated to be equal to " + str(scm_minutes) + "," + str(scm_seconds) + " for a 1500m event")

quit = input("Press enter to exit the program")