# http://controller:5000/v3/auth/tokens

controller = 0

key_file = open("C:\\Users\\tony\mycode\\attemptlogin\\keystone.common.wsgi", "r")

for line in key_file:
    if "http://controller:5000/v3/auth/tokens" in line:
        controller += 1

print(f"There are {controller} controllers")
key_file.close()