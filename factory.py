from basecar import BaseCar
from monstertruck import MonsterTruck
from racecar import RaceCar

car_classes = {
        'basecar': BaseCar,
        'monstertruck': MonsterTruck,
        'racecar': RaceCar
        # Future car types can be added here.
    }

def check_valid_car(car_type):
    """
    Check if the given car type is valid.
    
    Parameters:
    car_type (str): The type of car to check.
    
    Returns:
    bool: True if the car type is valid, False otherwise.
    """
    return car_type in car_classes.keys()

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
    return car_classes[car_type](start_x, start_y, direction)