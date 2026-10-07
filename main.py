from pyscript import display, document

# List of ICT club members
club_members = [
    "Pikachu 025",
    "Charizard 006",
    "Bulbasaur 001",
    "Squirtle 007"
]

def check_member(e):
    first_name = document.getElementById("firstName").value
    last_name = document.getElementById("lastName").value

    full_name = first_name + " " + last_name

    member = full_name in club_members

    messages = (
        "Congratulations " + full_name + "! You are now part of the ICT club.",
        "Sorry " + full_name + ", your name is not on the list."
    )

    result = messages[not member]

    document.getElementById("result").innerHTML = result