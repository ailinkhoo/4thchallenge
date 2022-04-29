# Python program to explain os.system() method
	
# importing os module
import os
from turtle import hideturtle

# Command to execute
# Using Windows OS command


cmd = input('Your message: ')

cmd = 'git add . && git commit -m "$msg"'

# Using os.system() method
os.system(cmd)
