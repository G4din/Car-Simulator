class Simulation:
    def __init__(self, room, car):
        """
        Initialize a new Simulation instance.
        
        Parameters:
        room (Room): The room where the car is being simulated.
        car (Car): The car to simulate.
        """
        self.room = room
        self.car = car

    def is_within_bounds(self):
        """
        Check if the car is within the bounds of the room.
        
        Returns:
        bool: True if the car is within bounds, False otherwise.
        """
        return self.room.is_position_within_bounds(self.car.x, self.car.y)

    def run(self, commands):
        """
        Run the simulation with a series of commands.
        
        Parameters:
        commands (str): A string of commands (e.g., "FFFRFFLBB").
        
        Returns:
        str: The result of the simulation, indicating success or failure and the car's final state.
        """
        for command in commands:
            if command == 'F':
                self.car.move_forward()
            elif command == 'B':
                self.car.move_backward()
            elif command == 'L':
                self.car.rotate_left()
            elif command == 'R':
                self.car.rotate_right()
            
            if not self.is_within_bounds():
                return f"Unsuccessful: The car drove into the wall at position ({self.car.x}, {self.car.y})."

        return f"Successful: End position ({self.car.x}, {self.car.y}) facing {self.car.direction}."