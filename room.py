class Room:
    def __init__(self, width, length):
        """
        Initialize a new Room instance.
        
        Parameters:
        width (int): The width of the room.
        length (int): The length of the room.
        """
        self.width = width
        self.length = length

    def is_position_within_bounds(self, x, y):
        """
        Check if given position (x, y) is within the room's boundaries.
        
        Parameters:
        x (int): The x-coordinate of the position.
        y (int): The y-coordinate of the position.
         
        Returns:
        bool: True if the position is within bounds, False otherwise.
        """
        return 0 <= x < self.width and 0 <= y < self.length