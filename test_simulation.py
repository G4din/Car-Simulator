import unittest
from room import Room
from factory import car_factory
from basecar import BaseCar
from monstertruck import MonsterTruck
from simulation import Simulation

class TestRoom(unittest.TestCase):
    def test_room_init(self):
        room = Room(5, 7)
        self.assertEqual(room.width, 5)
        self.assertEqual(room.length, 7)

    def test_position_within_bounds(self):
        room = Room(5, 5)
        self.assertTrue(room.is_position_within_bounds(0, 0))
        self.assertTrue(room.is_position_within_bounds(4, 4))
        self.assertFalse(room.is_position_within_bounds(5, 5))

class TestCar(unittest.TestCase):
    def test_car_init(self):
        car = BaseCar(1, 1, 'N')
        self.assertEqual(car.x, 1)
        self.assertEqual(car.y, 1)
        self.assertEqual(car.direction, 'N')

    def test_car_movement(self):
        car = BaseCar(2, 2, 'N')
        car.move_forward()
        self.assertEqual((car.x, car.y), (2, 3))
        car.rotate_right()
        car.move_forward()
        self.assertEqual((car.x, car.y, car.direction), (3, 3, 'E'))

class TestCarFactory(unittest.TestCase):
    def test_base_car_creation(self):
        car = car_factory('basecar', 0, 0, 'N')
        self.assertIsInstance(car, BaseCar)
        self.assertNotIsInstance(car, MonsterTruck)

    def test_monster_truck_creation(self):
        car = car_factory('monstertruck', 0, 0, 'N')
        self.assertIsInstance(car, MonsterTruck)

class TestMonsterTruck(unittest.TestCase): #TODO: If wanted, add tests for MonsterTruck-specific methods
    def test_monster_truck_special_move(self):
        #car = MonsterTruck(0, 0, 'N')
        # Assuming special_move method changes the car's position in a unique way (e.g., moving two steps forward)
        # car.special_move()
        #expected_position = (0, 2)
        #self.assertEqual((car.x, car.y), expected_position)
        pass

class TestSimulation(unittest.TestCase):
    def test_simulation_success(self):
        room = Room(10, 10)
        car = BaseCar(5, 5, 'N')
        simulation = Simulation(room, car)
        result = simulation.run('FFLFF')
        self.assertTrue("Successful" in result)

    def test_simulation_failure(self):
        room = Room(3, 3)
        car = BaseCar(1, 1, 'N')
        simulation = Simulation(room, car)
        result = simulation.run('FFFF')
        self.assertTrue("Unsuccessful" in result)

if __name__ == '__main__':
    unittest.main()