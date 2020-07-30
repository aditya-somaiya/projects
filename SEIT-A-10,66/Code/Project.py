import random
import time
#import sys
from PIL import Image
import pygame
import pyttsx3
t = 7
pygame.mixer.init()
win_sound = pygame.mixer.Sound("win.wav")
engine=pyttsx3.init()

def msg(room):
	time.sleep(1)
	if room['msg'] =='': #There is no custom messages
		return "You have entered the " + room['name']
	else:
		return room['msg']

def get_choice(room,dir):
	if dir=='N' or dir=='n':
		choice = 0
	elif dir=='E' or dir=='e':
		choice = 1
	elif dir=='S' or dir=='s':
		choice = 2
	elif dir=='W' or dir=='w':
		choice = 3
	else:
		return -1

	if room['directions'][choice] == 0:
		return 4
	else:
		return choice

def main():
	dirs = (0,0,0,0) #default

	enterance = {'name':'Enterance Way','directions':dirs,'msg':''}
	livingroom = {'name':'Livingroom','directions':dirs,'msg':''}
	hallway = {'name':'Hallway','directions':dirs,'msg':''}
	kitchen = {'name':'Kitchen','directions':dirs,'msg':''}
	diningroom = {'name':'Diningroom','directions':dirs,'msg':''}
	family_room = {'name':'Family Room','directions':dirs,'msg':''}

	#Directions are tuples: Which rooms are at N,E,S,W
	enterance['directions'] = (kitchen,livingroom,0,0)
	livingroom['directions'] = (diningroom,0,0,enterance)
	hallway['directions'] = (0,kitchen,0,family_room)
	kitchen['directions'] = (0,diningroom,enterance,hallway)
	diningroom['directions'] = (0,0,livingroom,kitchen)
	family_room['directions'] = (0,hallway,0,0)

	#Rooms where the Data Disk might be
	rooms = [livingroom,hallway,kitchen,diningroom,family_room]
	room_with_drive = random.choice(rooms)
	drive_acquired = False
	room = enterance
	print('Special Agent 007. Your mission is to find the data disk')
	engine.say("Special Agent 007. Your mission is to find the data disk")
	engine.runAndWait()

	while True:
		if drive_acquired and room['name'] == 'Enterance Way':
			win_sound.play()
			print("You have aquired the data and returned to extraction")
			engine.say("You have aquired the data and returned to extraction")
			engine.runAndWait()
			print("Mission Complete!")
			engine.say("Mission Complete!")
			engine.runAndWait()
			break
		elif not drive_acquired and room['name'] == room_with_drive['name']:
			drive_acquired = True
			print(msg(room))
			print("There's the data disk")
			engine.say("There's the data disk")
			engine.runAndWait()
			print("You have copied all the data")
			engine.say("You have copied all the data")
			engine.runAndWait()
			print("Head to extraction!")
			engine.say("Head to extraction!")
			engine.runAndWait()
			room['msg'] = ("You are back in the " + room['name'] +
				"\nYou already completed the objective" +
				"\nHead to Extraction!")
		else:
			print(msg(room))
			room['msg'] = "You are back in the " + room['name']

		stuck = True
		while stuck:
			global t
			if(t==0):
				retry()
			print("You have {} minutes left".format(t))
			engine.say("You have {} minutes left".format(t))
			engine.runAndWait()
			t=t-1
			engine.say("Which direction do you want to go in N,E,S,W?")
			engine.runAndWait()
			dir = input("Which direction do you want to go in N,E,S,W? ")
			choice = get_choice(room,dir)
			if choice == -1:
				dir = print("Please enter N,E,S or W?")
				engine.say("Please enter N,E,S or W?")
				engine.runAndWait()
			elif choice == 4:
				dir = print("You cannot go in that direction")
				engine.say("You cannot go in that direction")
				engine.runAndWait()
			else:
				room = room['directions'][choice]
				map(room)
				stuck = False

def map(room):
	if(room['name'] == 'Enterance Way'):
		img = Image.open('entrance1.PNG').show()
	elif(room['name'] == 'Diningroom'):
		img = Image.open('diningroom.PNG').show()
	elif(room['name'] == 'Family Room'):
		img = Image.open('familyroom.PNG').show()
	elif(room['name'] == 'Hallway'):
		img = Image.open('hallway.PNG').show()
	elif(room['name'] == 'Livingroom'):
		img = Image.open('livingroom.PNG').show()
	elif(room['name'] == 'Kitchen'):
		img = Image.open('kitchen.PNG').show()
     
def retry():
	print("You are out of time")
	engine.say("You are out of time")
	engine.runAndWait()
	print("Mission Failed!")
	engine.say("Mission Failed!")
	engine.runAndWait()
	print("You have failed this mission but you can always try again")
	engine.say("You have failed this mission but you can always try again")
	engine.runAndWait()
	print("Would you like to try another mission?")
	engine.say("Would you like to try another mission?")
	engine.runAndWait()
	global t
	t = 7
	restart = True
	while restart:
		engine.say("Do you copy, Press Y to confirm and N to deny")
		engine.runAndWait()
		print("Do you copy, Press Y to confirm and N to deny")
		cr = input()
		if cr == 'y' or cr == 'Y':
			print("Lets start the mission!")
			engine.say("Lets start the mission!")
			engine.runAndWait()
			main()
			time.sleep(1)
			print("We have found another one of Hiesenberg's bases, would you like to take another mission?")
			engine.say("We have found another one of Hiesenberg's bases, would you like to take another mission?")
			engine.runAndWait()
			time.sleep(1)
		elif cr == 'n' or cr == 'N':
			print("You have denied the mission!")
			engine.say("You have denied the mission!")
			engine.runAndWait()
			restart = False
			sys.exit()
		else:
			print("Please choose a correct response")
			engine.say("Please choose a correct response")
			engine.runAndWait()

print("Connecting...")
time.sleep(1)
print("Connecting...")
time.sleep(2)
print("Connection Established!")
time.sleep(1)
engine.say("New mission received")
engine.runAndWait()
print("Special Agent 007, this is HQ, you have been assigned a new mission, here are the specifics")
engine.say("Special Agent 007, this is HQ, you have been assigned a new mission, here are the specifics")
engine.runAndWait()
print("We have discovered a hidden base of the Crime Lord Hiesenberg")
engine.say("We have discovered a hidden base of the Crime Lord Hiesenberg")
engine.runAndWait()
print("While the assault teams hold of his forces we need an covert agent to go in the base and copy the information stored in a specific data drive.")
engine.say("While the assault teams hold of his forces we need an covert agent to go in the base and copy the information stored in a specific data drive.")
engine.runAndWait()
print("This data drive contains all the information on his assets and operations and is essential to his downfall")
engine.say("This data drive contains all the information on his assets and operations and is essential to his downfall")
engine.runAndWait()
print("This base looks like a normal house to avoid suspicions")
engine.say("This base looks like a normal house to avoid suspicions")
engine.runAndWait()
print("The house has 5 rooms and the data drive can in any of the rooms in the house")
engine.say("The house has 5 rooms and the data drive can in any of the rooms in the house")
engine.runAndWait()
print("Just wait a minute and a map will be displayed on your sceen")
engine.say("Just wait a minute and a map will be displayed on your sceen")
engine.runAndWait()
print("You will enter from the room marked yellow, from where you will go and search the house for the drive")
engine.say("You will enter from the room marked yellow, from where you will go and search the house for the drive")
engine.runAndWait()
print("Once you collect the data from the drive you are to rush back to extraction")
engine.say("Once you collect the data from the drive you are to rush back to extraction")
engine.runAndWait()
print("You will have 7 minutes to complete this mission")
engine.say("You will have 7 minutes to complete this mission")
engine.runAndWait()
print("This is a Stealth Mission, you will go in and come out with none the wiser")
engine.say("This is a Stealth Mission, you will go in and come out with none the wiser")
engine.runAndWait()
img=Image.open('entrance1.png').show()
start = True
while start:
	engine.say("Do you copy, press Y to confirm and N to deny")
	engine.runAndWait()
	print("Do you copy, press Y to confirm and N to deny")
	c = input()
	if c == 'y' or c == 'Y':
		print("Lets start the mission!")
		engine.say("Lets start the mission!")
		engine.runAndWait()
		main()
		time.sleep(1)
		t = 7
		print("We have found another one of Hiesenberg's bases, would you like to take another mission?")
		engine.say("We have found another one of Hiesenberg's bases, would you like to take another mission?")
		engine.runAndWait()
		time.sleep(1)
	elif c == 'n' or c == 'N':
		print("You have denied the mission!")
		engine.say("You have denied the mission!")
		engine.runAndWait()
		start = False
	else:
		print("Please choose a correct response")
		engine.say("Please choose a correct response")
		engine.runAndWait()