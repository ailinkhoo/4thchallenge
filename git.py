# Python program to explain os.system() method
	
# importing os module
import os

# Command to execute
# Using Windows OS command
cmd0 = 'cd '
cmd1 = 'git add .'
cmd2 = 'git commit -m "Updates"'
cmd3 = 'git push'

# Using os.system() method
os.system(cmd1)
os.system(cmd2)
os.system(cmd3)