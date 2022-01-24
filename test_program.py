#Instantiate Flask class
from flask import Flask, redirect, url_for

app = Flask(__name__)
print(__name__)


#Routing
@app.route('/personal_bests')
def pbs():
    return "personal_bests"


athletes = ("Joakim", "Kristian")
events = ("100 Free", "100 Fly", "50 Free")
athletes_events = {}
for i in athletes:
    athletes_events[i] = []
print(athletes_events)
for i in athletes_events:
    for x in events:
        athletes_events[i].append(x)
print(athletes_events)


hey = input("Press any key to exit")

if __name__ == "__main__":
    app.run()
