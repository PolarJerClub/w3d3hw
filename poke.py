import requests
# recreate your pokemon class here
class Pokemon:
    def __init__(self, name):
        self.name = name
        self.types = []
        self.weight = None
        # new image attribute
        self.image = None
        self.poke_api_call()
        
    def poke_api_call(self):
        r = requests.get(f"https://pokeapi.co/api/v2/pokemon/{self.name.lower()}")
        if r.status_code == 200:
            pokemon = r.json()
        else:
            print(f"Please check the spelling of your pokemon's name and try again!: {r.status_code}")
            return
        
        self.name = pokemon['name']
        self.types = [type_['type']['name'] for type_ in pokemon['types']]
        self.abilities = [ability['ability']['name'] for ability in pokemon['abilities']]
        self.weight = pokemon['weight']
        #new image details. adding image to attribute
        self.image = pokemon['sprites']['front_shiny']
        
    #repr gives us string representation of our object
    def __repr__(self):
        return f"You caught a {self.name}!"
    

class Move_Tutor(Pokemon):
    def __init__(self, name):
        super().__init__(name)
        self.name = name
        self.moves = []
        self.moves_list = []
    
    
    def teach_moves(self):
        r = requests.get(f"https://pokeapi.co/api/v2/pokemon/{self.name}/")
        if r.status_code == 200:
            pokemoves = r.json()
        else:
            print(f"Ran into an issue, please check your pokemon's name: {r.status_code}")
            return
        self.moves = [move['move']['name'] for move in pokemoves['moves']]

        print(f"Here are all of the moves that {self.name} can learn! Your pokemon may only learn 4 moves, so choose wisely!\n\n{self.moves}\n")
        self.ask_move1 = input(f"What is the first move you would like to teach {self.name}? ")
        self.moves_list.append(self.ask_move1)
        print(f"{self.name.title()} learned {self.ask_move1}!")
        self.ask_move2 = input(f"What is the second move you would like to teach {self.name}? ")
        self.moves_list.append(self.ask_move2)
        print(f"{self.name.title()} learned {self.ask_move2}!")
        self.ask_move3 = input(f"What is the third move you would like to teach {self.name}? ")
        self.moves_list.append(self.ask_move3)
        print(f"{self.name.title()} learned {self.ask_move3}!")
        self.ask_move4 = input(f"What is the last move you would like to teach {self.name}? ")
        self.moves_list.append(self.ask_move4)
        print(f"{self.name.title()} learned {self.ask_move4}!")
        print(f"\nCongratulations! {self.name} has learned four new moves! \n{self.moves_list}")
                        
                    
pikachu = Move_Tutor('pikachu')
pikachu.teach_moves()