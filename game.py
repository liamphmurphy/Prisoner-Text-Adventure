import time
from items import Inventory

# Function to start the game, which is called at the bottom of the file in main.
def cell(player):
	print('\n')
	print('Current inventory: ', player.totalinventory)
	print('\n')
	print('---PRISON CELL---')
	time.sleep(1)
	print('\n1: Look at cell door.')
	print("2: Look at prison cell walls.")
	print("3: Look at anything going on outside of the cell.")

	cmdlist = ['1','2','3']
	cmd = getcmd(cmdlist)
	time.sleep(1)
	if cmd == '1':
		print("Cell is locked, of course. The keyhole on the other side is reachable, but I need a key.")
		time.sleep(1)
		print("\n1: Attempt to unlock the door.")
		print("2: Return.")
		cmdlist = ['1','2']
		cmd = getcmd(cmdlist)

		if cmd == '1':
			if 'Guard Key' in player.totalinventory:
				print("Successfully picked the lock with the Guard Key.")
			else:
				time.sleep(1)
				print("You do not have a key, time to try something else.")
				time.sleep(2)
				cell(player)

	if cmd == '3':
		print("You see a guard with a set of keys jingling from his belt.")
		print("\n1: Call the guard over")
		time.sleep(0.5)
		print("\n2: Return")

		cmdlist = ['1','2']
		cmd = getcmd(cmdlist)
		if cmd == '1':
			print("\nYou yell out: 'Oi, guard, I'm not feeling so good over here!'")
			time.sleep(2)
			print("\nThe guard walks over and places himself right in front of the bars.")
			time.sleep(1)
			print("\n'Bloody hell, what is the matter?'")
			time.sleep(2)
			print("\n1: Wave him off and say, 'Oh nevermind, I felt sick for a moment, I am fine now.'")
			print ("\n2: Quickly reach through the bars, and smash his head against the bars.")
			cmdlist = ['1','2']
			cmd = getcmd(cmdlist)
            
			if cmd =='1':
				print("The guard sighs once more, throwing his hands up in disbelief. And mutters 'Idiot...'")
				cell(player)
			if cmd == '2':
				print("\nYou successfully knock the guard unconscious, and are able to grab his keys.")
				player.add_item('Guard Key')
				time.sleep(1)
				print("You have obtained: Guard Key")
				time.sleep(1)
				cell(player)
                

def getcmd(cmdlist):
	cmd = input("Enter your choice: ")
	if cmd in cmdlist:
		return cmd

if __name__ == "__main__":
	player = Inventory('Player 1', '', '') 
	print("The prisoner looks around the cell, scoffing at his present situation. He decides it's time to escape. Find a way out.")	
	time.sleep(3)
	cell(player)