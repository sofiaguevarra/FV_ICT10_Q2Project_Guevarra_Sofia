from pyscript import display, document
#This protion is for the Grade Calculator
def general_weighted_average(event=None):
    first_name = document.getElementById("first_name").value
    last_name = document.getElementById("last_name").value

#We'll use this so that if the person leaves the grades box blank, it leaves an error and asks them to fill it out
#I used https://www.w3schools.com/python/python_try_except.asp to help me with this code
    def to_float(val):
        try:
            return float(val)
        except: 
            return None

    math = to_float(document.getElementById('math').value)
    science = to_float(document.getElementById('science').value)
    english = to_float(document.getElementById('english').value)
    filipino = to_float(document.getElementById('filipino').value)
    social_studies = to_float(document.getElementById('social_studies').value)
    ict = to_float(document.getElementById('ict').value)

    if None in [math, science, english, filipino, social_studies, ict]:
        display("Please fill in all grade fields with valid numbers.", target='output') #This will be displayed when the person leaves the boxes or any boxes blank
        return

    subjects = ['Science', 'Math', 'English', 'Filipino', 'Social Studies', 'ICT']
    grades = [science, math, english, filipino, social_studies, ict]
    units = [5, 5, 5, 3, 3, 2]
#This is the equation to get the general weighted average. 
    weighted_sum = sum(g * u for g, u in zip(grades, units))
    total_units = sum(units)
    gwa = weighted_sum / total_units

    summary = f"""\
{subjects[0]}: {science:.0f}
{subjects[1]}: {math:.0f}
{subjects[2]}: {english:.0f}
{subjects[3]}: {filipino:.0f}
{subjects[4]}: {social_studies:.0f}
{subjects[5]}: {ict:.0f}
"""
#Once the person put all their grades already, it will show a summary and their general average
    display(f'Name: {first_name} {last_name}', target="student_info")
    display(summary, target='summary')
    display(f'Your general weighted average is {gwa:.2f}', target='output')

#This is the start for our page 3 for the Club information
#Taken from skills test
pick_a_club = {
    "Marching Band": { #key
        "Advisor": "Mr. Emilio Alumno", #Advisor: key, "Mr Emilio Alumno": value
        "Schedule": "Tuesday & Wednesday 3:00 to 4:30 PM", #Schedule: key, "Tuesday & Wednesday 3:00 to 4:30 PM": value
        "Venue": "Band Room", #Venue: key, "Band Room": value
        "Description": "Marching band is an opportunity to show off your talent with music!", #Description: Key, "Marching band is an opportunity to show off your talent with music!": Value
        "Members": "30" #Members: key, "30": Value
    },
#We used key value pairs for our dictionaries (The clubs). Every key is supposed to be unique, no repitition
    "Glee Club": {
        "Advisor": "Mr. Denver Martin",
        "Schedule": "Monday 3:00 to 5:00 PM",
        "Venue": "High School Music Room",
        "Description": "Show off your voice by joining the Glee Club!",
        "Members": "30"
    }, 
#We can use the same key names as the previous club because they aren't in the same dictionary
   
    "Dance Club": {
        "Advisor": "Mr. Alfred Cases",
        "Schedule": "Tuesday 3:00 to 5:00 PM",
        "Venue": "Teatro Preciosa",
        "Description": "Show off your dance moves with the Dance Club!",
        "Members": "30"
    },
    "Math Club": {
        "Advisor": "Mr. Nicole Gabuya",
        "Schedule": "Monday 2:30 to 3:00 PM",
        "Venue": "Room 404",
        "Description": "Math opens big doors for competitions!",
        "Members": "30"
    },
    "Science Club": {
        "Advisor": "Ms. Jameelyn Maramag",
        "Schedule": "Tuesday 3:00 to 4:00 PM",
        "Venue": "Room 404",
        "Description": "Science opens big doors for competition and experiments!",
        "Members": "30"
    },
    "Communications Arts Club": {
        "Advisor": "Ms. Yannis Fernandez",
        "Schedule": "Wednesday & Friday 3:00 to 4:00 PM",
        "Venue": "Room 406",
        "Description": "Create esseys, poems, and magazines!",
        "Members": "30"
    },
    "Cadet Officer Candidate Course": {
        "Advisor": "SSgt. Jemima David PA (Res)",
        "Schedule": "Wednesday 2:30 to 4:30 PM",
        "Venue": "Quadrangle / Teatro Preciosa",
        "Description": "Become the person you desire to be!",
        "Members": "30"
    },
    "Social Science Club": {
        "Advisor": "Mr. Roberto Lim",
        "Schedule": "Tuesday 3:00 to 4:00 PM",
        "Venue": "Room 409",
        "Description": "Opens big doors for debates, expanding knowledge, and many more!",
        "Members": "30"
    },
    "Volleyball Varsity": {
        "Advisor": "Mr. Adrian Ruiz",
        "Schedule": "Wednesday 3:00 to 4:00 PM",
        "Venue": "Quadrangle",
        "Description": "The volleyball team awaits for you, join now!",
        "Members": "30"
    },
    "Basketball Varsity": {
        "Advisor": "Mr. Adrian Ruiz",
        "Schedule": "Monday 3:00 to 4:00 PM",
        "Venue": "Quadrangle",
        "Description": "The basketball team awaits for you, join now!",
        "Members": "30"
    }
}
#This whole code runs the informatio output
def show_club_information(event=None):
    club_name = document.getElementById("club_info").value
    club = pick_a_club[club_name] 
#This will show the advisor, schedule, and venue of the persons selected club
    document.getElementById("output").innerHTML = (
        f"<div class='card p-3 bg-light text-dark'>"
        f"<h4 class='card-title'>{club_name}</h4>"
        f"<p><b>Advisor:</b> {club['Advisor']}</p>"
        f"<p><b>Schedule:</b> {club['Schedule']}</p>"
        f"<p><b>Venue:</b> {club['Venue']}</p>"
        f"<p><b>Description:</b> {club['Description']}</p>"
        f"<p><b>Number of Members:</b> {club['Members']}</p>"
        f"</div>"
    )



