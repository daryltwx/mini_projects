# Step 1. Ask for number of players
# Step 2. Number of players = number of range for loop
# Step 3. Random number generator 1-6. 
# Step 4. If number == 1, show total score
# Step 5. Next player starts
import random



# My try.
def main():
    score = 0
    number_of_players = int(input("How many players?: "))
    game_of_pig(number_of_players, score)


def game_of_pig(number_of_players, score):
        for i in range(number_of_players):
            while True:
                try:
                    if score < 50:
                        choice = input(f"Player {i+1} turn.. \nCurrent score: {score} \nRoll or End? ").lower().strip()
                        if choice == "roll":
                            points = random.randint(1,6)
                            print(points)
                            if points != 1:
                                score += points
                                pass
                            else:
                                print(f"Final score: {score}")
                                score = 0
                                break
                        elif choice == "end":
                            print(f"Final score: {score}")
                            score = 0
                            break
                    else: 
                        print(f"Ballsy, player {i} wins!")
                        return
                except ValueError:
                    print("Please select Roll or End")
                    pass


if __name__ == "__main__":
    main()



