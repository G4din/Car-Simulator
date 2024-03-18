# Car-Simulator

## Running the Simulation

`make run`

### How it Works
- **Room**: Defined by the user with width and length in meters. Represents the area in which the car can move.
- **Car**: Starts at a position and heading (N, E, S, or W) specified by the user. Moves according to the commands entered.
- **Commands**: The user inputs a series of commands for the car to follow:
- `F` - Move forward 1 meter.
- `B` - Move backward 1 meter.
- `L` - Rotate left 90 degrees.
- `R` - Rotate right 90 degrees.
- **Simulation**: The program simulates the movement of the car based on the commands and checks whether the car hits a wall.

## Input Format
- **Car Type**: A string for the car type that is going to be simulated (e.g., `MonsterTruck`).
- **Room Size**: Two integers representing the width and length of the room (e.g., `8 6`).
- **Starting Position and Heading**: Two integers for the starting position followed by a character for the heading (e.g., `2 3 N`).
- **Commands**: A string of characters without spaces representing the movement commands (e.g., `FFFRFFLBB`).

## Output
The simulation will output whether the execution was `Successful` or `Unsuccessful`. If successful, it will also display the end position and heading of the car. If unsuccessful, it will display that the car drove into a wall and where it hit the wall.

## Running the Tests

`make test`

## Assumptions made
- In the assignment, it is defined that there are multiple car types that the company has. The assignment states that the program should simulate, only, Monster Trucks. However, since it would be suitable for this company to simulate their other car types in the future, I made the assumption that the solution should be easy to scale up for more car types. Therefore, I made a factory pattern that allows new car types to be added in a simple manner. 
- The coordinates for the room (width and length) are indexed from 0 (e.g., 0-4 by 0-4).
- It is stated in the assignment that the room should be in whole meters, therefore, i made the assumption that the car should only be possible to start from whole meters as well.