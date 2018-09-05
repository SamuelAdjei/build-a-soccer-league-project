# Create a script named league_builder.py.

# Make sure the script doesn't execute when imported; put all of your logic
# and function calls inside of an if __name__ == "__main__": block.

# Create variables and programming logic to divide the 18 players into three teams:
# Sharks, Dragons and Raptors. Make sure the teams have the same number of players on them,
# and that the experience players are divided equally across the three teams.

# Create a text file named teams.txt that includes the name of a team,
# followed by the players on that team. List all three teams and their players.


# In the list of teams include the team name on one line,
# followed by a separate line for each player.


# Include the player's name, whether the player has experience playing soccer,
# and the player's guardian names. Separate each bit of player information by a comma.

# For example, the text file might start something like this:
# Sharks
# Frank Jones, YES, Jim and Jan Jones
# Sarah Palmer, YES, Robin and Sari Washington
# Joe Smith, NO, Bob and Jamie Smith


if __name__ == "__main__":

    import csv

    Sharks = []
    Dragons = []
    Raptors = []
    players = {}

    # Makes CSV iterable and divides players into even teams
    def read(filename):
        skilled = []
        unskilled = []
        unshark = []
        undragon = []
        unraptor = []
    # Take info from soccer_players.csv and make iterable
        with open('soccer_players.csv', 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            next(csvfile)
            for row in reader:
                players[row[0]] = int(row[1]), row[2],row[3]
    # Divide players into experienced and inexperienced
        for key,value in players.items():
            if value[1] == 'YES':
                skilled.append(key)
            else:
                unskilled.append(key)
    # Evenly divides skilled players into teams
        Sharks.extend(skilled[:3])
        for player in Sharks:
            skilled.remove(player)
        Dragons.extend(skilled[:3])
        for player in Dragons:
            skilled.remove(player)
        Raptors.extend(skilled[:3])
    # Evenly divides unskilled players into teams
        unshark.extend(unskilled[:3])
        for player in unshark:
            unskilled.remove(player)
        undragon.extend(unskilled[:3])
        for player in undragon:
            unskilled.remove(player)
        unraptor.extend(unskilled[:3])
    #Adds unskilled teams to experienced teams
        Dragons.extend(undragon)
        Sharks.extend(unshark)
        Raptors.extend(unraptor)

        print_txt(Dragons)
        print_txt(Sharks)
        print_txt(Raptors)

    #Prints team names, members, experience, and guardians to teams.txt
    def print_txt(team):
        with open('teams.txt', 'a') as file:
            if team == Dragons:
                file.write("Dragons \n\n")
            elif team == Sharks:
                file.write("\n\nSharks\n\n")
            else:
                file.write("\n\nRaptors\n\n")
            for key,value in players.items():
                if key in team:
                    file.write(key + ' , ' + value[1] + ' , ' +  value[2] + '\n')

    read('soccer_players.csv')
    #omg it worked :D

    #Generates .txt files and prints welcome letters to them.
    def create_txt(*player):
        for key,value in players.items():
            current = key
            parent = value[2]
            mykey = key.replace(' ','_')
            mykey = mykey.lower()
            thefile = mykey.lower() + ".txt"
            with open(thefile, 'w') as file:
                if current in Dragons:
                    the_team = "Dragons"
                elif current in Sharks:
                    the_team = "Sharks"
                else:
                    the_team = "Raptors"
                file.write("Dear {},\n\nCongratulations. Your child, {}, has been placed on the {} team. The first practice will be 9/8/18 at 5:20PM.\n\n".format(parent, current, the_team))
                file.close()

    create_txt(players)
