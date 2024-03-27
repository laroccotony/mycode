
# From the challenge list, pull the strings eyes, goggles, and nothing and create a print function that returns this output:
# My eyes! The goggles do nothing!

# From the trial list, pull the strings eyes, goggles, and nothing and create a print function that returns this output:
# My eyes! The goggles do nothing!

# From the nightmare list, pull the strings eyes, goggles, and nothing and create a print function that returns this output:
# My eyes! The goggles do nothing!

challenge= ["science", "turbo", ["goggles", "eyes"], "nothing"]
trial= ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]
nightmare= [{"slappy": "a", "text": "b", "kumquat": "goggles", "user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}},"banana": 15, "d": "nothing"}]

# When your script runs, it should output the following:
# My eyes! The goggles do nothing!
# My eyes! The goggles do nothing!
# My eyes! The goggles do nothing!

c_eyes = challenge[2][1]
c_goggles = challenge[2][0]
c_nothing = challenge[3]

t_eyes = trial[2]["goggles"]
t_goggles = trial[2]["eyes"]
t_nothing = trial[3]

n_eyes = nightmare[0]["user"]["name"]["first"]
n_goggles = nightmare[0]["kumquat"]
n_nothing = nightmare[0]["d"]

print(f"My {c_eyes}! The {c_goggles} do {c_nothing}!")
print(f"My {t_eyes}! The {t_goggles} do {t_nothing}!")
print(f"My {n_eyes}! The {n_goggles} do {n_nothing}!")