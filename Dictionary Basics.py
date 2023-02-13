football_players_club = {"Cristiano Ronaldo": "Juventus",
                         "Bruno Fernandez": "Manchester United",
                         "Lionel Messi": "PSG",
                         "Sadio Mane": "FC Bayern Munchen",
                         "Harry Kane": "Tottenham Hotspur"
                         }

print(football_players_club.keys())
print(football_players_club.values())
print('---------------------------------------')

del football_players_club["Cristiano Ronaldo"]  # delete
football_players_club.pop("Bruno Fernandez")  # another delete
football_players_club.clear()  # delete all the pairs
print(football_players_club)
print('---------------------------------------')

print('Kilian Mbappe' in football_players_club.keys())  # to check if value is in dict
print('---------------------------------------')

football_players_club["Mo Salah"] = "Liverpool"  # add
new_pair = (("Jadon Sancho", "Man Utd"), ("Enzo Fernandez", "Chelsea"))  # another way of add
football_players_club.update(new_pair)
football_players_club |= new_pair  # another way of add
football_players_club.update({"Ronald Araujo": "FCB", "Osman Dembele": "FCB"})  # update
print(len(football_players_club))  # len or number of keys
print('---------------------------------------')

print(football_players_club.items())  # List of pairs to iterate through
print('---------------------------------------')

for k, v in football_players_club.items():  # iterating through
    print(f'{k} : {v}')
print('---------------------------------------')

# Formatting

print("{0} is my favorite Team".format(football_players_club['Jadon Sancho']))
print("{Jadon Sancho} is my favorite Team".format(**football_players_club))  # Unpacking
print("{0[Jadon Sancho]} is my favorite Team".format(football_players_club))
print(f'{football_players_club["Jadon Sancho"]} is my favorite Team')

