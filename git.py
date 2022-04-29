# Python program to explain os.system() method
	
# importing os module
import os

# Command to execute
# Using Windows OS command


cmd = 'git add . && git commit -m "Update" && git push'
print(type(cmd))

# Using os.system() method
os.system(cmd)
