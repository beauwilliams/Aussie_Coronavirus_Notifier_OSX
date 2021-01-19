import os, sys


file = open("launchctl_config.plist","w")

cwd = os.getcwd()
pythonpath =  "<string>{}/env/bin/python</string>".format(cwd)
filepath = "<string>{}/coronafier.py</string>".format(cwd)
interval = 60*int(input("Time in minutes you wish to be notified of the current coronavirus stats in Australia: "))


#launchctl plist file to be generated for purposes of automatically notifying us at a regular interval
F = ["<?xml version=\"1.0\" encoding=\"UTF-8\"?> \n", "<!DOCTYPE plist PUBLIC \"-//Apple//DTD PLIST 1.0//EN\" \"http://www.apple.com/DTDs/PropertyList-1.0.dtd\"> \n", "<plist version=\"1.0\"> \n", "<dict> \n", "<key>Label</key> \n", "<string>desktop-notifier-python</string> \n", "<key>ProgramArguments</key> \n", "<array> \n", "%s \n" % (pythonpath), "%s \n" % (filepath), "</array> \n", "<key>StartInterval</key> \n", "<integer>%s</integer> \n" % (interval), "</dict> \n", "</plist> \n", ]

file.writelines(F)
file.close()

