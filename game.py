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
                time.sleep(2)
                print("You are now out of the cell, and make a dash for the near by armory.")
                time.sleep(1)
                player.remove_item('Guard Key')
                armory(player)
            else:
                time.sleep(1)
                print("You do not have a key, time to try something else.")
                time.sleep(2)
                cell(player)

    if cmd == '2':
        print("You see all of the days you have tallied since arriving at the prison: 95 days.")
        time.sleep(1)
        print("Some of the stone is loose, but you doubt at this point anything can be done here.")
        time.sleep(2)
        print("1: Return.")
        print("2: Try prying the stones apart.")
        cmdlist = ['1','2']
        cmd = getcmd(cmdlist)

        if cmd == '1':
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
                print("The guard sighs, throwing his hands up in disbelief. And mutters under his breath 'Idiot...'")
                cell(player)
            if cmd == '2':
                print("\nYou successfully knock the guard unconscious, and are able to grab his keys.")
                player.add_item('Guard Key')
                time.sleep(1)
                print("You have obtained: Guard Key")
                time.sleep(1)
                cell(player)

def armory(player):
    print('\n')
    print('Current inventory: ', player.totalinventory)
    print('\n')
    print('---PRISON ARMORY---')
    time.sleep(1)

    print('You reach the armory: the door is open and you peak inside.')
    time.sleep(1)
    print('Inside you see four guards: three sitting at a table in a corner of the armory, and one is\n')
    print('equipping himself with a sword. What do you want to do?')

    time.sleep(1)
    print('\n1: It\'s too risky: step away from the armory and go further into the prison.')
    time.sleep(1)
    print('\n2:A weapon is important: attempt to sneak in and grab a weapon without anyone noticing.')

    cmdlist = ['1','2']
    cmd = getcmd(cmdlist)
    if cmd == '1':
        print('You sneak past the door, and continue deeper into the prison.')
        time.sleep(1)
        cell(player)
    if cmd == '2':
        print('You enter the cell, and attempt to grab a near by sword.')
        player.add_item('Sword')
        print(player.totalinventory)
        time.sleep(20)

def getcmd(cmdlist):
    cmd = input("Enter your choice: ")
    if cmd in cmdlist:
        return cmd

if __name__ == "__main__":
    player = Inventory('Player 1', '', '', '')
    print("The prisoner looks around the cell, scoffing at his present situation. He decides it's time to escape. Find a way out.")
    time.sleep(3)
    cell(player)
