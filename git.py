# Python program to explain os.system() method
	
# importing os module
import os

# Command to execute
# Using Windows OS command



cmd1 = 'msg = input("Your message")'

os.system(cmd1)

# cmd = 'git add . && git commit -m "Update" && git push'

cmd = 'git add . && git commit -m "${msg}" && git push'

# Using os.system() method
os.system(cmd)
