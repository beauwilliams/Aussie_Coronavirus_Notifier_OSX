# Coronavirus stats notifier for MAC OSX

This is a little project to demonstrate the use of an API and some python / shell scripts

With this tool you can receive an update to coronavirus stats in your OSX Notification Center

## USAGE

*Step 1* `cd` to the git directory after you have cloned it

*Step 2* Run `./launch.sh` and follow the prompts to start the service

## STOP THE SERVICE

Run the `./stop.sh` script

### PREVIEW IMAGE

![preview](https://i.ibb.co/V9w8bC9/Screen-Shot-2021-01-19-at-8-34-44-pm.png)

#### Currently supports Australia only

#### NOTE: This repo ships with a patched version of plyer. It sheds a dependency and fixes a bug relating to recent versions of osx to allow us to send notifications using some applescript I wrote as a replacement for the python module that was used previously. This should run on all OSX machines alike no need to worry about your python version!

