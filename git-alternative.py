# Python program to explain os.system() method 
# #python script that runs git commands on a specified schedule.
	
# importing module
import os
import schedule
import time
from datetime import datetime

# Command to execute
# Using Windows OS command

cmd = 'git add . && git commit -m "Update" && git push'


# Using os.system() method

os.system(cmd)

