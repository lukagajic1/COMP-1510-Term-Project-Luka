# COMP-1510-202610-Term-Project

## YOUR NAME:
Luka Gajic

## YOUR STUDENT NUMBER:
A01495410

## YOUR GITHUB NAME:
lukagajic1

---

# Overview

## Escape the Forest — Text-Based Adventure Game

Escape the Forest is a text-based adventure game where
the player must navigate through a dangerous forest,
survive random encounters, and defeat the Forest
Guardian to escape.

The player begins at level 1 (Beginner) and must
explore the map, gain experience through challenges,
and reach level 3 (Forest Challenger) before they can
defeat the final boss.

Throughout the game, the player encounters:

- Enemies (guessing games) <br/>
- Potions (risk/reward mechanics) <br/>
- Dice-based chance challenges

Your goal is to survive, grow stronger, and escape the forest.

---

# How to Run the Game

1. Make sure you have Python installed (Python 3.10+ recommended)

2. In your terminal, navigate to the project folder

3. Run the game: python game.py

4. Enter your name and begin playing

---

# Game Mechanics
Movement <br/>
Player moves using:
1. North
2. South
3. West
4. East

Movement is restricted within the board boundaries <br/>

Leveling System <br/>
Gain EXP from winning challenges <br/>
Level thresholds: <br/>
Level 1 → 2 needs 3 EXP <br/>
Level 2 → 3 needs 6 EXP <br/>

Level Names: <br/>
Level 1: Beginner <br/>
Level 2: Intermediate <br/>
Level 3: Forest Challenger <br/>

Win Condition <br/>
Reach the end of the map (9, 9) and solve the forest guardians riddle to escape the forest.<br/>
Must be Level 3 to defeat the Forest Guardian <br/>

Lose Condition <br/>
HP reaches 0

---

# Requirements

| **Requirement**                   | **Location**                                                                                                                                                                                                                              |
|-----------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **List and/or dictionary comprehensions used correctly** | `make_board` in game.py (lines 54–57) uses dictionary comprehension                                                                                                                                                                       |
| **Selection using if-statements**                        | `validate_move` in game.py uses selection to determine how character moves based on input lines 227-236                                                                                                                                   |
| **Repetition using for-loop and/or while loop**          | `game` function in game.py (line 101) and `display_map`function (line 581) use loops                                                                                                                                                      |
| **Membership operator used correctly**                   | `validate_move` in game.py (line 238) checks if coordinates exist in board                                                                                                                                                                |
| **Range function used correctly**                        | Used in `make_board` (line 56) and `display_map` (lines 581-582) in game.py                                                                                                                                                               |
| **One or more functions from itertools**                 | `product` used in `make_board` in game.py (line 56)                                                                                                                                                                                       |
| **Random module used correctly**                         | Used in `guessing_game`(line 326), `potion_gamble`(line 489), and `dice_roll_challenge`(line 641)                                                                                                                                         |
| **All output nicely formatted**                          | f-strings used in print statements throughout game.py (lines 106, 644, 663)                                                                                                                                                               |
| **Board creation using dictionary + tuples**             | `make_board` in game.py uses tuple keys for coordinates (lines 54-57)                                                                                                                                                                     |
| **Board is correct size & efficient**                    | `make_board` creates a 10x10 grid using dimensions in `game` (lines 91-93)                                                                                                                                                                |
| **Gameplay ends properly**                               | `check_if_goal_attained` checks when character is at end coordinates (9, 9) and `game` lines 115-120 makes sure level 3 is needed to begin final challenge, `game` also handles win (boss defeat) and lose (HP reaches 0) (lines 146-150) |
| **Movement + boundaries correct**                        | `validate_move` in game.py prevents out-of-bounds movement (line 238)                                                                                                                                                                     |
| **Varied + scalable challenges**                         | `guessing_game` (line 310), `potion_gamble`(line 475), and `dice_roll_challenge (line 628)                                                                                                                                                |
| **Mutability minimized**                                 | Only the character dictionary is mutated throughout gameplay                                                                                                                                                                              |
| **Mutable scope minimized**                              | Functions are modular and handle one task each                                                                                                                                                                                            |
| **Leveling system implemented correctly**                | `level_up` updates level, stats, and level name (lines 443-472)                                                                                                                                                                           |
| **EXP system implemented correctly**                     | `gain_experience` (lines 382-397), `get_exp_threshold` (lines 400-417), and `has_leveled_up` (lines 420-440)                                                                                                                              |
| **Final boss implemented**                               | `final_boss_encounter`(lines 513-567) handles end-game challenge                                                                                                                                                                          |
| **Use of loops in gameplay**                             | `game` (line 101) loop and challenge loops in `guessing_game` (line 331)                                                                                                                                                                  |
| **Exception handling for user input**                    | try/except blocks in input-based functions like `get_user_choice`(lines 190-193)                                                                                                                                                          |

---

