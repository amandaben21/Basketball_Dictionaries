class Player:
    def __init__(self, players_dict):
        self.name = players_dict["name"]
        self.age = players_dict["age"]
        self.position = players_dict["position"]
        self.team = players_dict["team"]
    
    # overwriting the way python will interperate the object as when it gets printed to the console,
    # so when type print it will go to this method first to default it representing that object
    def __repr__(self): 
        return f"Player: {self.name}, {self.age} y/o, pos: {self.position}, team: {self.team}"


#Challenge 2: Create instances using individual player dictionaries.
# Given these variables, create Player instances for each of the 
# following dictionaries. Be sure to instantiate these outside the
# class definition, in the outer scope.
kevin = {
    "name": "Kevin Durant", 
    "age":34, 
    "position": "small forward", 
    "team": "Brooklyn Nets"
}

jason = {
    "name": "Jason Tatum", 
    "age":24, 
    "position": "small forward", 
    "team": "Boston Celtics"
}

kyrie = {
    "name": "Kyrie Irving", 
    "age":32, "position": "Point Guard", 
    "team": "Brooklyn Nets"
}
print("~~~~~~~~~~~~~~~~~~~~~~")

player_kevin = Player(kevin)
print(kevin["name"])
print(player_kevin)

print("~~~~~~~~~~~~~~~~~~~~~~")

player_jason = Player(jason)
print(jason["name"])
print(player_jason)

print("~~~~~~~~~~~~~~~~~~~~~~")

player_kyrie = Player(kyrie)
print(kyrie["name"])
print(player_kyrie)

print("~~~~~~~~~~~~~~~~~~~~~~")

#Challenge 3: Make a list of Player instances from a list of dictionaries
# Finally, given the example list of players at the top of this module (the one with many players)
# write a for loop that will populate an empty list with Player objects from the original 
# list of dictionaries.
players = [
    {
        "name": "Kevin Durant",
        "age":34, 
        "position": "small forward", 
        "team": "Brooklyn Nets"
    },

    {
        "name": "Jason Tatum", 
        "age":24, 
        "position": "small forward", 
        "team": "Boston Celtics"
    },

    {
        "name": "Kyrie Irving", 
        "age":32, "position": "Point Guard",
        "team": "Brooklyn Nets"
    },

    {
        "name": "Damian Lillard",
        "age":33, "position": "Point Guard",
        "team": "Portland Trailblazers"
    },

    {
        "name": "Joel Embiid",
        "age":32, "position": "Power Foward",
        "team": "Philidelphia 76ers"
    },

    {
        "name": "",
        "age":16,
        "position": "P",
        "team": "en"
    }
]

new_team = []
for player_dict in players:
    player = Player(player_dict)
    new_team.append(player)
print(new_team)