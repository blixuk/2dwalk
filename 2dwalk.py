#!/usr/bin/env python3
# Author: Blix

import random
import itertools
import time

X = -1 # X axis
Y = 0 # Y axis
HEADING = 1 # NORTH: 1, EAST: 2, SOUTH: 3, WEST: 4
COUNT = 0 # turn counter

def doWalk():
	global X
	global Y
	global HEADING
	global COUNT

	for count, heading in getHeading(): # get the turn count and the heading
		if heading == HEADING:	# if the heading is the same as the last turn don't move
			pass
		elif heading == 1: # if heading is north move one positive Y position
			Y += 1 # NORTH 
		elif heading == 2: # if heading is east move one positive X position
			X += 1 # EAST 
		elif heading == 3: # if heading is south move one negative Y position
			Y -= 1 # SOUTH
		elif heading == 4: # if heading is west move one negative X position
			X -= 1 # WEST
		
		COUNT = count # update the global turn counter
		HEADING = heading # update the global heading

		if X == 0 and Y == 0: # if X and Y both equal 0; we have returned home
			setStatus(X, Y, HEADING, COUNT)
			print('Returned Home!')
			writeCount(count) # append the current number of turns to the list
			break # quit

		setStatus(X, Y, HEADING, COUNT) # show a status of all current information
		#time.sleep(0.1)

def getHeading():
	for count in itertools.count(start=1): # get an infinate counter starting at 1
		yield count, int(random.randrange(1, 5)) # return the count and a random number between 1 and 4

def setStatus(x, y, h, c):
	heading = ['NORTH', 'EAST', 'SOUTH', 'WEST'] # list if heading names for visual purposes
	print(f'| TURN: {c}	| X: {x}	| Y: {y}	| HEADING: {heading[h - 1]}') # print the stats to the terminal

def writeCount(count): # append the output to a list
	with open('counter.txt', 'a+') as file:
		file.write(str(f'{count}\n')) # append the turn count to a new line

if __name__ == "__main__":
	doWalk() # start walking