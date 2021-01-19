#!/bin/bash

#I am shipping python with this for now just to make sure it is portable
"${PWD}"/env/bin/python launchctl_generator.py

#Loads the launchctl
launchctl load launchctl_config.plist

#Starts it
launchctl start desktop-notifier-python


