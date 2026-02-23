# Empire Builder

#### Video Demo:  <https://www.youtube.com/watch?v=fv_u0f-kZdk>

#### Description:
Empire Builder is a text-based strategy game where the player manages a civilization. The goal is to balance resources (Gold, Food), grow the population, and defend against barbarian raids.

The game involves strategic decision-making:
- **Economy:** Managing food production via farms and tax income from the population.
- **Survival:** Dealing with random events like famine and barbarian attacks.
- **Defense:** Building barracks and walls to protect the empire.

#### Files:

1.  **project.py**: The main entry point of the game. It contains the game loop, handles user input, and displays the game status using the `tabulate` library. It also includes the logic for parsing user commands via Regular Expressions (`re` library) and calculating battle mechanics.

2.  **nation.py**: Contains the `Nation` class. This class manages all the attributes of the empire (gold, food, population, buildings). It handles the logic for:
    - Collecting resources (with population growth mechanics).
    - Building structures (Farm, Barrack, Wall) with cost and balance checks.
    - Calculating resource consumption.

3.  **test_project.py**: Contains unit tests for the project using `pytest`. It tests:
    - Command parsing logic (Regex).
    - Resource calculation and population growth.
    - Building mechanics (successful builds and error handling for insufficient funds).
    - Defense and enemy power calculations.

4.  **requirements.txt**: Lists the external libraries required to run the project (`tabulate` and `pytest`).

Note: After recording this video demo, a minor structural refactoring was made to the code to fully comply with CS50's project.py structure requirements (moving the parsing and math functions from a separate utils.py file directly into project.py). The core logic, gameplay, and tests remain exactly the same as shown in the video.
