from basecar import BaseCar

class MonsterTruck(BaseCar):
    def __init__(self, start_x, start_y, direction):
        """
        Initialize a new MonsterTruck instance.
        
        Parameters:
        start_x (int): The starting x-coordinate of the car.
        start_y (int): The starting y-coordinate of the car.
        direction (str): The initial direction the car is facing ('N', 'E', 'S', 'W').
        """
        super().__init__(start_x, start_y, direction)
        # Initialize any MonsterTruck-specific attributes here.

    # Placeholder for future MonsterTruck-specific methods
    # def some_monster_truck_specific_method(self):
    #     pass