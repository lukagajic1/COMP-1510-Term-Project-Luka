"""
Luka Gajic
A01495410

Create a game.
"""
import random
import copy
from itertools import product


def make_board(rows: int, columns: int) -> dict:
    """
    Create and return a dictionary with tuple coordinates as keys representing the game board and
    short room descriptions as values.

    :param rows: an integer representing the number of rows in the board
    :param columns: an integer representing the number of columns in the board
    :precondition: rows must be a positive integer greater than 0
    :precondition: columns must be a positive integer greater than 0
    :postcondition: create a dictionary containing tuples representing the locations on the board
    :raises ValueError: if rows or columns are not integers
    :raises ValueError: if rows or columns are not greater than 0
    :return: a dictionary containing key-value pairs of tuples, representing the coordinates on the board,
             and a string describing the locations at each coordinate.

    >>> board = make_board(2, 2)
    >>> len(board)
    4
    """
    descriptions = [
        "A foggy forest clearing",
        "A narrow path covered in roots",
        "A glowing mushroom grove",
        "A silent pond reflecting moonlight",
        "A ruined shrine overtaken by vines",
        "A dark thicket where branches claw at you",
        "A clearing filled with strange whispers",
    ]

    if type(rows) is not int:
        raise ValueError("rows must be an integer")

    if type(columns) is not int:
        raise ValueError("columns must be an integer")

    if rows <= 0:
        raise ValueError("rows must be greater than 0")

    if columns <= 0:
        raise ValueError("columns must be greater than 0")

    else:
        game_board = {
            (row, column): random.choice(descriptions)
            for row, column in product(range(rows), range(columns))
        }

    return game_board


def make_character(name: str) -> dict:
    """
    Initialize a character with the attributes of X-coordinate, Y-coordinate, Max HP, Level, EXP, Name, Luck, Level Name
    and Current HP as keys in a dictionary.

    :postcondition: create a character at coordinates (0, 0), where the key 'X-coordinate' represents integer row value
                    key and 'Y-coordinate' key represents integer column value
    :postcondition: set the character key 'Current HP' to integer value 8
    :postcondition: set the character Key 'Luck' to integer value 1
    :postcondition: set the character Key 'EXP' to integer value 0
    :postcondition: set the character Key 'Name' to user input string
    :postcondition: set the character Key 'Max HP' to integer value 8'
    :postcondition: set the character key 'Level Name' to string 'Beginner'
    :return: a dictionary representing the player character

    >>> player = make_character("Luka")
    >>> player["X-coordinate"]
    0
    >>> player["Current HP"]
    8
    """
    return {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 8,
            "Max HP": 8, "Luck": 1, "Level": 1, "EXP": 0, "Name": name, "Level Name": "Beginner"}


def game():
    """
    Drive the game.
    """
    rows = 10
    columns = 10
    board = make_board(rows, columns)
    character_name = input("Enter character name: ")
    describe_game()
    character = make_character(character_name)
    achieved_goal = False

    describe_current_location(board, character)

    while is_alive(character) and not achieved_goal:
        direction = get_user_choice()
        valid_move = validate_move(board, character, direction)

        if not valid_move:
            print(f"You are at position ({character['X-coordinate']}, {character['Y-coordinate']}) "
                  f"You cannot go that way. Try again.")
            continue

        move_character(character, direction)
        display_map(rows, columns, character)
        print()
        describe_current_location(board, character)

        if check_if_goal_attained(rows, columns, character):
            if character["Level"] < 3:
                print("You found the Forest Guardian, but you must be level 3 to challenge it.")
            else:
                achieved_goal = final_boss_encounter(character)
            continue

        there_is_a_challenge = check_for_foes()

        if not there_is_a_challenge:
            continue

        print()
        print("A challenge appears...")
        print()

        challenge_type = choose_challenge()

        if challenge_type == "enemy":
            won = guessing_game(character)
        elif challenge_type == "potion":
            won = potion_gamble(character)
        else:
            won = dice_roll_challenge(character)

        if won:
            gain_experience(character)

            if has_leveled_up(character):
                level_up(character)

    if achieved_goal:
        print()
        print("Congratulations! You defeated the Forest Guardian and escaped!")
    else:
        print("Game over! You ran out of HP.")


def describe_current_location(board: dict, character: dict) -> None:
    """
    Describe the character's current location on the board.

    :param board: a dictionary representing the board
    :param character: a dictionary representing the character
    :precondition: board must be a dictionary with non-negative integer tuple keys representing the
                   (X-coordinate,Y-coordinate) location on the board
    :precondition: character dictionary must contain X-coordinate and Y-coordinate
                   keys with non-negative integer values
    :postcondition: extract the string associated with the current tuple coordinates in board dictionary
    """
    coordinates = (character["X-coordinate"], character["Y-coordinate"])

    try:
        print(f"You are in ({character['X-coordinate']}, {character['Y-coordinate']}): {board[coordinates]}")
    except KeyError:
        print("Invalid location, not on board")


def get_user_choice() -> str:
    """
    Determine the user's chosen direction.

    :postcondition: convert user inputted integer to corresponding direction as a string of either 'North', 'South',
                    'East', or 'West'
    :return: a string representing chosen direction of 'North', 'South', 'East', or 'West'
    """
    directions = {1: "North", 2: "South", 3: "West", 4: "East"}

    while True:
        print("Choose a direction:")
        for key, value in directions.items():
            print(key, value)

        user_input = input("Enter the integer corresponding to your desired direction: \n")

        try:
            choice = int(user_input)
        except ValueError:
            print("Please enter an integer from 1 to 4.")
        else:
            if choice in directions:
                return directions[choice]
            else:
                print("That is not a valid direction. Try again.")


def validate_move(board: dict, character: dict, direction: str) -> bool:
    """
    Determine whether the user requested movement is within the boundaries of
    the board.

    :param board: a dictionary representing the board
    :param character: a dictionary representing the character
    :param direction: a string representing the direction of travel
    :precondition: board must be a dictionary with non-negative integer tuple keys representing the
                   (X-coordinate,Y-coordinate) location on the board
    :precondition: character dictionary must contain X-coordinate and Y-coordinate
                   keys with non-negative integer values
    :precondition: direction must be a string of either 'North', 'South', 'East', or 'West'
    :postcondition: determine whether the outcome coordinate tuple of the desired movement
                    direction is within the game board
    :return: True if coordinates after moving is within the board, else False

    >>> game_board = make_board(5, 5)
    >>> game_character = make_character("Luka")
    >>> validate_move(game_board, game_character, "North")
    False
    >>> validate_move(game_board, game_character, "East")
    True
    """
    character_copy = copy.deepcopy(character)

    if direction == "North":
        character_copy["X-coordinate"] -= 1
    elif direction == "South":
        character_copy["X-coordinate"] += 1
    elif direction == "East":
        character_copy["Y-coordinate"] += 1
    elif direction == "West":
        character_copy["Y-coordinate"] -= 1
    else:
        return False

    return (character_copy["X-coordinate"], character_copy["Y-coordinate"]) in board


def move_character(character: dict, direction: str) -> None:
    """
    Update the character X or Y coordinates value in the character dictionary based on the chosen direction.

    :param character: a dictionary representing the character
    :param direction: a string representing the desired direction of travel
    :precondition: character dictionary must contain X-coordinate and Y-coordinate
                   keys with non-negative integer values
    :precondition: direction must be a string of either 'North', 'South', 'East', or 'West'
    :postcondition: update the value within the character coordinates key based on chosen direction
    :raises ValueError: if direction is not string 'North', 'South', 'East', or 'West'

    >>> player = make_character("Luka")
    >>> move_character(player, "East")
    >>> player["Y-coordinate"]
    1
    >>> move_character(player, "South")
    >>> player["X-coordinate"]
    1
    """
    if direction == "North":
        character["X-coordinate"] -= 1
    elif direction == "South":
        character["X-coordinate"] += 1
    elif direction == "East":
        character["Y-coordinate"] += 1
    elif direction == "West":
        character["Y-coordinate"] -= 1
    else:
        raise ValueError("Direction must be North, South, West, or East")


def check_if_goal_attained(rows: int, columns: int, character: dict) -> bool:
    """
    Determine whether the character coordinates match the bottom-right corner coordinates of
    the board.

    :param rows: the number of rows in the board
    :param columns: the number of columns in the board
    :param character: a dictionary representing the character
    :precondition: rows must be an integer greater than 0
    :precondition: columns must be an integer greater than 0
    :precondition: character 'X-coordinate' key must be a non-negative integer
    :precondition: character 'Y-coordinate' key must be a non-negative integer
    :postcondition: determine if the character (X-coordinate, Y-coordinate) is at the bottom right coordinate
                    of the board.
    :return: True if the character coordinates match the bottom right coordinates of the board, else False

    >>> player = make_character("Luka")
    >>> check_if_goal_attained(5, 5, player)
    False
    >>> player["X-coordinate"] = 4
    >>> player["Y-coordinate"] = 4
    >>> check_if_goal_attained(5, 5, player)
    True
    """
    return (character["X-coordinate"], character["Y-coordinate"]) == (rows - 1, columns - 1)


def check_for_foes() -> bool:
    """
    Roll a random integer between 1 - 4 and check if that integer equals 1.

    :postcondition: 25% chance of returning True
    :return: True if random number chosen between 1 and 4 equals 1, else returns False
    """
    return random.randint(1, 4) == 1


def guessing_game(character: dict) -> bool:
    """
    Play a guessing game.

    Ask the user to guess a number in a level-based range. If the guess is wrong,
    reduce the character's current HP by 1.

    :param character: a dictionary representing the character
    :precondition: character must contain key 'Luck' and 'Current HP' and the value must be an integer greater than 0
    :postcondition: reduce 'Current HP' key in character value by 1 if the user guesses incorrectly
    :postcondition: determine the character key 'Current HP' value after guessing and
                    whether they guessed incorrectly or not
    :return: True if the player guesses correctly, else False
    """
    lower = 1
    upper = max(2, 6 - character["Luck"])
    secret_number = random.randint(lower, upper)

    print("A foe appears!")
    print(f"Guess a number between {lower} and {upper} inclusive.")

    while True:
        user_input = input("Enter your guess: ")

        try:
            guess = int(user_input)
        except ValueError:
            print("You must enter an integer. Try again")
            continue

        if not lower <= guess <= upper:
            print(f"Please enter a number between {lower} and {upper}.")
            continue

        if guess == secret_number:
            print(f"You're right!, you have {character['Current HP']} HP\n")
            return True

        elif guess < secret_number:
            character["Current HP"] -= 1
            print(f"Too low, the number was {secret_number}, "
                  f"you lose 1 HP, you now have {character['Current HP']} HP\n")
            return False

        else:
            character["Current HP"] -= 1
            print(f"Too high, the number was {secret_number}, "
                  f"you lose 1 HP, you now have {character['Current HP']} HP\n")
            return False

    return False


def is_alive(character: dict) -> bool:
    """
    Determine whether the value for 'Current HP' key in character dictionary is above 0.

    :param character: a dictionary representing the character
    :precondition: character must contain key 'Current HP' and the value must be an integer greater than 0
    :postcondition: determine if the character 'Current HP' key is greater than 0
    :return: True if the 'Current HP' key in character dictionary value is > 0 , else False

    >>> player = make_character("Luka")
    >>> is_alive(player)
    True
    >>> player["Current HP"] = 0
    >>> is_alive(player)
    False
    """
    return character["Current HP"] > 0


def gain_experience(character: dict) -> None:
    """
    Add experience to the player character and display progress.

    :param character: a dictionary representing the character
    :precondition: character must contain keys 'EXP' and 'Level'
    :postcondition: increase EXP by 1 and display current progress toward next level
    """
    character["EXP"] += 1

    threshold = get_exp_threshold(character)

    if threshold:
        print(f"You gained 1 EXP! ({character['EXP']}/{threshold} EXP)")
    else:
        print(f"You gained 1 EXP! (MAX LEVEL)")


def get_exp_threshold(character: dict) -> int | None:
    """
    Get the EXP required for the next level.

    :param character: a dictionary representing the character
    :precondition: character must contain 'Level'
    :postcondition: return the EXP needed for the next level if one exists
    :return: an integer EXP threshold or None if the character is at max level

    >>> player = make_character("Luka")
    >>> get_exp_threshold(player)
    3
    >>> player["Level"] = 3
    >>> get_exp_threshold(player) is None
    True
    """
    thresholds = {1: 3, 2: 6}
    return thresholds.get(character["Level"])


def has_leveled_up(character: dict) -> bool:
    """
    Determine whether the character has enough EXP to level up.

    :param character: a dictionary representing the character
    :precondition: character must contain keys 'Level' and 'EXP'
    :postcondition: determine whether the character meets the EXP requirement for the next level
    :return: True if the character should level up, else False

    >>> player = make_character("Luka")
    >>> player["EXP"] = 2
    >>> has_leveled_up(player)
    False
    >>> player["EXP"] = 3
    >>> has_leveled_up(player)
    True
    """
    thresholds = {1: 3, 2: 6}
    current_level = character["Level"]

    return current_level in thresholds and character["EXP"] >= thresholds[current_level]


def level_up(character: dict) -> None:
    """
    Increase the character's level and increase character level, max hp, current hp, and luck.

    :param character: a dictionary representing the character
    :precondition: character must contain 'Level', 'Max HP', 'Current HP', and 'Luck'
    :postcondition: increase level, max HP, current HP, and luck

    >>> player = make_character("Luka")
    >>> level_up(player)
    Luka leveled up to level 2 (Intermediate)!
    Max HP is now 10 and Luck is now 2.
    <BLANKLINE>
    >>> player["Level"]
    2
    """
    character["Level"] += 1

    if character["Level"] == 2:
        character["Level Name"] = "Intermediate"

    elif character["Level"] == 3:
        character["Level Name"] = "Forest Challenger"

    character["Max HP"] += 2
    character["Current HP"] = character["Max HP"]
    character["Luck"] += 1

    print(f"{character['Name']} leveled up to level {character['Level']} ({character['Level Name']})!")
    print(f"Max HP is now {character['Max HP']} and Luck is now {character['Luck']}.\n")


def potion_gamble(character: dict) -> bool:
    """
    Run a potion gamble challenge.

    The potion becomes more likely to help the player as the player's luck increases.

    :param character: a dictionary representing the character
    :precondition: character must contain 'Current HP', 'Max HP', and 'Luck'
    :postcondition: either heal the character or reduce the character's HP by 1
    :return: True if the potion helps, else False
    """
    print("You find a mysterious potion.")
    lower = 1
    upper = 4 - character["Luck"]
    outcome = random.randint(lower, upper)
    print(f"You have a 1 and {upper} chance of healing.")
    if outcome == 1:
        if character["Current HP"] < character["Max HP"]:
            character["Current HP"] += 1
        print(f"You are in luck, the potion helps you. HP is now {character['Current HP']}.")
        return True

    else:
        character["Current HP"] -= 1
        print(f"Luck is not on your side, the potion was poisonous. HP is now {character['Current HP']}.")
        return False


def choose_challenge() -> str:
    """
    Randomly choose a challenge type.

    :postcondition: randomly return one challenge type
    :return: the string 'enemy', 'potion' or 'dice'
    """
    return random.choice(["enemy", "potion", "dice"])


def final_boss_encounter(character: dict) -> bool:
    """
    Run the Forest Guardian's final multiple-choice riddle challenge.

    Repeatedly ask the player the riddle until they select the correct answer
    or run out of HP.

    :param character: a dictionary representing the character
    :precondition: character must contain 'Current HP'
    :postcondition: either allow the player to win the game or reduce HP after wrong answers
    :return: True if the player answers correctly, else False
    """
    correct_answer = 2

    while True:
        print("\nThe Forest Guardian rises before you.")
        print('"Answer my riddle, and you may leave this forest."\n')

        print("What walks on four legs in the morning,")
        print("two legs in the afternoon,")
        print("and one leg at night?\n")

        print("1. Dog")
        print("2. Human")
        print("3. Spider")
        print("4. Bird")
        print("5. Snake")

        user_input = input("\nEnter your choice (1-5): ")

        try:
            choice = int(user_input)
        except ValueError:
            print("Please enter an integer from 1 to 5.")
            continue

        if choice not in range(1, 6):
            print("That is not a valid option. Choose a number from 1 to 5.")
            continue

        if choice == correct_answer:
            print("\nThe Forest Guardian bows before you.")
            print("You solved the riddle and escaped the forest!")
            return True

        character["Current HP"] -= 2
        print("\nWrong. The Forest Guardian strikes you down.")
        print(f"You lose 2 HP and now have {character['Current HP']} HP.")

        if not is_alive(character):
            return False

        print("Try again...\n")

    return False


def display_map(rows: int, columns: int, character: dict) -> None:
    """
    Display the game board with the player and goal positions.

    :param rows: an integer representing the number of rows
    :param columns: an integer representing the number of columns
    :param character: a dictionary representing the character
    :precondition: rows and columns must be positive integers
    :precondition: character must contain 'X-coordinate' and 'Y-coordinate'
    :postcondition: print the board using [P] for the player and [G] for the goal
    """
    for row in range(rows):
        for column in range(columns):
            if row == character["X-coordinate"] and column == character["Y-coordinate"]:
                print("[P]", end="")
            elif row == rows - 1 and column == columns - 1:
                print("[G]", end="")
            else:
                print("[ ]", end="")
        print()


def describe_game():
    """
    Describe the game's setting and mechanics.

    :postcondition: print the introduction, goal, and how stats work
    """
    print("\n" + "=" * 60)
    print("Escape the Forest")
    print("=" * 60)
    print("You awaken in a dark and cursed forest.")
    print("Strange creatures wander between the trees, and mysterious potions")
    print("are hidden in the ground.\n")

    print("Your goal is to reach the far corner of the forest (9, 9)")
    print("and defeat the Forest Guardian to escape.\n")

    print("As you explore, you will encounter challenges:")
    print("- Enemies (guessing games)")
    print("- Potions (which may help or harm you)")
    print("- Dice games of chance\n")

    print("Leveling System:")
    print("- You gain EXP when you win encounters")
    print("- At certain EXP thresholds, you level up")
    print("- Leveling increases your Max HP and Luck\n")

    print("Luck System:")
    print("- Higher Luck makes enemy challenges easier")
    print("- The number range in guessing games becomes smaller\n")

    print("You begin at level 1 (Beginner)")
    print("Reach level 3 to have a chance of defeating the Forest Guardian.")
    print("Stay alive and escape the forest!")
    print("=" * 60 + "\n")


def dice_roll_challenge(character: dict) -> bool:
    """
    Run a dice roll challenge with luck-based retries.

    The player must guess whether the roll will be higher, lower, or equal
    to a given number. Luck determines how many retries they get.

    :param character: a dictionary representing the character
    :return: True if the player succeeds, else False
    """
    retries = character["Luck"] - 1
    given_number = random.randint(2, 5)

    while True:

        print("\nA forest spirit challenges you to a game of chance.")
        print(f"They rolled a dice and it landed on the number {given_number}.")
        print("\nYour turn to roll, will your roll be higher, lower, or equal to this number?")
        print("1. Higher")
        print("2. Lower")
        print("3. Equal")

        user_input = input("Enter your choice (1-3): ")

        try:
            choice = int(user_input)
        except ValueError:
            print("Please enter 1, 2, or 3.\n")
            continue

        if choice not in [1, 2, 3] or type(choice) != int:
            print("That is not a valid option.\n")
            continue

        roll = random.randint(1, 6)
        print(f"You rolled a {roll}.")

        if choice == 1 and roll > given_number:
            print("You guessed correctly!\n")
            return True

        if choice == 2 and roll < given_number:
            print("You guessed correctly!\n")
            return True

        if choice == 3 and roll == given_number:
            print("Perfect guess! You matched the number!\n")
            return True

        print("Wrong guess.")

        if retries > 0:
            retries -= 1
            print("Your luck gives you another chance...\n")
            continue

        character["Current HP"] -= 1
        print(f"You lose 1 HP and now have {character['Current HP']} HP.\n")
        return False

    return False


def main():
    """
    Drive the program.
    """
    game()


if __name__ == "__main__":
    main()