import shutil
import os

os.chdir("C:\\Users\\tony\\mycode")

shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")
shutil.copytree("5g_research/", "5g_research_backup/")
