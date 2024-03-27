# Use the char_name and char_stat variables to pull the appropriate value from the dictionary below.
marvelchars= {
"starlord":
  {"real name": "peter quill",
  "powers": "dance moves",
  "archenemy": "Thanos"},

"mystique":
  {"real name": "raven darkholme",
  "powers": "shape shifter",
  "archenemy": "Professor X"},

"hulk":
  {"real name": "bruce banner",
  "powers": "super strength",
  "archenemy": "adrenaline"}
             }


def find_info(character, stat):
    # Normalize input to lowercase
    character_key = character.lower()
    stat_key = stat.lower()

    # Try to access the character and stat, handling cases where they might not exist
    character_info = marvelchars.get(character_key, {})
    stat_value = character_info.get(stat_key, "Information not found. Please check your inputs.")

    return f"{character.capitalize()}'s {stat} is: {stat_value}"

# Prompt user for input
char_name = input("Which character do you want to know about? (Starlord, Mystique, Hulk) ")
char_stat = input("What statistic do you want to know about? (real name, powers, archenemy) ")

# Print the information
print(find_info(char_name, char_stat))