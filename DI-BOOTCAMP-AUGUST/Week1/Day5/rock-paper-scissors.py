import game

def get_user_menu_choice() : 
    user_choice = input("Menu: \n (g) Play a new game \n (x) Show scores and exit \n  : ")
    if not user_choice in ["g","x"] :
        get_user_menu_choice()
    return user_choice

def print_results(results) :
    print("Game Results")
    for key,value in results.items() :
        print(f" You {key} {value} times")
        
def main() :
    party = game.Game()
    user = get_user_menu_choice()
    while not user == "x":
        print_results(party.play())
        user = get_user_menu_choice()
    print("\nThank you for playing")
    
    
main()
        
        