import shutil
import os

os.chdir("C:\\Users\\tony\\mycode")

xname = input('What is the new name for kerrigan.obj? ')
shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)
