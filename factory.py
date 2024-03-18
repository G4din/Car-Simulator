from basecar import BaseCar
from monstertruck import MonsterTruck

def car_factory(car_type, start_x, start_y, direction):
    """
    Create a new car instance based on the given car type.

    Parameters:
    car_type (str): The type of car to create.
    start_x (int): The starting x-coordinate of the car.
    start_y (int): The starting y-coordinate of the car.
    direction (str): The initial direction the car is facing ('N', 'E', 'S', 'W').

    Returns:
    Car: A new car instance of the specified type.
    """
    car_classes = {
        'basecar': BaseCar,
        'monstertruck': MonsterTruck,
        # Future car types can be added here.
    }
    return car_classes[car_type](start_x, start_y, direction)