"""
Luka Gajic
A01495410

Create a game.
"""
import random
import copy


def make_board(rows, columns):
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
        game_board = {(row, column): random.choice(descriptions) for row in range(rows) for column in range(columns)}

    return game_board


def make_character(name):
    """
    Initialize a character with the attributes of X-coordinate, Y-coordinate, and Current HP as keys in a dictionary.

    :postcondition: create a character at coordinates (0, 0), where the key 'X-coordinate' represents integer row value
                    key and 'Y-coordinate' key represents integer column value
    :postcondition: set the character key 'Current HP' to integer value 5
    :return: a dictionary with keys 'X-coordinate', 'Y-coordinate', and 'Current HP',
             where 'X-coordinate' stores the integer row position, 'Y-coordinate' stores the integer column position,
             and 'Current HP' stores the integer health value of the character

    >>> player = make_character()
    >>> player["X-coordinate"]
    0
    >>> player["Current HP"]
    5
    """
    return {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5,
            "Max HP": 5, "Luck": 1, "Level": 1, "EXP": 0, "Name": name}


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

        if valid_move:
            move_character(character, direction)
            describe_current_location(board, character)

            if check_if_goal_attained(rows, columns, character):
                if character["Level"] < 3:
                    print("You found the Forest Guardian, but you must be level 3 to challenge it.")
                else:
                    final_boss_encounter(character)
            else:
                there_is_a_challenge = check_for_foes()

                if there_is_a_challenge:
                    challenge_type = choose_challenge()

                    if challenge_type == "enemy":
                        won = guessing_game(character)
                    else:
                        won = potion_gamble(character)

                    if won:
                        gain_experience(character)
                        if has_leveled_up(character):
                            level_up(character)
        else:
            print(f"You are at position ({character['X-coordinate']}, {character['Y-coordinate']}) "
                  f"You cannot go that way. Try again.")

    if achieved_goal:
        print("Congratulations! You defeated the Forest Guardian and escaped!")
    else:
        print("Game over! You ran out of HP.")


def describe_current_location(board, character):
    """
    Describe the character's current location on the board.

    :param board: a dictionary representing the board
    :param character: a dictionary representing the character
    :precondition: board must be a dictionary with non-negative integer tuple keys representing the
                   (X-coordinate,Y-coordinate) location on the board
    :precondition: character dictionary must contain X-coordinate and Y-coordinate
                   keys with non-negative integer values
    :postcondition: extract the string associated with the current tuple coordinates in board dictionary

    >>> game_board = make_board(2, 2)
    >>> player = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5}
    >>> describe_current_location(game_board, player)
    You are in (0, 0): Empty room

    >>> game_board = make_board(2, 2)
    >>> player = {"X-coordinate": 5, "Y-coordinate": 5, "Current HP": 5}
    >>> describe_current_location(game_board, player)
    Invalid location, not on board
    """
    coordinates = (character["X-coordinate"], character["Y-coordinate"])

    try:
        print(f"You are in ({character['X-coordinate']}, {character['Y-coordinate']}): {board[coordinates]}")
    except KeyError:
        print("Invalid location, not on board")


def get_user_choice():
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

        user_input = input("Enter the integer corresponding to your desired direction: ")
        print()

        try:
            choice = int(user_input)
        except ValueError:
            print("Please enter an integer from 1 to 4.")
        else:
            if choice in directions:
                return directions[choice]
            else:
                print("That is not a valid direction. Try again.")


def validate_move(board, character, direction):
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


def move_character(character, direction):
    """
    Update the character X or Y coordinates value in the character dictionary based on the chosen direction.

    :param character: a dictionary representing the character
    :param direction: a string representing the desired direction of travel
    :precondition: character dictionary must contain X-coordinate and Y-coordinate
                   keys with non-negative integer values
    :precondition: direction must be a string of either 'North', 'South', 'East', or 'West'
    :postcondition: update the value within the character coordinates key based on chosen direction
    :raises ValueError: if direction is not string 'North', 'South', 'East', or 'West'

    >>> player = make_character()
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


def check_if_goal_attained(rows, columns, character):
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

    >>> player = make_character()
    >>> check_if_goal_attained(5, 5, player)
    False
    >>> player["X-coordinate"] = 4
    >>> player["Y-coordinate"] = 4
    >>> check_if_goal_attained(5, 5, player)
    True
    """
    return (character["X-coordinate"], character["Y-coordinate"]) == (rows - 1, columns - 1)


def check_for_foes():
    """
    Roll a random integer between 1 - 4 and check if that integer equals 1.

    :postcondition: 25% chance of returning True
    :return: True if random number chosen between 1 and 4 equals 1, else returns False
    """
    return random.randint(1, 4) == 1


def guessing_game(character):
    """
    Play a guessing game.

    Ask the user to guess a number from 1 to 5 inclusive. If the guess
    is incorrect, reduce "Current HP" key's value in character dictionary by 1.

    :param character: a dictionary representing the character
    :precondition: character must contain key 'Current HP' and the value must be an integer greater than 0
    :postcondition: reduce 'Current HP' key in character value by 1 if the user guesses incorrectly
    :postcondition: determine the character key 'Current HP' value after guessing and
                    whether they guessed incorrectly or not
    :return: character dictionary with updated 'Current HP' key's value
    """
    lower = 1
    upper = 5
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


def is_alive(character):
    """
    Determine whether the value for 'Current HP' key in character dictionary is above 0.

    :param character: a dictionary representing the character
    :precondition: character must contain key 'Current HP' and the value must be an integer greater than 0
    :postcondition: determine if the character 'Current HP' key is greater than 0
    :return: True if the 'Current HP' key in character dictionary value is > 0 , else False

    >>> player = make_character()
    >>> is_alive(player)
    True
    >>> player["Current HP"] = 0
    >>> is_alive(player)
    False
    """
    return character["Current HP"] > 0


def gain_experience(character):
    """
    Add experience to player character.

    :param character:
    :return:
    """
    character["EXP"] += 1


def has_leveled_up(character):
    """
    Determine whether the character has enough EXP to level up.

    :param character: a dictionary representing the character
    :return: True if the character should level up, else False
    """
    thresholds = {1: 3, 2: 6}
    current_level = character["Level"]

    return current_level in thresholds and character["EXP"] >= thresholds[current_level]


def level_up(character):
    """
    Increase the character's level and increase character level, max hp, current hp, and luck.

    :param character: a dictionary representing the character
    :postcondition: increase level, max HP, current HP, and luck
    """
    character["Level"] += 1
    character["Max HP"] += 2
    character["Current HP"] = character["Max HP"]
    character["Luck"] += 1

    print(f"{character['Name']} leveled up to level {character['Level']}!")
    print(f"Max HP is now {character['Max HP']} and Luck is now {character['Luck']}.")


def potion_gamble(character):
    """
    Run a potion gamble challenge.

    :param character: a dictionary representing the character
    :return: True after resolving the event
    """
    print("You find a mysterious potion.")
    outcome = random.randint(1, 3)

    if outcome == 1:
        if character["Current HP"] < character["Max HP"]:
            character["Current HP"] += 1
        print(f"The potion helps you. HP is now {character['Current HP']}.")
    else:
        character["Current HP"] -= 1
        print(f"The potion was poisonous. HP is now {character['Current HP']}.")

    return True


def choose_challenge():
    """
    Randomly choose a challenge type.

    :return: a string representing the chosen challenge
    """
    return random.choice(["enemy", "potion"])


def final_boss_encounter(character):
    """

    :param character:
    :return:
    """
    pass


def describe_game():
    """

    :return:
    """
    print("Game info")


def main():
    """
    Drive the program.
    """
    game()


if __name__ == "__main__":
    main()