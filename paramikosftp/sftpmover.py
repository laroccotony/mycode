#!/usr/bin/env python3

import paramiko
import os

def main():
    t = paramiko.Transport("10.10.2.3", 22)
    t.connect(username="bender", password="alta3")

    for x in os.listdir("C:\\Users\\tony\\mycode\\filestocopy\\"): # iterate on directory contents
      if not os.path.isdir("C:\\Users\\tony\\mycode\\filestocopy\\"+x): # filter everything that is NOT a directory
        sftp.put("C:\\Users\\tony\\mycode\\filestocopy\\"+x) # sftp.put("from_path_local", "to_path_remote") - move file to target location

    sftp.close()
    t.close()

if __name__ == "__main__":
    main()