

loginfail = 0

keystone_file = open("C:\\Users\\tony\mycode\\attemptlogin\\keystone.common.wsgi", "r")

for line in keystone_file:
    if "- - - - -] Authorization failed" in line:
        loginfail += 1

print("The nunber if failed login attempts is", loginfail)
keystone_file.close()