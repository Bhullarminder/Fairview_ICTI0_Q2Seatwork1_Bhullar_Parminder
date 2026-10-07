from pyscript import display, document

# List of ICT club members
club_members = ["ictmem1", "ictmem2", "ictmem3", "ictmem4"]

def check_member(e):
    # Get the first and last name
    first_name = document.getElementById("firstName").value
    last_name = document.getElementById("lastName").value

    # Combine first name and last name
    full_name = first_name + " " + last_name

    # Check if the full name is in the club members list
    member = full_name in club_members

    # Messages stored in a tuple
    messages = (
        "Congratulations " + full_name + "! You are now part of the ICT club.",
        "Sorry " + full_name + ", your name is not on the list."
    )

    # True = 1, False = 0
    # 'not member' makes True become 0 and False become 1
    result = messages[not member]

    display(result, target="result")