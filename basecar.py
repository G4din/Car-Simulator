class BaseCar:
    def __init__(self, start_x, start_y, direction):
        """
        Initialize a new Car instance.
        
        Parameters:
        start_x (int): The starting x-coordinate of the car.
        start_y (int): The starting y-coordinate of the car.
        direction (str): The initial direction the car is facing ('N', 'E', 'S', 'W').
        """
        self.x = start_x
        self.y = start_y
        self.direction = direction
        self.directions = ['N', 'E', 'S', 'W']  # This order is important for rotations.

    def move_forward(self):
        """
        Move the car forward by 1 meter in the direction it is currently facing.
        """
        if self.direction == 'N':
            self.y += 1
        elif self.direction == 'S':
            self.y -= 1
        elif self.direction == 'E':
            self.x += 1
        elif self.direction == 'W':
            self.x -= 1
 
    def move_backward(self):
        """
        Move the car backward by 1 meter opposite to the direction it is currently facing.
        """
        if self.direction == 'N':
            self.y -= 1
        elif self.direction == 'S':
            self.y += 1
        elif self.direction == 'E':
            self.x -= 1
        elif self.direction == 'W':
            self.x += 1

    def rotate_left(self):
        """
        Rotate the car 90 degrees to the left (counter-clockwise).
        """
        current_index = self.directions.index(self.direction)
        
        self.direction = self.directions[(current_index - 1) % 4] # Modulo is important to ensure that the index wraps around to the beginning if necessary.

    def rotate_right(self):
        """
        Rotate the car 90 degrees to the right (clockwise).
        """
        current_index = self.directions.index(self.direction)
        self.direction = self.directions[(current_index + 1) % 4]