from pyscript import display, document

# List of ICT club members
club_members = [
    "Pikachu 025",
    "Charizard 006",
    "Bulbasaur 001",
    "Squirtle 007"
]

def check_member(e):
    # Get the first and last name
    first_name = document.getElementById("firstName").value
    last_name = document.getElementById("lastName").value

    # Combine first name and last name
    full_name = first_name + " " + last_name

    # Checks if the full name is in the club members list
    member = full_name in club_members

    # Messages are stored in a tuple
    messages = (
        "Sorry " + full_name + ", your name is not on the list.",
        "Congratulations " + full_name + "! You are now part of the ICT Club."
    )

    # Use True = 1 and False = 0 to select the message
    result = messages * member

    # Display the result
    document.getElementById("result").innerHTML = result