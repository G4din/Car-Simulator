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

    def move_forward(self):
        """
        Move the car forward by 0.5 meters in the direction it is currently facing.
        """
        if self.direction == 'N':
            self.y += 0.5
        elif self.direction == 'S':
            self.y -= 0.5
        elif self.direction == 'E':
            self.x += 0.5
        elif self.direction == 'W':
            self.x -= 0.5
 
    def move_backward(self):
        """
        Move the car backward by 0.5 meters opposite to the direction it is currently facing.
        """
        if self.direction == 'N':
            self.y -= 0.5
        elif self.direction == 'S':
            self.y += 0.5
        elif self.direction == 'E':
            self.x -= 0.5
        elif self.direction == 'W':
            self.x += 0.5