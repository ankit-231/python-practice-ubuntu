class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.items = []

def start_game():
    print("Welcome to the Adventure Game!")
    name = input("Enter your name: ")
    player = Player(name)
    print(f"Hello, {player.name}! Let's start the adventure.")

    while True:
        action = input("What would you like to do? (explore/fight/quit): ").lower()
        if action == 'quit':
            print("Thanks for playing!")
            break
        elif action == 'explore':
            print("You found a treasure chest!")
            player.items.append("Treasure")
        elif action == 'fight':
            print("A monster attacks you!")
            player.health -= 20
            if player.health <= 0:
                print("Game over! You lost.")
                break
            else:
                print("You defeated the monster.")
        else:
            print("Invalid action. Please choose explore, fight, or quit.")

start_game()
