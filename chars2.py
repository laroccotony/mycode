# Dictionary with character details, keys are lowercase for case-insensitive matching
marvelchars = {
    "starlord": {
        "real name": "peter quill",
        "powers": "dance moves",
        "archenemy": "Thanos"
    },
    "mystique": {
        "real name": "raven darkholme",
        "powers": "shape shifter",
        "archenemy": "Professor X"
    },
    "hulk": {
        "real name": "bruce banner",
        "powers": "super strength",
        "archenemy": "adrenaline"
    }
}

# Prompt user for input and convert to lowercase
char_name = input("Which character do you want to know about? (Starlord, Mystique, Hulk) ").lower()
char_stat = input("What statistic do you want to know about? (real name, powers, archenemy) ").lower()

# Check if the inputs are valid and retrieve the requested information
if char_name in marvelchars and char_stat in marvelchars[char_name]:
    # Original character name's capitalization is restored for printing
    original_char_name = [key for key in marvelchars if key.lower() == char_name][0]
    print(f"{original_char_name.capitalize()}'s {char_stat} is: {marvelchars[char_name][char_stat]}")
else:
    print("Information not found. Please check your inputs.")
