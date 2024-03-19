from basecar import BaseCar

class RaceCar(BaseCar):
    def __init__(self, start_x, start_y, direction):
        """
        Initialize a new RaceCar instance.
        
        Parameters:
        start_x (int): The starting x-coordinate of the car.
        start_y (int): The starting y-coordinate of the car.
        direction (str): The initial direction the car is facing ('N', 'E', 'S', 'W').
        """
        super().__init__(start_x, start_y, direction)
        # Initialize any RaceCar-specific attributes here.

    def rotate_left(self):
        """
        Rotate the RaceCar to the right (clockwise) despite the 'left' command,
        overriding the standard left rotation.
        """
        super().rotate_right()

    def rotate_right(self):
        """
        Rotate the RaceCar to the left (counter-clockwise) despite the 'right' command,
        overriding the standard right rotation.
        """
        super().rotate_left()