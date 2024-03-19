from room import Room
from factory import car_factory, check_valid_car
from simulation import Simulation

def get_room_size():
    """
    Prompt the user to enter the size of the room and return the width and length as integers.

    Returns:
    int: The width of the room.
    int: The length of the room.
    """
    while True:
        size_input = input("Enter the size of the room (X Y): ").split()
        if len(size_input) != 2:
            print("You must enter exactly two integers.")
            continue
        width, length = map(int, size_input)
        if width <= 0 or length <= 0:
            print("Room dimensions must be positive integers.")
            continue
        return width, length

def get_start_position(room_width, room_length):
    """
    Prompt the user to enter the starting position and heading of the car and return the x-coordinate, y-coordinate, and direction.
    
    Parameters:
    room_width (int): The width of the room.
    room_length (int): The length of the room.
    
    Returns:
    int: The starting x-coordinate of the car.
    int: The starting y-coordinate of the car.
    str: The initial direction the car is facing ('N', 'E', 'S', 'W').
    """
    while True:
        start_input = input("Enter the starting position and heading of the car (X Y N/E/S/W): ").split()
        if len(start_input) != 3:
            print("You must enter exactly two integers followed by one direction (N/E/S/W).")
            continue
        x, y = map(int, start_input[:2])
        direction = start_input[2].upper()
        if direction not in ('N', 'E', 'S', 'W'):
            print("Direction must be one of 'N', 'E', 'S', 'W'.")
            continue
        if x < 0 or y < 0 or x >= room_width or y >= room_length:
            print("Starting position must be within room boundaries.")
            continue
        return x, y, direction

def get_commands():
    """
    Prompt the user to enter the commands the car should execute and return the commands as a string.
     
    Returns:
    str: The commands the car should execute.
    """
    while True:
        commands = input("Enter commands the car should execute (F/B/L/R): ").upper()
        if not all(command in 'FBLR' for command in commands):
            print("Commands can only include 'F', 'B', 'L', or 'R'.")
            continue
        return commands
    
def get_car_type():
    """
    Prompt the user to enter the type of car to simulate and return the car type as a string.
    
    Returns:
    str: The type of car to simulate ('BaseCar', 'MonsterTruck' or 'RaceCar').
    """
    while True:
        car_type = input("Enter the type of car to simulate (BaseCar/MonsterTruck/RaceCar): ").strip().lower()
        if check_valid_car(car_type):
            return car_type
        print("Invalid car type. Please enter 'BaseCar', 'MonsterTruck' or 'RaceCar'.")

def main():
    """
    Run the car simulator program.
    """
    car_type = get_car_type()
    room_width, room_length = get_room_size()
    start_x, start_y, direction = get_start_position(room_width, room_length)
    commands = get_commands()

    car = car_factory(car_type, start_x, start_y, direction)

    room = Room(room_width, room_length)
    simulation = Simulation(room, car)

    result = simulation.run(commands)
    print(result)

if __name__ == "__main__":
    main()