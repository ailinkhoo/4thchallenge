# Python program to explain os.system() method
	
# importing os module
import os

# Command to execute
# Using Windows OS command

cmd = 'git add . && git commit -m "Updates" && git push'

# Using os.system() method
os.system(cmd)
