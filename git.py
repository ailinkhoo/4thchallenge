# Python program to explain os.system() method
	
# importing os module
import os

# Command to execute
# Using Windows OS command

msg = input("Message: ")

cmd = "git add . && git commit -m '{msg}' && git push"

# Using os.system() method
os.system(cmd)

