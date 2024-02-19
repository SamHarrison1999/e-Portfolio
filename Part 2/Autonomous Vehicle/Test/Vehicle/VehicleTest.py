import unittest
from collections import deque
from unittest.mock import patch

from Main.Vehicle.Axel import Axel
from Main.Vehicle.Bonnet import Bonnet
from Main.Vehicle.Brake import Brake
from Main.Vehicle.Camera import Camera
from Main.Vehicle.Chassis import Chassis
from Main.Vehicle.Contact import Contact
from Main.Vehicle.Door import Door
from Main.Vehicle.Engine import Engine
from Main.Vehicle.EngineMode import EngineMode
from Main.Vehicle.FuelType import FuelType
from Main.Vehicle.Location import Location
from Main.Vehicle.Message import Message
from Main.Vehicle.Object import Object
from Main.Vehicle.Phone import Phone
from Main.Vehicle.Radio import Radio
from Main.Vehicle.RoadType import RoadType
from Main.Vehicle.Route import Route
from Main.Vehicle.Sensor import Sensor
from Main.Vehicle.Suspension import Suspension
from Main.Vehicle.TransmissionType import TransmissionType
from Main.Vehicle.Trunk import Trunk
from Main.Vehicle.Tyre import Tyre
from Main.Vehicle.Vehicle import *
from Main.Vehicle.Wheel import Wheel
from Main.Weather.Weather import Weather


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self._current_weather = Weather("Sunny", 25)
        self._auto_pilot_system = AutoPilot(True, self._current_weather, 30)
        self._body_type = BodyType.Coupe
        self._collision_detection_system = CollisionDetectionSystem(False, False, False)
        self._red = Colour(255, 0, 0)
        self._black = Colour(0, 0, 0)
        self._cruise_control = CruiseControl(False, 70, self._current_weather, 50)
        self._current_lane = 3
        self._vehicle_dimensions = {"Length (Meters)": 5, "Width (Meters)": 2, "Height (Meters)": 2, "Weight (Tons)": 2}
        self._drive_system = DriveSystem.AWD
        self._fuel = Fuel(FuelType.Diesel, 100, 50)
        self._current_location = Location(10, 50, 0, "Maple Drive", 4, RoadType.CRoad, False, 30)
        self._destination = Location(10, 60, 0, "Pine Lane", 4, RoadType.CRoad, False, 30)
        self._directions_to_destination = deque(
            ["In 500 yards turn left", "In 300 yards turn right", "In 2 miles you have reached your destination"])
        self._directions_to_destination_using_shortest_route = deque(
            ["In 1 mile turn left", "In 500 yards you have reached your destination"])
        self._directions_to_destination_using_quickest_route = deque(
            ["In 1.2 miles turn left", "In 200 yards you have reached your destination"])
        self._route = Route(10, 10, self._directions_to_destination)
        self._shortest_route = Route(1, 10, self._directions_to_destination_using_shortest_route)
        self._quickest_route = Route(10, 1, self._directions_to_destination_using_quickest_route)
        self._routes = [self._route, self._shortest_route, self._quickest_route]
        self._gps = GPS(self._current_location, self._destination, self._routes)
        self._emergency_contact = Contact("Emergency", "Contact", "+447987654321")
        self._drivers_phone = Phone("+447123456789", self._emergency_contact, [self._emergency_contact], [])
        self._car_radio = Radio("Capital", 95.8, None)
        self._infotainment_system = InfotainmentSystem(self._drivers_phone, self._car_radio, "English")
        self._lane_marking_detection_system = LaneMarkingDetectionSystem(5, 0)
        self._left_indicator = False
        self._logs = ["Car Unlocked", "Driver Authenticated", "Car Started", "Destination Set", "Accelerating",
                      "Decelerating", "Arrived"]
        self._make = "Audi"
        self._mileage = Mileage(40, 100000)
        self._model = "A4"
        self._hd_camera_quality = (1920, 1080)
        self._cone_camera = Camera(self._hd_camera_quality, deque(["Frame 1"]), "MP4")
        self._cone_sensor = Sensor("Cone Sensor")
        self._cone = Object("Cone", {"Length": 0.5, "Width": 0.2, "Height": 1}, 1, 5, 10)
        self._person_camera = Camera(self._hd_camera_quality, deque(["Frame 1"]), "MP4")
        self._person_sensor = Sensor("Person Sensor")
        self._person = Object("Person", {"Width": 0.1, "Height": 2}, 1, 5, 10)
        self._car_camera = Camera(self._hd_camera_quality, deque(), "MP4")
        self._car_sensor = Sensor("Car Sensor")
        self._object_detection_system = ObjectDetectionSystem(
            [self._cone_camera, self._person_camera, self._car_camera],
            [self._cone_sensor, self._person_sensor, self._car_sensor], [self._cone, self._person])
        self._axel = Axel(1, "Axel", self._black, "Audi", {"Length": 0.5, "Width": 1})
        self._bonnet = Bonnet(1, "Bonnet", self._red, "Audi", {"Length": 1, "Width": 1})
        self._front_left_brake = Brake(1, "Front Left Brake", self._black, "Audi", {"Length": 0.1, "Width": 0.1})
        self._front_right_brake = Brake(2, "Front Right Brake", self._black, "Audi", {"Length": 0.1, "Width": 0.1})
        self._rear_left_brake = Brake(3, "Rear Left Brake", self._black, "Audi", {"Length": 0.1, "Width": 0.1})
        self._rear_right_brake = Brake(4, "Rear Right Brake", self._black, "Audi", {"Length": 0.1, "Width": 0.1})
        self._chassis = Chassis(1, "Chassis", self._black, "Audi", {"Length": 1.5, "Width": 2})
        self._front_driver_side_door = Door(1, "Front Driver Side Door", self._red, "Audi", {"Length": 1, "Width": 1},
                                            True, True)
        self._front_passenger_side_door = Door(2, "Front Passenger Side Door", self._red, "Audi",
                                               {"Length": 1, "Width": 1}, True,
                                               True)
        self._rear_driver_side_door = Door(3, "Rear Driver Side Door", self._red, "Audi", {"Length": 1, "Width": 1},
                                           True, True)
        self._rear_passenger_side_door = Door(4, "Rear Passenger Side Door", self._red, "Audi",
                                              {"Length": 1, "Width": 1}, True,
                                              True)
        self._engine = Engine(1, "Engine", self._black, "Audi", {"Length": 0.5, "Width": 0.5, "Height": 0.5}, 2, 250,
                              12, 8,
                              EngineMode.Sport)
        self._suspension = Suspension(1, "Suspension", self._black, "Audi", {"Length": 1.5, "Width": 2})
        self._trunk = Trunk(1, "Trunk", self._red, "Audi", {"Length": 1, "Width": 1}, True, True)
        self._front_left_tyre = Tyre(1, "Front Left Tyre", self._black, "Audi", {"Diameter": 3, "Radius": 3}, 10, 50)
        self._front_right_tyre = Tyre(2, "Front Right Tyre", self._black, "Audi", {"Diameter": 3, "Radius": 3}, 10, 50)
        self._rear_left_tyre = Tyre(3, "Rear Left Tyre", self._black, "Audi", {"Diameter": 3, "Radius": 3}, 10, 50)
        self._rear_right_tyre = Tyre(4, "Rear Right Tyre", self._black, "Audi", {"Diameter": 3, "Radius": 3}, 10, 50)
        self._front_left_wheel = Wheel(1, "Front Left Wheel", self._black, "Audi", {"Diameter": 3, "Radius": 3})
        self._front_right_wheel = Wheel(2, "Front Right Wheel", self._black, "Audi", {"Diameter": 3, "Radius": 3})
        self._rear_left_wheel = Wheel(3, "Rear Left Wheel", self._black, "Audi", {"Diameter": 3, "Radius": 3})
        self._rear_right_wheel = Wheel(4, "Rear Right Wheel", self._black, "Audi", {"Diameter": 3, "Radius": 3})
        self._parts = [self._axel, self._bonnet, self._front_left_brake, self._front_right_brake, self._rear_left_brake,
                       self._rear_right_brake, self._chassis,
                       self._front_driver_side_door, self._front_passenger_side_door, self._rear_driver_side_door,
                       self._rear_passenger_side_door,
                       self._engine, self._suspension, self._trunk, self._front_left_tyre, self._front_right_tyre,
                       self._rear_left_tyre, self._rear_right_tyre,
                       self._front_left_wheel, self._front_right_wheel, self._rear_left_wheel, self._rear_right_wheel]
        self._registration_number = "AB24CDE"
        self._right_indicator = False
        self._security_system = SecuritySystem(True, False)
        self._speed = Speed(150, 5, 20)
        self._steering = Steering(0)
        self._transmission = Transmission(1, "Transmission", self._black, "Audi",
                                          {"Length": 0.5, "Width": 0.5, "Height": 0.5},
                                          TransmissionType.MANUAL, 6, 3)
        self._year = 2024
        self._vehicle = Vehicle(self._auto_pilot_system, self._body_type, self._collision_detection_system, self._red,
                                self._cruise_control,
                                self._current_lane, self._vehicle_dimensions, self._drive_system, self._fuel, self._gps,
                                self._infotainment_system,
                                self._lane_marking_detection_system, self._left_indicator, self._logs, self._make,
                                self._mileage, self._model,
                                self._object_detection_system, self._parts, self._registration_number,
                                self._right_indicator, self._security_system,
                                self._speed, self._steering, self._transmission, self._year)

    def tearDown(self):
        self._current_weather = None
        self._auto_pilot_system = None
        self._body_type = None
        self._collision_detection_system = None
        self._red = None
        self._black = None
        self._cruise_control = None
        self._current_lane = None
        self._vehicle_dimensions = None
        self._drive_system = None
        self._fuel = None
        self._current_location = None
        self._destination = None
        self._directions_to_destination = None
        self._directions_to_destination_using_shortest_route = None
        self._directions_to_destination_using_quickest_route = None
        self._route = None
        self._shortest_route = None
        self._quickest_route = None
        self._routes = None
        self._gps = None
        self._emergency_contact = None
        self._drivers_phone = None
        self._car_radio = None
        self._infotainment_system = None
        self._lane_marking_detection_system = None
        self._left_indicator = None
        self._logs = None
        self._make = None
        self._mileage = None
        self._model = None
        self._hd_camera_quality = None
        self._cone_camera = None
        self._cone_sensor = None
        self._cone = None
        self._person_camera = None
        self._person_sensor = None
        self._person = None
        self._car_camera = None
        self._car_sensor = None
        self._object_detection_system = None
        self._axel = None
        self._bonnet = None
        self._front_left_brake = None
        self._front_right_brake = None
        self._rear_left_brake = None
        self._rear_right_brake = None
        self._chassis = None
        self._front_driver_side_door = None
        self._front_passenger_side_door = None
        self._rear_driver_side_door = None
        self._rear_passenger_side_door = None
        self._engine = None
        self._suspension = None
        self._trunk = None
        self._front_left_tyre = None
        self._front_right_tyre = None
        self._rear_left_tyre = None
        self._rear_right_tyre = None
        self._front_left_wheel = None
        self._front_right_wheel = None
        self._rear_left_wheel = None
        self._rear_right_wheel = None
        self._parts = None
        self._registration_number = None
        self._right_indicator = None
        self._security_system = None
        self._speed = None
        self._steering = None
        self._transmission = None
        self._year = None
        self._vehicle = None

    def testValueErrorRaisedIfAnyOfTheVehiclesDimensionsAreBelowZero(self):
        """Testing a value error is raised if any of the vehicles dimensions aren't valid"""
        with self.assertRaises(ValueError):
            self._vehicle = Vehicle(self._auto_pilot_system, self._body_type, self._collision_detection_system,
                                    self._red, self._cruise_control, self._current_lane, {"Height": -1},
                                    self._drive_system, self._fuel,
                                    self._gps, self._infotainment_system, self._lane_marking_detection_system,
                                    self._left_indicator, self._logs, self._make,
                                    self._mileage, self._model, self._object_detection_system, self._parts,
                                    self._registration_number,
                                    self._right_indicator, self._security_system, self._speed, self._steering,
                                    self._transmission, self._year)

    def testValueErrorRaisedIfTheCurrentLaneIsNotAvailable(self):
        """Testing a value error is raised if the current lane the vehicle is in is not an available lane"""
        with self.assertRaises(ValueError):
            self._vehicle = Vehicle(self._auto_pilot_system, self._body_type, self._collision_detection_system,
                                    self._red, self._cruise_control, -1, self._vehicle_dimensions, self._drive_system,
                                    self._fuel,
                                    self._gps, self._infotainment_system, self._lane_marking_detection_system,
                                    self._left_indicator, self._logs, self._make,
                                    self._mileage, self._model, self._object_detection_system, self._parts,
                                    self._registration_number,
                                    self._right_indicator, self._security_system, self._speed, self._steering,
                                    self._transmission, self._year)

    def testValueErrorRaisedIfTheVehicleHasNoMake(self):
        """Testing a value error is raised if the vehicle has no make"""
        with self.assertRaises(ValueError):
            self._vehicle = Vehicle(self._auto_pilot_system, self._body_type, self._collision_detection_system,
                                    self._red, self._cruise_control, self._current_lane, self._vehicle_dimensions,
                                    self._drive_system,
                                    self._fuel,
                                    self._gps, self._infotainment_system, self._lane_marking_detection_system,
                                    self._left_indicator, self._logs, "",
                                    self._mileage, self._model, self._object_detection_system, self._parts,
                                    self._registration_number,
                                    self._right_indicator, self._security_system, self._speed, self._steering,
                                    self._transmission, self._year)

    def testValueErrorRaisedIfTheVehicleHasNoModelName(self):
        """Testing a value error is raised if the vehicle has no model name"""
        with self.assertRaises(ValueError):
            self._vehicle = Vehicle(self._auto_pilot_system, self._body_type, self._collision_detection_system,
                                    self._red,
                                    self._cruise_control,
                                    self._current_lane, self._vehicle_dimensions, self._drive_system, self._fuel,
                                    self._gps,
                                    self._infotainment_system,
                                    self._lane_marking_detection_system, self._left_indicator, self._logs, self._make,
                                    self._mileage, "",
                                    self._object_detection_system, self._parts, self._registration_number,
                                    self._right_indicator, self._security_system,
                                    self._speed, self._steering, self._transmission, self._year)

    def testValueErrorRaisedIfTheVehiclesRegistrationNumberIsNotValid(self):
        """Testing a value error is raised if the registration number is not valid"""
        with self.assertRaises(ValueError):
            self._vehicle = Vehicle(self._auto_pilot_system, self._body_type, self._collision_detection_system,
                                    self._red,
                                    self._cruise_control,
                                    self._current_lane, self._vehicle_dimensions, self._drive_system, self._fuel,
                                    self._gps,
                                    self._infotainment_system,
                                    self._lane_marking_detection_system, self._left_indicator, self._logs, self._make,
                                    self._mileage, self._model,
                                    self._object_detection_system, self._parts, "1234567",
                                    self._right_indicator, self._security_system,
                                    self._speed, self._steering, self._transmission, self._year)

    def testValueErrorRaisedIfTheVehiclesWasMadeInTheFuture(self):
        """Testing a value error is raised if the year the vehicle was made is in the future"""
        with self.assertRaises(ValueError):
            self._vehicle = Vehicle(self._auto_pilot_system, self._body_type, self._collision_detection_system,
                                    self._red,
                                    self._cruise_control,
                                    self._current_lane, self._vehicle_dimensions, self._drive_system, self._fuel,
                                    self._gps,
                                    self._infotainment_system,
                                    self._lane_marking_detection_system, self._left_indicator, self._logs, self._make,
                                    self._mileage, self._model,
                                    self._object_detection_system, self._parts, self._registration_number,
                                    self._right_indicator, self._security_system,
                                    self._speed, self._steering, self._transmission, 9500)

    def testVehicleWithoutParts(self):
        """Testing a vehicle without any parts"""
        self._vehicle = Vehicle(self._auto_pilot_system, self._body_type, self._collision_detection_system, self._red,
                                self._cruise_control,
                                self._current_lane, self._vehicle_dimensions, self._drive_system, self._fuel, self._gps,
                                self._infotainment_system,
                                self._lane_marking_detection_system, self._left_indicator, self._logs, self._make,
                                self._mileage, self._model,
                                self._object_detection_system, None, self._registration_number,
                                self._right_indicator, self._security_system,
                                self._speed, self._steering, self._transmission, self._year)
        self.assertEqual(self._vehicle.parts, [])

    def testVehicleWithoutLogs(self):
        """Testing a vehicle without any parts"""
        self._vehicle = Vehicle(self._auto_pilot_system, self._body_type, self._collision_detection_system, self._red,
                                self._cruise_control,
                                self._current_lane, self._vehicle_dimensions, self._drive_system, self._fuel, self._gps,
                                self._infotainment_system,
                                self._lane_marking_detection_system, self._left_indicator, None, self._make,
                                self._mileage, self._model,
                                self._object_detection_system, self._parts, self._registration_number,
                                self._right_indicator, self._security_system,
                                self._speed, self._steering, self._transmission, self._year)
        self.assertEqual(self._vehicle.logs, [])

    def testAutoPilotGetter(self):
        """Testing the autopilot system is returned when you call the autopilot getter"""
        with self.subTest("Auto Pilot Status"):
            self.assertEqual(self._vehicle.auto_pilot.enabled, True)
        with self.subTest("Distance From Closest Car"):
            self.assertEqual(self._vehicle.auto_pilot.following_distance, 30)
        with self.subTest("Recommended Following Distance"):
            self.assertEqual(self._vehicle.auto_pilot.weather.recommended_following_distance(), 2)
        with self.subTest("Weather Condition"):
            self.assertEqual(self._vehicle.auto_pilot.weather.weather_condition, "Sunny")
        with self.subTest("Temperature"):
            self.assertEqual(self._vehicle.auto_pilot.weather.temperature, 25)
        with self.subTest("Weather Object"):
            self.assertEqual(self._vehicle.auto_pilot.weather.__str__(),
                             "Weather Condition: Sunny\n"
                             "Temperature: 25 degrees\n"
                             "Recommended Following Distance: 2 Meters")
        with self.subTest("Auto Pilot Object"):
            self.assertEqual(self._vehicle.auto_pilot.__str__(),
                             "AutoPilot: Enabled\n"
                             "Distance From The Closest Car: 30 meters\n"
                             "Weather Condition: Sunny\n"
                             "Temperature: 25 degrees\n"
                             "Recommended Following Distance: 2 Meters")

    def testAutoPilotSetter(self):
        """Testing you can update the autopilot object by calling the autopilot setter"""
        self._vehicle.auto_pilot = AutoPilot(False, Weather("Raining", 5), 10)
        with self.subTest("Auto Pilot Status"):
            self.assertEqual(self._vehicle.auto_pilot.enabled, False)
        with self.subTest("Distance From Closest Car"):
            self.assertEqual(self._vehicle.auto_pilot.following_distance, 10)
        with self.subTest("Recommended Following Distance"):
            self.assertEqual(self._vehicle.auto_pilot.weather.recommended_following_distance(), 4)
        with self.subTest("Weather Condition"):
            self.assertEqual(self._vehicle.auto_pilot.weather.weather_condition, "Raining")
        with self.subTest("Temperature"):
            self.assertEqual(self._vehicle.auto_pilot.weather.temperature, 5)
        with self.subTest("Weather Object"):
            self.assertEqual(self._vehicle.auto_pilot.weather.__str__(),
                             "Weather Condition: Raining\n"
                             "Temperature: 5 degrees\n"
                             "Recommended Following Distance: 4 Meters")
        with self.subTest("Auto Pilot Object"):
            self.assertEqual(self._vehicle.auto_pilot.__str__(),
                             "AutoPilot: Disabled\n"
                             "Distance From The Closest Car: 10 meters\n"
                             "Weather Condition: Raining\n"
                             "Temperature: 5 degrees\n"
                             "Recommended Following Distance: 4 Meters")

    def testBodyTypeGetter(self):
        """Testing the body type is returned when you call the body type getter"""
        self.assertEqual(self._vehicle.body_type, BodyType.Coupe)

    def testBodyTypeSetter(self):
        """Testing you can update the vehicles body type by calling the set body type function"""
        self._vehicle.body_type = BodyType.Convertible
        self.assertEqual(self._vehicle.body_type, BodyType.Convertible)

    def testCollisionDetectionSystemGetter(self):
        """Testing the collision detection system is returned when you call the collision detection system getter"""
        with self.subTest("Collision Status"):
            self.assertEqual(self._vehicle.collision_detection_system.collision_occurred, False)
        with self.subTest("Handbrake Status"):
            self.assertEqual(self._vehicle.collision_detection_system.handbrake_engaged, False)
        with self.subTest("Hazard Light Status"):
            self.assertEqual(self._vehicle.collision_detection_system.hazard_lights_turned_on, False)
        with self.subTest("Collision Detection System"):
            self.assertEqual(self._vehicle.collision_detection_system.__str__(),
                             "No Collision Detected\n"
                             "Handbrake not engaged\n"
                             "Hazard Lights Off")

    def testCollisionDetectionSystemSetter(self):
        """Testing you can update the collision detection object by calling the collision detection system setter"""
        self._vehicle.collision_detection_system = CollisionDetectionSystem(True, True, True)
        with self.subTest("Collision Status"):
            self.assertEqual(self._vehicle.collision_detection_system.collision_occurred, True)
        with self.subTest("Handbrake Status"):
            self.assertEqual(self._vehicle.collision_detection_system.handbrake_engaged, True)
        with self.subTest("Hazard Light Status"):
            self.assertEqual(self._vehicle.collision_detection_system.hazard_lights_turned_on, True)
        with self.subTest("Collision Detection System"):
            self.assertEqual(self._vehicle.collision_detection_system.__str__(),
                             "Collision Detected\n"
                             "Handbrake Engaged\n"
                             "Hazard Lights On")

    def testColourGetter(self):
        """Testing the vehicles colour is returned when you call the colour getter"""
        with self.subTest("Red"):
            self.assertEqual(self._vehicle.colour.red, 255)
        with self.subTest("Green"):
            self.assertEqual(self._vehicle.colour.green, 0)
        with self.subTest("Blue"):
            self.assertEqual(self._vehicle.colour.blue, 0)
        with self.subTest("Colour"):
            self.assertEqual(self._vehicle.colour.__str__(), "RGB(255, 0, 0)\n"
                                                             "CMYK(0, 100, 100, 0)\n"
                                                             "#FF0000")

    def testColourSetter(self):
        """Testing you can update the vehicles colour by calling the colour setter"""
        self._vehicle.colour = Colour(255, 255, 255)
        with self.subTest("Red"):
            self.assertEqual(self._vehicle.colour.red, 255)
        with self.subTest("Green"):
            self.assertEqual(self._vehicle.colour.green, 255)
        with self.subTest("Blue"):
            self.assertEqual(self._vehicle.colour.blue, 255)
        with self.subTest("Colour"):
            self.assertEqual(self._vehicle.colour.__str__(), "RGB(255, 255, 255)\n"
                                                             "CMYK(0, 0, 0, 0)\n"
                                                             "#FFFFFF")

    def testCruiseControlGetter(self):
        """Testing the cruise control system is returned when you call the cruise control getter"""
        with self.subTest("Cruise Control Activated"):
            self.assertEqual(self._vehicle.cruise_control.activated, False)
        with self.subTest("Target Speed"):
            self.assertEqual(self._vehicle.cruise_control.target_speed, 70)
        with self.subTest("Recommended Following Distance"):
            self.assertEqual(self._vehicle.cruise_control.following_distance, 50)
        with self.subTest("Distance From Closest Car"):
            self.assertEqual(self._vehicle.cruise_control.weather.recommended_following_distance(), 2)
        with self.subTest("Weather Condition"):
            self.assertEqual(self._vehicle.cruise_control.weather.weather_condition, "Sunny")
        with self.subTest("Temperature"):
            self.assertEqual(self._vehicle.cruise_control.weather.temperature, 25)
        with self.subTest("Weather Object"):
            self.assertEqual(self._vehicle.cruise_control.weather.__str__(),
                             "Weather Condition: Sunny\n"
                             "Temperature: 25 degrees\n"
                             "Recommended Following Distance: 2 Meters")
        with self.subTest("Cruise Control Object"):
            self.assertEqual(self._vehicle.cruise_control.__str__(),
                             "Cruise Control Deactivated\n"
                             "Target Speed: 70MPH\n"
                             "Recommended Following Distance: 2 Meters\n"
                             "Distance From The Closest Car: 50 Meters")

    def testCruiseControlSetter(self):
        """Testing you can update the cruise control object by calling the cruise control setter"""
        self._vehicle.cruise_control = CruiseControl(True, 50, Weather("Raining", 10), 10)
        with self.subTest("Cruise Control Activated"):
            self.assertEqual(self._vehicle.cruise_control.activated, True)
        with self.subTest("Target Speed"):
            self.assertEqual(self._vehicle.cruise_control.target_speed, 50)
        with self.subTest("Recommended Following Distance"):
            self.assertEqual(self._vehicle.cruise_control.following_distance, 10)
        with self.subTest("Distance From Closest Car"):
            self.assertEqual(self._vehicle.cruise_control.weather.recommended_following_distance(), 4)
        with self.subTest("Weather Condition"):
            self.assertEqual(self._vehicle.cruise_control.weather.weather_condition, "Raining")
        with self.subTest("Temperature"):
            self.assertEqual(self._vehicle.cruise_control.weather.temperature, 10)
        with self.subTest("Weather Object"):
            self.assertEqual(self._vehicle.cruise_control.weather.__str__(),
                             "Weather Condition: Raining\n"
                             "Temperature: 10 degrees\n"
                             "Recommended Following Distance: 4 Meters")
        with self.subTest("Cruise Control Object"):
            self.assertEqual(self._vehicle.cruise_control.__str__(),
                             "Cruise Control Activated\n"
                             "Target Speed: 50MPH\n"
                             "Recommended Following Distance: 4 Meters\n"
                             "Distance From The Closest Car: 10 Meters")

    def testCurrentLaneGetter(self):
        """Testing the current lane is returned when you call the current lane getter"""
        self.assertEqual(self._vehicle.current_lane, 3)

    def testCurrentLaneSetter(self):
        """Testing you can update the lane the vehicle is in when you call the current lane setter"""
        self._vehicle.current_lane = 2
        self.assertEqual(self._vehicle.current_lane, 2)

    def testValueErrorRaisedIfTheCurrentLaneSetUsingTheCurrentLaneSetterIsNotAvailable(self):
        """Testing a value error is raised if you set the current lane to a lane that isn't available"""
        with self.assertRaises(ValueError):
            self._vehicle.current_lane = 10

    def testVehicleDimensionsGetter(self):
        """Testing the vehicle dimensions are returned when you call the dimensions getter"""
        self.assertEqual(self._vehicle.dimensions,
                         {"Length (Meters)": 5,
                          "Width (Meters)": 2,
                          "Height (Meters)": 2,
                          "Weight (Tons)": 2})

    def testVehicleDimensionsSetter(self):
        """Testing you can update the vehicles dimensions by calling the vehicle dimensions setter"""
        self._vehicle.dimensions = {"Length (Meters)": 4,
                                    "Width (Meters)": 3,
                                    "Height (Meters)": 1.5,
                                    "Weight (Tons)": 1}
        self.assertEqual(self._vehicle.dimensions,
                         {"Length (Meters)": 4,
                          "Width (Meters)": 3,
                          "Height (Meters)": 1.5,
                          "Weight (Tons)": 1})

    def testValueErrorRaisedIfAnyOfTheVehiclesDimensionsSetUsingTheVehicleDimensionsSetterAreBelowZero(self):
        """Testing a value error is raised if you set any of the vehicles dimensions to a negative number"""
        with self.assertRaises(ValueError):
            self._vehicle.dimensions = {"Length (Meters)": 4,
                                        "Width (Meters)": 3,
                                        "Height (Meters)": 1.5,
                                        "Weight (Tons)": -1}

    def testDriveSystemGetter(self):
        """Testing the drive system is returned when you call the drive system getter"""
        self.assertEqual(self._vehicle.drive_system.value, "AWD")

    def testDriveSystemSetter(self):
        """Testing you can update the drive system by calling the drive system setter"""
        self._vehicle.drive_system = DriveSystem.FourByFour
        self.assertEqual(self._vehicle.drive_system.value, "4x4")

    def testFuelGetter(self):
        """Testing the vehicles fuel information is returned when you call the fuel getter"""
        with self.subTest("Fuel Type"):
            self.assertEqual(self._vehicle.fuel.fuel_type, FuelType.Diesel)
        with self.subTest("Fuel Remaining"):
            self.assertEqual(self._vehicle.fuel.fuel_remaining, 50)
        with self.subTest("Fuel Capacity"):
            self.assertEqual(self._vehicle.fuel.capacity, 100)
        with self.subTest("Fuel Object"):
            self.assertEqual(self._vehicle.fuel.__str__(),
                             "Fuel Type: Diesel\n"
                             "Fuel Tank Capacity: 100L\n"
                             "Amount of fuel remaining: 50L")

    def testFuelSetter(self):
        """Testing you can update the vehicles fuel information by calling the fuel setter"""
        self._vehicle.fuel = Fuel(FuelType.Unleaded, 70, 30)
        with self.subTest("Fuel Type"):
            self.assertEqual(self._vehicle.fuel.fuel_type, FuelType.Unleaded)
        with self.subTest("Fuel Remaining"):
            self.assertEqual(self._vehicle.fuel.fuel_remaining, 30)
        with self.subTest("Fuel Capacity"):
            self.assertEqual(self._vehicle.fuel.capacity, 70)
        with self.subTest("Fuel Object"):
            self.assertEqual(self._vehicle.fuel.__str__(),
                             "Fuel Type: Unleaded\n"
                             "Fuel Tank Capacity: 70L\n"
                             "Amount of fuel remaining: 30L")

    def testGPSGetter(self):
        """Testing the GPS Object is returned when you call the GPS Getter"""
        self.assertEqual(self._vehicle.gps.__str__(), "Current Location:\n"
                                                      "Longitude: 10\n"
                                                      "Latitude: 50\n"
                                                      "Altitude: 0 Meters\n"
                                                      "Road Name: Maple Drive\n"
                                                      "Number Of Lanes: 4 lanes\n"
                                                      "Road Type: C Road\n"
                                                      "Traffic Status: No Traffic ahead\n"
                                                      "Speed Limit: 30MPH\n"
                                                      "Destination:\n"
                                                      "Longitude: 10\n"
                                                      "Latitude: 60\n"
                                                      "Altitude: 0 Meters\n"
                                                      "Road Name: Pine Lane\n"
                                                      "Number Of Lanes: 4 lanes\n"
                                                      "Road Type: C Road\n"
                                                      "Traffic Status: No Traffic ahead\n"
                                                      "Speed Limit: 30MPH\n"
                                                      "Routes:\n"
                                                      "Route 1:\n"
                                                      "Distance to destination: 10 Miles\n"
                                                      "Duration to destination: 10 Minuets\n"
                                                      "Directions:\n"
                                                      "In 500 yards turn left\n"
                                                      "In 300 yards turn right\n"
                                                      "In 2 miles you have reached your destination\n"
                                                      "Route 2:\n"
                                                      "Distance to destination: 1 Miles\n"
                                                      "Duration to destination: 10 Minuets\n"
                                                      "Directions:\n"
                                                      "In 1 mile turn left\n"
                                                      "In 500 yards you have reached your destination\n"
                                                      "Route 3:\n"
                                                      "Distance to destination: 10 Miles\n"
                                                      "Duration to destination: 1 Minuets\n"
                                                      "Directions:\n"
                                                      "In 1.2 miles turn left\n"
                                                      "In 200 yards you have reached your destination")

    def testGPSSetter(self):
        """Testing the GPS Object is returned when you call the GPS Getter"""
        current_location = Location(0, 0, 0, "M25", 6, RoadType.Motorway, False, 70)
        destination = Location(20, 0, 0, "M11", 6, RoadType.Motorway, False, 70)
        route = Route(20, 30, deque(["In 20 miles take the exit and join the M11"]))
        self._vehicle.gps = GPS(current_location, destination, [route])
        self.assertEqual(self._vehicle.gps.__str__(),
                         "Current Location:\n"
                         "Longitude: 0\n"
                         "Latitude: 0\n"
                         "Altitude: 0 Meters\n"
                         "Road Name: M25\n"
                         "Number Of Lanes: 6 lanes\n"
                         "Road Type: Motorway\n"
                         "Traffic Status: No Traffic ahead\n"
                         "Speed Limit: 70MPH\n"
                         "Destination:\n"
                         "Longitude: 20\n"
                         "Latitude: 0\n"
                         "Altitude: 0 Meters\n"
                         "Road Name: M11\n"
                         "Number Of Lanes: 6 lanes\n"
                         "Road Type: Motorway\n"
                         "Traffic Status: No Traffic ahead\n"
                         "Speed Limit: 70MPH\n"
                         "Routes:\n"
                         "Route 1:\n"
                         "Distance to destination: 20 Miles\n"
                         "Duration to destination: 30 Minuets\n"
                         "Directions:\n"
                         "In 20 miles take the exit and join the M11")

    def testInfotainmentSystemGetter(self):
        """Testing the vehicles infotainment system is returned when you call the infotainment system getter"""
        with self.subTest("Phone number"):
            self.assertEqual(self._vehicle.infotainment_system.phone.phone_number, "+447123456789")
        with self.subTest("Emergency Contact Name"):
            self.assertEqual(self._vehicle.infotainment_system.phone.emergency_contact.first_name, "Emergency")
        with self.subTest("Emergency Contact Last Name"):
            self.assertEqual(self._vehicle.infotainment_system.phone.emergency_contact.last_name, "Contact")
        with self.subTest("Emergency Contact Contact Number"):
            self.assertEqual(self._vehicle.infotainment_system.phone.emergency_contact.contact_number, "+447987654321")
        with self.subTest("Emergency Contact Object"):
            self.assertEqual(self._vehicle.infotainment_system.phone.emergency_contact.__str__(),
                             "First Name: Emergency\n"
                             "Last Name: Contact\n"
                             "Contact Number: +447987654321")
        with self.subTest("Messages"):
            self.assertEqual(self._vehicle.infotainment_system.phone.messages, [])
        with self.subTest("Contact First Name"):
            self.assertEqual(self._vehicle.infotainment_system.phone.contacts[0].first_name, "Emergency")
        with self.subTest("Contact Last Name"):
            self.assertEqual(self._vehicle.infotainment_system.phone.contacts[0].last_name, "Contact")
        with self.subTest("Contact Contact Number"):
            self.assertEqual(self._vehicle.infotainment_system.phone.contacts[0].contact_number, "+447987654321")
        with self.subTest("Contacts"):
            self.assertEqual(self._vehicle.infotainment_system.phone.contacts[0].__str__(),
                             "First Name: Emergency\n"
                             "Last Name: Contact\n"
                             "Contact Number: +447987654321")
        with self.subTest("Phone Object"):
            self.assertEqual(self._vehicle.infotainment_system.phone.__str__(),
                             "Phone Number: +447123456789\n"
                             "Emergency Contact:\n"
                             "First Name: Emergency\n"
                             "Last Name: Contact\n"
                             "Contact Number: +447987654321\n"
                             "Contacts:\n"
                             "Contact 1:\n"
                             "First Name: Emergency\n"
                             "Last Name: Contact\n"
                             "Contact Number: +447987654321\n"
                             "Messages:")
        with self.subTest("Radio Station Name"):
            self.assertEqual(self._vehicle.infotainment_system.radio.station_name, "Capital")
        with self.subTest("Radio Station FM NUmber"):
            self.assertEqual(self._vehicle.infotainment_system.radio.frequency_modulation, 95.8)
        with self.subTest("Radio Station AM Number"):
            self.assertEqual(self._vehicle.infotainment_system.radio.amplitude_modulation, 0)
        with self.subTest("Radio Station Object"):
            self.assertEqual(self._vehicle.infotainment_system.radio.__str__(),
                             "Station Name: Capital\n"
                             "FM: 95.8\n"
                             "AM: 0Hz")
        with self.subTest("Infotainment System Language"):
            self.assertEqual(self._vehicle.infotainment_system.language, "English")
        with self.subTest("Infotainment System Object"):
            self.assertEqual(self._vehicle.infotainment_system.__str__(),
                             "Phone Number: +447123456789\n"
                             "Emergency Contact:\n"
                             "First Name: Emergency\n"
                             "Last Name: Contact\n"
                             "Contact Number: +447987654321\n"
                             "Contacts:\n"
                             "Contact 1:\n"
                             "First Name: Emergency\n"
                             "Last Name: Contact\n"
                             "Contact Number: +447987654321\n"
                             "Messages:\n"
                             "Radio:\n"
                             "Station Name: Capital\n"
                             "FM: 95.8\n"
                             "AM: 0Hz\n"
                             "Language: English")

    def testInfotainmentSystemSetter(self):
        """Testing you can update the vehicles infotainment system by calling the infotainment system setter"""
        self._vehicle.infotainment_system = InfotainmentSystem(
            Phone("+447506530821", Contact("Test", "Contact", "+447123456789"),
                  [Contact("Test", "Contact", "+447123456789"), Contact("Second", "Contact", "+447987654321")], [
                      Message(Contact("Message", "Sender", "+447506530821"),
                              Contact("Second", "Contact", "+447987654321"),
                              "Test Text Message")]),
            Radio("Kiss", 100, None), "English")
        with self.subTest("Phone number"):
            self.assertEqual(self._vehicle.infotainment_system.phone.phone_number, "+447506530821")
        with self.subTest("Emergency Contact Name"):
            self.assertEqual(self._vehicle.infotainment_system.phone.emergency_contact.first_name, "Test")
        with self.subTest("Emergency Contact Last Name"):
            self.assertEqual(self._vehicle.infotainment_system.phone.emergency_contact.last_name, "Contact")
        with self.subTest("Emergency Contact Contact Number"):
            self.assertEqual(self._vehicle.infotainment_system.phone.emergency_contact.contact_number, "+447123456789")
        with self.subTest("Emergency Contact Object"):
            self.assertEqual(self._vehicle.infotainment_system.phone.emergency_contact.__str__(),
                             "First Name: Test\n"
                             "Last Name: Contact\n"
                             "Contact Number: +447123456789")
        with self.subTest("Messages Sender First Name"):
            self.assertEqual(self._vehicle.infotainment_system.phone.messages[0].sender.first_name, "Message")
        with self.subTest("Messages Sender Last Name"):
            self.assertEqual(self._vehicle.infotainment_system.phone.messages[0].sender.last_name, "Sender")
        with self.subTest("Messages Sender Contact Number"):
            self.assertEqual(self._vehicle.infotainment_system.phone.messages[0].sender.contact_number, "+447506530821")
        with self.subTest("Messages Receiver First Name"):
            self.assertEqual(self._vehicle.infotainment_system.phone.messages[0].receiver.first_name, "Second")
        with self.subTest("Messages Receiver Last Name"):
            self.assertEqual(self._vehicle.infotainment_system.phone.messages[0].receiver.last_name, "Contact")
        with self.subTest("Messages Receiver Contact Number"):
            self.assertEqual(self._vehicle.infotainment_system.phone.messages[0].receiver.contact_number,
                             "+447987654321")
        with self.subTest("Message Body"):
            self.assertEqual(self._vehicle.infotainment_system.phone.messages[0].message, "Test Text Message")
        with self.subTest("Message Object"):
            self.assertEqual(self._vehicle.infotainment_system.phone.messages[0].__str__(),
                             "Sender:\n"
                             "First Name: Message\n"
                             "Last Name: Sender\n"
                             "Contact Number: +447506530821\n"
                             "Receiver:\n"
                             "First Name: Second\n"
                             "Last Name: Contact\n"
                             "Contact Number: +447987654321\n"
                             "Message:\n"
                             "Test Text Message")
        with self.subTest("First Contact First Name"):
            self.assertEqual(self._vehicle.infotainment_system.phone.contacts[0].first_name, "Test")
        with self.subTest("First Contact Last Name"):
            self.assertEqual(self._vehicle.infotainment_system.phone.contacts[0].last_name, "Contact")
        with self.subTest("First Contact Contact Number"):
            self.assertEqual(self._vehicle.infotainment_system.phone.contacts[0].contact_number, "+447123456789")
        with self.subTest("First Contact"):
            self.assertEqual(self._vehicle.infotainment_system.phone.contacts[0].__str__(),
                             "First Name: Test\n"
                             "Last Name: Contact\n"
                             "Contact Number: +447123456789")
        with self.subTest("Second Contact First Name"):
            self.assertEqual(self._vehicle.infotainment_system.phone.contacts[1].first_name, "Second")
        with self.subTest("Second Contact Last Name"):
            self.assertEqual(self._vehicle.infotainment_system.phone.contacts[1].last_name, "Contact")
        with self.subTest("Second Contact Contact Number"):
            self.assertEqual(self._vehicle.infotainment_system.phone.contacts[1].contact_number, "+447987654321")
        with self.subTest("Second Contacts"):
            self.assertEqual(self._vehicle.infotainment_system.phone.contacts[1].__str__(),
                             "First Name: Second\n"
                             "Last Name: Contact\n"
                             "Contact Number: +447987654321")
        with self.subTest("Phone Object"):
            self.assertEqual(self._vehicle.infotainment_system.phone.__str__(),
                             "Phone Number: +447506530821\n"
                             "Emergency Contact:\n"
                             "First Name: Test\n"
                             "Last Name: Contact\n"
                             "Contact Number: +447123456789\n"
                             "Contacts:\n"
                             "Contact 1:\n"
                             "First Name: Test\n"
                             "Last Name: Contact\n"
                             "Contact Number: +447123456789\n"
                             "Contact 2:\n"
                             "First Name: Second\n"
                             "Last Name: Contact\n"
                             "Contact Number: +447987654321\n"
                             "Messages:\n"
                             "Message 1:\n"
                             "Sender:\n"
                             "First Name: Message\n"
                             "Last Name: Sender\n"
                             "Contact Number: +447506530821\n"
                             "Receiver:\n"
                             "First Name: Second\n"
                             "Last Name: Contact\n"
                             "Contact Number: +447987654321\n"
                             "Message:\n"
                             "Test Text Message")
        with self.subTest("Radio Station Name"):
            self.assertEqual(self._vehicle.infotainment_system.radio.station_name, "Kiss")
        with self.subTest("Radio Station FM NUmber"):
            self.assertEqual(self._vehicle.infotainment_system.radio.frequency_modulation, 100)
        with self.subTest("Radio Station AM Number"):
            self.assertEqual(self._vehicle.infotainment_system.radio.amplitude_modulation, 0)
        with self.subTest("Radio Station Object"):
            self.assertEqual(self._vehicle.infotainment_system.radio.__str__(), "Station Name: Kiss\n"
                                                                                "FM: 100\n"
                                                                                "AM: 0Hz")
        with self.subTest("Infotainment System Language"):
            self.assertEqual(self._vehicle.infotainment_system.language, "English")
        with self.subTest("Infotainment System Object"):
            self.assertEqual(self._vehicle.infotainment_system.__str__(),
                             "Phone Number: +447506530821\n"
                             "Emergency Contact:\n"
                             "First Name: Test\n"
                             "Last Name: Contact\n"
                             "Contact Number: +447123456789\n"
                             "Contacts:\n"
                             "Contact 1:\n"
                             "First Name: Test\n"
                             "Last Name: Contact\n"
                             "Contact Number: +447123456789\n"
                             "Contact 2:\n"
                             "First Name: Second\n"
                             "Last Name: Contact\n"
                             "Contact Number: +447987654321\n"
                             "Messages:\n"
                             "Message 1:\n"
                             "Sender:\n"
                             "First Name: Message\n"
                             "Last Name: Sender\n"
                             "Contact Number: +447506530821\n"
                             "Receiver:\n"
                             "First Name: Second\n"
                             "Last Name: Contact\n"
                             "Contact Number: +447987654321\n"
                             "Message:\n"
                             "Test Text Message\n"
                             "Radio:\n"
                             "Station Name: Kiss\n"
                             "FM: 100\n"
                             "AM: 0Hz\n"
                             "Language: English")

    def testLaneMarkingDetectionSystemGetter(self):
        """Testing the lane marking detection system is returned when you call the lane marking detection getter"""
        with self.subTest("Left Distance"):
            self.assertEqual(self._vehicle.lane_marking_detection_system.left_distance, 5)
        with self.subTest("Right Distance"):
            self.assertEqual(self._vehicle.lane_marking_detection_system.right_distance, 0)
        with self.subTest("Lane Marking Detection System"):
            self.assertEqual(self._vehicle.lane_marking_detection_system.__str__(),
                             "Distance from left lane marking: 5 Meters\n"
                             "Distance from right lane marking: 0 Meters\n"
                             "In Lane")

    def testLaneMarkingDetectionSystemSetter(self):
        """Testing the lane marking detection setter"""
        self._vehicle.lane_marking_detection_system = LaneMarkingDetectionSystem(-10, 10)
        with self.subTest("Left Distance"):
            self.assertEqual(self._vehicle.lane_marking_detection_system.left_distance, -10)
        with self.subTest("Right Distance"):
            self.assertEqual(self._vehicle.lane_marking_detection_system.right_distance, 10)
        with self.subTest("Lane Marking Detection System"):
            self.assertEqual(self._vehicle.lane_marking_detection_system.__str__(),
                             "Distance from left lane marking: -10 Meters\n"
                             "Distance from right lane marking: 10 Meters\n"
                             "Not In Lane")

    def testLeftIndicatorGetter(self):
        """Testing the left indicator status is returned when you call the left indicator getter"""
        self.assertEqual(self._vehicle.left_indicator, False)

    def testLeftIndicatorSetter(self):
        """Testing you can update the left indicator status by calling the left indicator setter"""
        self._vehicle.left_indicator = True
        self.assertEqual(self._vehicle.left_indicator, True)

    def testLogsGetter(self):
        """Testing the logs are returned when you call the logs getter"""
        self.assertEqual(self._vehicle.logs,
                         ['Car Unlocked',
                          'Driver Authenticated',
                          'Car Started',
                          'Destination Set',
                          'Accelerating',
                          'Decelerating',
                          'Arrived'])

    def testLogsSetter(self):
        """Testing you can update the vehicles logs by calling the logs setter"""
        self._vehicle.logs = ["Test"]
        self.assertEqual(self._vehicle.logs, ["Test"])

    def testLogsSetterWithNone(self):
        """Testing when you update the logs to none"""
        self._vehicle.logs = None
        self.assertEqual(self._vehicle.logs, [])

    def testMakeGetter(self):
        """Testing the vehicle manufacturer is returned when you call the make getter"""
        self.assertEqual(self._vehicle.make, "Audi")

    def testMakeSetter(self):
        """Testing you can update the vehicles brand name by calling the make setter"""
        self._vehicle.make = "BMW"
        self.assertEqual(self._vehicle.make, "BMW")

    def testValueErrorRaisedIfTheVehicleMakeSetUsingTheMakeSetterIsAnEmptyString(self):
        """Testing a value error is raised if you try to set the make of vehicle to an empty string"""
        with self.assertRaises(ValueError):
            self._vehicle.make = ""

    def testMileageGetter(self):
        """Testing the vehicles mileage is returned when you call the mileage getter"""
        with self.subTest("MPG"):
            self.assertEqual(self._vehicle.mileage.miles_per_gallon, 40)
        with self.subTest("Current Mileage"):
            self.assertEqual(self._vehicle.mileage.current_mileage, 100000)
        with self.subTest("Mileage Object"):
            self.assertEqual(self._vehicle.mileage.__str__(), "MPG: 40\nCurrent Mileage: 100000 Miles")

    def testMileageSetter(self):
        """Testing you can update the vehicles mileage by calling the mileage setter"""
        self._vehicle.mileage = Mileage(60, 120000)
        with self.subTest("MPG"):
            self.assertEqual(self._vehicle.mileage.miles_per_gallon, 60)
        with self.subTest("Current Mileage"):
            self.assertEqual(self._vehicle.mileage.current_mileage, 120000)
        with self.subTest("Mileage Object"):
            self.assertEqual(self._vehicle.mileage.__str__(), "MPG: 60\nCurrent Mileage: 120000 Miles")

    def testModelGetter(self):
        """Testing the model name is returned when you call the model getter"""
        self.assertEqual(self._vehicle.model, "A4")

    def testModelSetter(self):
        """Testing the model name can be updated by calling the model setter"""
        self._vehicle.model = "R8"
        self.assertEqual(self._vehicle.model, "R8")

    def testValueErrorRaisedIfTheVehicleModelNameSetUsingTheModelSetterIsAnEmptyString(self):
        """Testing a value error is raised if you try to set the vehicle model name to an empty string"""
        with self.assertRaises(ValueError):
            self._vehicle.model = ""

    def testObjectDetectionSystemGetter(self):
        """Testing the vehicles object detection system is returned when you call the object detection system getter"""
        with self.subTest("Cone Camera"):
            with self.subTest("Cone Camera Quality"):
                self.assertEqual(self._vehicle.object_detection_system.cameras[0].pixels, (1920, 1080))
            with self.subTest("Cone Camera Frames Recorded"):
                self.assertEqual(self._vehicle.object_detection_system.cameras[0].frames, deque(["Frame 1"]))
            with self.subTest("Cone Camera File Format"):
                self.assertEqual(self._vehicle.object_detection_system.cameras[0].file_format, "MP4")
            with self.subTest("Cone Camera Object"):
                self.assertEqual(self._vehicle.object_detection_system.cameras[0].__str__(),
                                 "Camera Quality: 1920 x 1080\n"
                                 "Frames:\n"
                                 "Frame 1\n"
                                 "File Name: File.MP4")
        with self.subTest("Person Camera"):
            with self.subTest("Person Camera Quality"):
                self.assertEqual(self._vehicle.object_detection_system.cameras[1].pixels, (1920, 1080))
            with self.subTest("Person Camera Frames Recorded"):
                self.assertEqual(self._vehicle.object_detection_system.cameras[1].frames, deque(["Frame 1"]))
            with self.subTest("Person Camera File Format"):
                self.assertEqual(self._vehicle.object_detection_system.cameras[1].file_format, "MP4")
            with self.subTest("Person Camera Object"):
                self.assertEqual(self._vehicle.object_detection_system.cameras[1].__str__(),
                                 "Camera Quality: 1920 x 1080\n"
                                 "Frames:\n"
                                 "Frame 1\n"
                                 "File Name: File.MP4")
        with self.subTest("Car Camera"):
            with self.subTest("Car Camera Quality"):
                self.assertEqual(self._vehicle.object_detection_system.cameras[2].pixels, (1920, 1080))
            with self.subTest("Car Camera Frames Recorded"):
                self.assertEqual(self._vehicle.object_detection_system.cameras[2].frames, deque())
            with self.subTest("Car Camera File Format"):
                self.assertEqual(self._vehicle.object_detection_system.cameras[2].file_format, "MP4")
            with self.subTest("Car Camera Object"):
                self.assertEqual(self._vehicle.object_detection_system.cameras[2].__str__(),
                                 "Camera Quality: 1920 x 1080\n"
                                 "Frames:\n"
                                 "File Name: File.MP4")
        with self.subTest("Cone Sensor"):
            with self.subTest("Cone Sensor Type"):
                self.assertEqual(self._vehicle.object_detection_system.sensors[0].sensor_type, "Cone Sensor")
            with self.subTest("Cone Sensor Object"):
                self.assertEqual(self._vehicle.object_detection_system.sensors[0].__str__(), "Sensor: Cone Sensor")
        with self.subTest("Person Sensor"):
            with self.subTest("Person Sensor Type"):
                self.assertEqual(self._vehicle.object_detection_system.sensors[1].sensor_type, "Person Sensor")
            with self.subTest("Person Sensor Object"):
                self.assertEqual(self._vehicle.object_detection_system.sensors[1].__str__(), "Sensor: Person Sensor")
        with self.subTest("Car Sensor"):
            with self.subTest("Car Sensor Type"):
                self.assertEqual(self._vehicle.object_detection_system.sensors[2].sensor_type, "Car Sensor")
            with self.subTest("Car Sensor Object"):
                self.assertEqual(self._vehicle.object_detection_system.sensors[2].__str__(), "Sensor: Car Sensor")
        with self.subTest("Cone"):
            with self.subTest("Cone Object Name"):
                self.assertEqual(self._vehicle.object_detection_system.objects_detected[0].name, "Cone")
            with self.subTest("Cone Dimensions"):
                self.assertEqual(self._vehicle.object_detection_system.objects_detected[0].dimensions,
                                 {"Length": 0.5, "Width": 0.2, "Height": 1})
            with self.subTest("Lane Cone Is In"):
                self.assertEqual(self._vehicle.object_detection_system.objects_detected[0].lane_object_is_in, 1)
            with self.subTest("Distance To Cone"):
                self.assertEqual(self._vehicle.object_detection_system.objects_detected[0].distance_to_object, 5)
            with self.subTest("Time Until Impact With Cone"):
                self.assertEqual(
                    self._vehicle.object_detection_system.objects_detected[0].time_until_impact_with_object, 10)
            with self.subTest("Cone Object"):
                self.assertEqual(self._vehicle.object_detection_system.objects_detected[0].__str__(),
                                 "Object Name: Cone\n"
                                 "Object Dimensions:\n"
                                 "Length: 0.5 Meters\n"
                                 "Width: 0.2 Meters\n"
                                 "Height: 1 Meters\n"
                                 "Object in Lane 1\n"
                                 "Distance to object: 5 Meters\n"
                                 "Time until impact with object at current speed: 10 Seconds")
        with self.subTest("Person"):
            with self.subTest("Person Object Name"):
                self.assertEqual(self._vehicle.object_detection_system.objects_detected[1].name, "Person")
            with self.subTest("Person Dimensions"):
                self.assertEqual(self._vehicle.object_detection_system.objects_detected[1].dimensions,
                                 {"Width": 0.1, "Height": 2})
            with self.subTest("Lane Person Is In"):
                self.assertEqual(self._vehicle.object_detection_system.objects_detected[1].lane_object_is_in, 1)
            with self.subTest("Distance To Person"):
                self.assertEqual(self._vehicle.object_detection_system.objects_detected[1].distance_to_object, 5)
            with self.subTest("Time Until Impact With Person"):
                self.assertEqual(
                    self._vehicle.object_detection_system.objects_detected[1].time_until_impact_with_object, 10)
            with self.subTest("Person Object"):
                self.assertEqual(self._vehicle.object_detection_system.objects_detected[1].__str__(),
                                 "Object Name: Person\n"
                                 "Object Dimensions:\n"
                                 "Width: 0.1 Meters\n"
                                 "Height: 2 Meters\n"
                                 "Object in Lane 1\n"
                                 "Distance to object: 5 Meters\n"
                                 "Time until impact with object at current speed: 10 Seconds")
        with self.subTest("Object Detection System Object"):
            self.assertEqual(self._vehicle.object_detection_system.__str__(),
                             "Cameras:\n"
                             "Camera 1:\n"
                             "Camera Quality: 1920 x 1080\n"
                             "Frames:\n"
                             "Frame 1\n"
                             "File Name: File.MP4\n"
                             "Camera 2:\n"
                             "Camera Quality: 1920 x 1080\n"
                             "Frames:\n"
                             "Frame 1\n"
                             "File Name: File.MP4\n"
                             "Camera 3:\n"
                             "Camera Quality: 1920 x 1080\n"
                             "Frames:\n"
                             "File Name: File.MP4\n"
                             "Sensors:\n"
                             "Sensor 1:\n"
                             "Sensor: Cone Sensor\n"
                             "Sensor 2:\n"
                             "Sensor: Person Sensor\n"
                             "Sensor 3:\n"
                             "Sensor: Car Sensor\n"
                             "Objects Detected:\n"
                             "Object 1:\nObject Name: Cone\n"
                             "Object Dimensions:\n"
                             "Length: 0.5 Meters\n"
                             "Width: 0.2 Meters\n"
                             "Height: 1 Meters\n"
                             "Object in Lane 1\n"
                             "Distance to object: 5 Meters\n"
                             "Time until impact with object at current speed: 10 Seconds\n"
                             "Object 2:\n"
                             "Object Name: Person\n"
                             "Object Dimensions:\n"
                             "Width: 0.1 Meters\n"
                             "Height: 2 Meters\n"
                             "Object in Lane 1\n"
                             "Distance to object: 5 Meters\n"
                             "Time until impact with object at current speed: 10 Seconds\n")

    def testObjectDetectionSystemSetter(self):
        """Testing you can update the object detection system by calling the object detection system setter"""
        self._vehicle.object_detection_system = ObjectDetectionSystem([], [], [])
        with self.subTest("Cameras"):
            self.assertEqual(self._vehicle.object_detection_system.cameras, [])
        with self.subTest("Sensors"):
            self.assertEqual(self._vehicle.object_detection_system.sensors, [])
        with self.subTest("Objects"):
            self.assertEqual(self._vehicle.object_detection_system.cameras, [])
        with self.subTest("Object Detection System"):
            self.assertEqual(self._vehicle.object_detection_system.__str__(), "Cameras:\n"
                                                                              "Sensors:\n"
                                                                              "Objects Detected:\n")

    def testPartsGetter(self):
        """Testing a list of the parts that make up the vehicle are returned when you call the parts getter"""
        with self.subTest("Axel ID"):
            self.assertEqual(self._vehicle.parts[0].part_id, 1)
        with self.subTest("Bonnet ID"):
            self.assertEqual(self._vehicle.parts[1].part_id, 1)
        with self.subTest("Front Left Brake ID"):
            self.assertEqual(self._vehicle.parts[2].part_id, 1)
        with self.subTest("Front Right Brake ID"):
            self.assertEqual(self._vehicle.parts[3].part_id, 2)
        with self.subTest("Rear Left Brake ID"):
            self.assertEqual(self._vehicle.parts[4].part_id, 3)
        with self.subTest("Rear Right Brake ID"):
            self.assertEqual(self._vehicle.parts[5].part_id, 4)
        with self.subTest("Chassis ID"):
            self.assertEqual(self._vehicle.parts[6].part_id, 1)
        with self.subTest("Front Driver Side Door ID"):
            self.assertEqual(self._vehicle.parts[7].part_id, 1)
        with self.subTest("Front Passenger Side Door ID"):
            self.assertEqual(self._vehicle.parts[8].part_id, 2)
        with self.subTest("Rear Driver Side Door ID"):
            self.assertEqual(self._vehicle.parts[9].part_id, 3)
        with self.subTest("Rear Passenger Side Door ID"):
            self.assertEqual(self._vehicle.parts[10].part_id, 4)
        with self.subTest("Engine ID"):
            self.assertEqual(self._vehicle.parts[11].part_id, 1)
        with self.subTest("Suspension ID"):
            self.assertEqual(self._vehicle.parts[12].part_id, 1)
        with self.subTest("Trunk ID"):
            self.assertEqual(self._vehicle.parts[13].part_id, 1)
        with self.subTest("Front Left Tyre ID"):
            self.assertEqual(self._vehicle.parts[14].part_id, 1)
        with self.subTest("Front Right Tyre ID"):
            self.assertEqual(self._vehicle.parts[15].part_id, 2)
        with self.subTest("Rear Left Tyre ID"):
            self.assertEqual(self._vehicle.parts[16].part_id, 3)
        with self.subTest("Rear Right Tyre ID"):
            self.assertEqual(self._vehicle.parts[17].part_id, 4)
        with self.subTest("Front Left Wheel ID"):
            self.assertEqual(self._vehicle.parts[18].part_id, 1)
        with self.subTest("Front Right Wheel ID"):
            self.assertEqual(self._vehicle.parts[19].part_id, 2)
        with self.subTest("Rear Left Wheel ID"):
            self.assertEqual(self._vehicle.parts[20].part_id, 3)
        with self.subTest("Rear Right Wheel ID"):
            self.assertEqual(self._vehicle.parts[21].part_id, 4)
        with self.subTest("Axel Name"):
            self.assertEqual(self._vehicle.parts[0].name, "Axel")
        with self.subTest("Bonnet Name"):
            self.assertEqual(self._vehicle.parts[1].name, "Bonnet")
        with self.subTest("Front Left Brake Name"):
            self.assertEqual(self._vehicle.parts[2].name, "Front Left Brake")
        with self.subTest("Front Right Brake Name"):
            self.assertEqual(self._vehicle.parts[3].name, "Front Right Brake")
        with self.subTest("Rear Left Brake Name"):
            self.assertEqual(self._vehicle.parts[4].name, "Rear Left Brake")
        with self.subTest("Rear Right Brake Name"):
            self.assertEqual(self._vehicle.parts[5].name, "Rear Right Brake")
        with self.subTest("Chassis Name"):
            self.assertEqual(self._vehicle.parts[6].name, "Chassis")
        with self.subTest("Front Driver Side Door Name"):
            self.assertEqual(self._vehicle.parts[7].name, "Front Driver Side Door")
        with self.subTest("Front Passenger Side Door Name"):
            self.assertEqual(self._vehicle.parts[8].name, "Front Passenger Side Door")
        with self.subTest("Rear Driver Side Door Name"):
            self.assertEqual(self._vehicle.parts[9].name, "Rear Driver Side Door")
        with self.subTest("Rear Passenger Side Door Name"):
            self.assertEqual(self._vehicle.parts[10].name, "Rear Passenger Side Door")
        with self.subTest("Engine Name"):
            self.assertEqual(self._vehicle.parts[11].name, "Engine")
        with self.subTest("Suspension Name"):
            self.assertEqual(self._vehicle.parts[12].name, "Suspension")
        with self.subTest("Trunk Name"):
            self.assertEqual(self._vehicle.parts[13].name, "Trunk")
        with self.subTest("Front Left Tyre Name"):
            self.assertEqual(self._vehicle.parts[14].name, "Front Left Tyre")
        with self.subTest("Front Right Tyre Name"):
            self.assertEqual(self._vehicle.parts[15].name, "Front Right Tyre")
        with self.subTest("Rear Left Tyre Name"):
            self.assertEqual(self._vehicle.parts[16].name, "Rear Left Tyre")
        with self.subTest("Rear Right Tyre Name"):
            self.assertEqual(self._vehicle.parts[17].name, "Rear Right Tyre")
        with self.subTest("Front Left Wheel Name"):
            self.assertEqual(self._vehicle.parts[18].name, "Front Left Wheel")
        with self.subTest("Front Right Wheel Name"):
            self.assertEqual(self._vehicle.parts[19].name, "Front Right Wheel")
        with self.subTest("Rear Left Wheel Name"):
            self.assertEqual(self._vehicle.parts[20].name, "Rear Left Wheel")
        with self.subTest("Rear Right Wheel Name"):
            self.assertEqual(self._vehicle.parts[21].name, "Rear Right Wheel")
        with self.subTest("Axel Colour"):
            self.assertEqual(self._vehicle.parts[0].colour, self._black)
        with self.subTest("Bonnet Colour"):
            self.assertEqual(self._vehicle.parts[1].colour, self._red)
        with self.subTest("Front Left Brake Colour"):
            self.assertEqual(self._vehicle.parts[2].colour, self._black)
        with self.subTest("Front Right Brake Colour"):
            self.assertEqual(self._vehicle.parts[3].colour, self._black)
        with self.subTest("Rear Left Brake Colour"):
            self.assertEqual(self._vehicle.parts[4].colour, self._black)
        with self.subTest("Rear Right Brake Colour"):
            self.assertEqual(self._vehicle.parts[5].colour, self._black)
        with self.subTest("Chassis Colour"):
            self.assertEqual(self._vehicle.parts[6].colour, self._black)
        with self.subTest("Front Driver Side Door Colour"):
            self.assertEqual(self._vehicle.parts[7].colour, self._red)
        with self.subTest("Front Passenger Side Door Colour"):
            self.assertEqual(self._vehicle.parts[8].colour, self._red)
        with self.subTest("Rear Driver Side Door Colour"):
            self.assertEqual(self._vehicle.parts[9].colour, self._red)
        with self.subTest("Rear Passenger Side Door Colour"):
            self.assertEqual(self._vehicle.parts[10].colour, self._red)
        with self.subTest("Engine Colour"):
            self.assertEqual(self._vehicle.parts[11].colour, self._black)
        with self.subTest("Suspension Colour"):
            self.assertEqual(self._vehicle.parts[12].colour, self._black)
        with self.subTest("Trunk Colour"):
            self.assertEqual(self._vehicle.parts[13].colour, self._red)
        with self.subTest("Front Left Tyre Colour"):
            self.assertEqual(self._vehicle.parts[14].colour, self._black)
        with self.subTest("Front Right Tyre Colour"):
            self.assertEqual(self._vehicle.parts[15].colour, self._black)
        with self.subTest("Rear Left Tyre Colour"):
            self.assertEqual(self._vehicle.parts[16].colour, self._black)
        with self.subTest("Rear Right Tyre Colour"):
            self.assertEqual(self._vehicle.parts[17].colour, self._black)
        with self.subTest("Front Left Wheel Colour"):
            self.assertEqual(self._vehicle.parts[18].colour, self._black)
        with self.subTest("Front Right Wheel Colour"):
            self.assertEqual(self._vehicle.parts[19].colour, self._black)
        with self.subTest("Rear Left Wheel Colour"):
            self.assertEqual(self._vehicle.parts[20].colour, self._black)
        with self.subTest("Rear Right Wheel Colour"):
            self.assertEqual(self._vehicle.parts[21].colour, self._black)
        with self.subTest("Axel Manufacturer"):
            self.assertEqual(self._vehicle.parts[0].manufacturer, "Audi")
        with self.subTest("Bonnet Manufacturer"):
            self.assertEqual(self._vehicle.parts[1].manufacturer, "Audi")
        with self.subTest("Front Left Brake Manufacturer"):
            self.assertEqual(self._vehicle.parts[2].manufacturer, "Audi")
        with self.subTest("Front Right Brake Manufacturer"):
            self.assertEqual(self._vehicle.parts[3].manufacturer, "Audi")
        with self.subTest("Rear Left Brake Manufacturer"):
            self.assertEqual(self._vehicle.parts[4].manufacturer, "Audi")
        with self.subTest("Rear Right Brake Manufacturer"):
            self.assertEqual(self._vehicle.parts[5].manufacturer, "Audi")
        with self.subTest("Chassis Manufacturer"):
            self.assertEqual(self._vehicle.parts[6].manufacturer, "Audi")
        with self.subTest("Front Driver Side Door Manufacturer"):
            self.assertEqual(self._vehicle.parts[7].manufacturer, "Audi")
        with self.subTest("Front Passenger Side Door Manufacturer"):
            self.assertEqual(self._vehicle.parts[8].manufacturer, "Audi")
        with self.subTest("Rear Driver Side Door Manufacturer"):
            self.assertEqual(self._vehicle.parts[9].manufacturer, "Audi")
        with self.subTest("Rear Passenger Side Door Manufacturer"):
            self.assertEqual(self._vehicle.parts[10].manufacturer, "Audi")
        with self.subTest("Engine Manufacturer"):
            self.assertEqual(self._vehicle.parts[11].manufacturer, "Audi")
        with self.subTest("Suspension Manufacturer"):
            self.assertEqual(self._vehicle.parts[12].manufacturer, "Audi")
        with self.subTest("Trunk Manufacturer"):
            self.assertEqual(self._vehicle.parts[13].manufacturer, "Audi")
        with self.subTest("Front Left Tyre Manufacturer"):
            self.assertEqual(self._vehicle.parts[14].manufacturer, "Audi")
        with self.subTest("Front Right Tyre Manufacturer"):
            self.assertEqual(self._vehicle.parts[15].manufacturer, "Audi")
        with self.subTest("Rear Left Tyre Manufacturer"):
            self.assertEqual(self._vehicle.parts[16].manufacturer, "Audi")
        with self.subTest("Rear Right Tyre Manufacturer"):
            self.assertEqual(self._vehicle.parts[17].manufacturer, "Audi")
        with self.subTest("Front Left Wheel Manufacturer"):
            self.assertEqual(self._vehicle.parts[18].manufacturer, "Audi")
        with self.subTest("Front Right Wheel Manufacturer"):
            self.assertEqual(self._vehicle.parts[19].manufacturer, "Audi")
        with self.subTest("Rear Left Wheel Manufacturer"):
            self.assertEqual(self._vehicle.parts[20].manufacturer, "Audi")
        with self.subTest("Rear Right Wheel Manufacturer"):
            self.assertEqual(self._vehicle.parts[21].manufacturer, "Audi")
        with self.subTest("Axel Dimensions"):
            self.assertEqual(self._vehicle.parts[0].dimensions, {"Length": 0.5, "Width": 1})
        with self.subTest("Bonnet Dimensions"):
            self.assertEqual(self._vehicle.parts[1].dimensions, {"Length": 1, "Width": 1})
        with self.subTest("Front Left Brake Dimensions"):
            self.assertEqual(self._vehicle.parts[2].dimensions, {"Length": 0.1, "Width": 0.1})
        with self.subTest("Front Right Brake Dimensions"):
            self.assertEqual(self._vehicle.parts[3].dimensions, {"Length": 0.1, "Width": 0.1})
        with self.subTest("Rear Left Brake Dimensions"):
            self.assertEqual(self._vehicle.parts[4].dimensions, {"Length": 0.1, "Width": 0.1})
        with self.subTest("Rear Right Brake Dimensions"):
            self.assertEqual(self._vehicle.parts[5].dimensions, {"Length": 0.1, "Width": 0.1})
        with self.subTest("Chassis Dimensions"):
            self.assertEqual(self._vehicle.parts[6].dimensions, {"Length": 1.5, "Width": 2})
        with self.subTest("Front Driver Side Door Dimensions"):
            self.assertEqual(self._vehicle.parts[7].dimensions, {"Length": 1, "Width": 1})
        with self.subTest("Front Passenger Side Door Dimensions"):
            self.assertEqual(self._vehicle.parts[8].dimensions, {"Length": 1, "Width": 1})
        with self.subTest("Rear Driver Side Door Dimensions"):
            self.assertEqual(self._vehicle.parts[9].dimensions, {"Length": 1, "Width": 1})
        with self.subTest("Rear Passenger Side Door Dimensions"):
            self.assertEqual(self._vehicle.parts[10].dimensions, {"Length": 1, "Width": 1})
        with self.subTest("Engine Dimensions"):
            self.assertEqual(self._vehicle.parts[11].dimensions, {"Length": 0.5, "Width": 0.5, "Height": 0.5})
        with self.subTest("Suspension Dimensions"):
            self.assertEqual(self._vehicle.parts[12].dimensions, {"Length": 1.5, "Width": 2})
        with self.subTest("Trunk Dimensions"):
            self.assertEqual(self._vehicle.parts[13].dimensions, {"Length": 1, "Width": 1})
        with self.subTest("Front Left Tyre Dimensions"):
            self.assertEqual(self._vehicle.parts[14].dimensions, {"Diameter": 3, "Radius": 3})
        with self.subTest("Front Right Tyre Dimensions"):
            self.assertEqual(self._vehicle.parts[15].dimensions, {"Diameter": 3, "Radius": 3})
        with self.subTest("Rear Left Tyre Dimensions"):
            self.assertEqual(self._vehicle.parts[16].dimensions, {"Diameter": 3, "Radius": 3})
        with self.subTest("Rear Right Tyre Dimensions"):
            self.assertEqual(self._vehicle.parts[17].dimensions, {"Diameter": 3, "Radius": 3})
        with self.subTest("Front Left Wheel Dimensions"):
            self.assertEqual(self._vehicle.parts[18].dimensions, {"Diameter": 3, "Radius": 3})
        with self.subTest("Front Right Wheel Dimensions"):
            self.assertEqual(self._vehicle.parts[19].dimensions, {"Diameter": 3, "Radius": 3})
        with self.subTest("Rear Left Wheel Dimensions"):
            self.assertEqual(self._vehicle.parts[20].dimensions, {"Diameter": 3, "Radius": 3})
        with self.subTest("Rear Right Wheel Dimensions"):
            self.assertEqual(self._vehicle.parts[21].dimensions, {"Diameter": 3, "Radius": 3})
        with self.subTest("Axel Object"):
            self.assertEqual(self._vehicle.parts[0].__str__(),
                             "Part Name: Axel\n"
                             "Part ID: 1\n"
                             "Colour: \n"
                             "RGB(0, 0, 0)\n"
                             "CMYK(0, 0, 0, 100)\n"
                             "#000000\n"
                             "Manufacture: Audi\n"
                             "Length: 0.5 Meters\n"
                             "Width: 1 Meters")
        with self.subTest("Bonnet Object"):
            self.assertEqual(self._vehicle.parts[1].__str__(),
                             "Part Name: Bonnet\n"
                             "Part ID: 1\n"
                             "Colour: \n"
                             "RGB(255, 0, 0)\n"
                             "CMYK(0, 100, 100, 0)\n"
                             "#FF0000\n"
                             "Manufacture: Audi\n"
                             "Length: 1 Meters\n"
                             "Width: 1 Meters")
        with self.subTest("Front Left Brake Object"):
            self.assertEqual(self._vehicle.parts[2].__str__(),
                             "Part Name: Front Left Brake\n"
                             "Part ID: 1\n"
                             "Colour: \n"
                             "RGB(0, 0, 0)\n"
                             "CMYK(0, 0, 0, 100)\n"
                             "#000000\n"
                             "Manufacture: Audi\n"
                             "Length: 0.1 Meters\n"
                             "Width: 0.1 Meters")
        with self.subTest("Front Right Brake Object"):
            self.assertEqual(self._vehicle.parts[3].__str__(),
                             "Part Name: Front Right Brake\n"
                             "Part ID: 2\n"
                             "Colour: \n"
                             "RGB(0, 0, 0)\n"
                             "CMYK(0, 0, 0, 100)\n"
                             "#000000\n"
                             "Manufacture: Audi\n"
                             "Length: 0.1 Meters\n"
                             "Width: 0.1 Meters")
        with self.subTest("Rear Left Brake Object"):
            self.assertEqual(self._vehicle.parts[4].__str__(),
                             "Part Name: Rear Left Brake\n"
                             "Part ID: 3\n"
                             "Colour: \n"
                             "RGB(0, 0, 0)\n"
                             "CMYK(0, 0, 0, 100)\n"
                             "#000000\n"
                             "Manufacture: Audi\n"
                             "Length: 0.1 Meters\n"
                             "Width: 0.1 Meters")
        with self.subTest("Rear Left Brake Object"):
            self.assertEqual(self._vehicle.parts[5].__str__(),
                             "Part Name: Rear Right Brake\n"
                             "Part ID: 4\n"
                             "Colour: \n"
                             "RGB(0, 0, 0)\n"
                             "CMYK(0, 0, 0, 100)\n"
                             "#000000\n"
                             "Manufacture: Audi\n"
                             "Length: 0.1 Meters\n"
                             "Width: 0.1 Meters")
        with self.subTest("Chassis Object"):
            self.assertEqual(self._vehicle.parts[6].__str__(),
                             "Part Name: Chassis\n"
                             "Part ID: 1\n"
                             "Colour: \n"
                             "RGB(0, 0, 0)\n"
                             "CMYK(0, 0, 0, 100)\n"
                             "#000000\n"
                             "Manufacture: Audi\n"
                             "Length: 1.5 Meters\n"
                             "Width: 2 Meters")
        with self.subTest("Front Driver Side Door Object"):
            self.assertEqual(self._vehicle.parts[7].__str__(),
                             "Part Name: Front Driver Side Door\n"
                             "Part ID: 1\n"
                             "Colour: \n"
                             "RGB(255, 0, 0)\n"
                             "CMYK(0, 100, 100, 0)\n"
                             "#FF0000\n"
                             "Manufacture: Audi\n"
                             "Length: 1 Meters\n"
                             "Width: 1 Meters\n"
                             "Door Shut\n"
                             "Door Locked")
        with self.subTest("Front Passenger Side Door Object"):
            self.assertEqual(self._vehicle.parts[8].__str__(),
                             "Part Name: Front Passenger Side Door\n"
                             "Part ID: 2\n"
                             "Colour: \n"
                             "RGB(255, 0, 0)\n"
                             "CMYK(0, 100, 100, 0)\n"
                             "#FF0000\n"
                             "Manufacture: Audi\n"
                             "Length: 1 Meters\n"
                             "Width: 1 Meters\n"
                             "Door Shut\n"
                             "Door Locked")
        with self.subTest("Rear Driver Side Door Object"):
            self.assertEqual(self._vehicle.parts[9].__str__(),
                             "Part Name: Rear Driver Side Door\n"
                             "Part ID: 3\n"
                             "Colour: \n"
                             "RGB(255, 0, 0)\n"
                             "CMYK(0, 100, 100, 0)\n"
                             "#FF0000\n"
                             "Manufacture: Audi\n"
                             "Length: 1 Meters\n"
                             "Width: 1 Meters\n"
                             "Door Shut\n"
                             "Door Locked")
        with self.subTest("Rear Passenger Side Door Object"):
            self.assertEqual(self._vehicle.parts[10].__str__(),
                             "Part Name: Rear Passenger Side Door\n"
                             "Part ID: 4\n"
                             "Colour: \n"
                             "RGB(255, 0, 0)\n"
                             "CMYK(0, 100, 100, 0)\n"
                             "#FF0000\n"
                             "Manufacture: Audi\n"
                             "Length: 1 Meters\n"
                             "Width: 1 Meters\n"
                             "Door Shut\n"
                             "Door Locked")
        with self.subTest("Engine Object"):
            self.assertEqual(self._vehicle.parts[11].__str__(),
                             "Part Name: Engine\n"
                             "Part ID: 1\n"
                             "Colour: \n"
                             "RGB(0, 0, 0)\n"
                             "CMYK(0, 0, 0, 100)\n"
                             "#000000\n"
                             "Manufacture: Audi\n"
                             "Length: 0.5 Meters\n"
                             "Width: 0.5 Meters\n"
                             "Height: 0.5 Meters\n"
                             "Engine Size: 2L\n"
                             "Break Horse Power: 250\n"
                             "Number of Cylinders: 12\n"
                             "Number of Valves: 8\n"
                             "Mode: Sport")
        with self.subTest("Suspension Object"):
            self.assertEqual(self._vehicle.parts[12].__str__(),
                             "Part Name: Suspension\n"
                             "Part ID: 1\n"
                             "Colour: \n"
                             "RGB(0, 0, 0)\n"
                             "CMYK(0, 0, 0, 100)\n"
                             "#000000\n"
                             "Manufacture: Audi\n"
                             "Length: 1.5 Meters\n"
                             "Width: 2 Meters")
        with self.subTest("Trunk Object"):
            self.assertEqual(self._vehicle.parts[13].__str__(),
                             "Part Name: Trunk\n"
                             "Part ID: 1\n"
                             "Colour: \n"
                             "RGB(255, 0, 0)\n"
                             "CMYK(0, 100, 100, 0)\n"
                             "#FF0000\n"
                             "Manufacture: Audi\n"
                             "Length: 1 Meters\n"
                             "Width: 1 Meters\n"
                             "Trunk Shut\n"
                             "Trunk Locked")
        with self.subTest("Front Left Tyre Object"):
            self.assertEqual(self._vehicle.parts[14].__str__(),
                             "Part Name: Front Left Tyre\n"
                             "Part ID: 1\n"
                             "Colour: \n"
                             "RGB(0, 0, 0)\n"
                             "CMYK(0, 0, 0, 100)\n"
                             "#000000\n"
                             "Manufacture: Audi\n"
                             "Diameter: 3 Meters\n"
                             "Radius: 3 Meters\n"
                             "Current Air Pressure: 50 psi\n"
                             "Tyre Thread Remaining: 10 mm")
        with self.subTest("Front Right Tyre Object"):
            self.assertEqual(self._vehicle.parts[15].__str__(),
                             "Part Name: Front Right Tyre\n"
                             "Part ID: 2\n"
                             "Colour: \n"
                             "RGB(0, 0, 0)\n"
                             "CMYK(0, 0, 0, 100)\n"
                             "#000000\n"
                             "Manufacture: Audi\n"
                             "Diameter: 3 Meters\n"
                             "Radius: 3 Meters\n"
                             "Current Air Pressure: 50 psi\n"
                             "Tyre Thread Remaining: 10 mm")
        with self.subTest("Rear Left Tyre Object"):
            self.assertEqual(self._vehicle.parts[16].__str__(),
                             "Part Name: Rear Left Tyre\n"
                             "Part ID: 3\n"
                             "Colour: \n"
                             "RGB(0, 0, 0)\n"
                             "CMYK(0, 0, 0, 100)\n"
                             "#000000\n"
                             "Manufacture: Audi\n"
                             "Diameter: 3 Meters\n"
                             "Radius: 3 Meters\n"
                             "Current Air Pressure: 50 psi\n"
                             "Tyre Thread Remaining: 10 mm")
        with self.subTest("Rear Right Tyre Object"):
            self.assertEqual(self._vehicle.parts[17].__str__(),
                             "Part Name: Rear Right Tyre\n"
                             "Part ID: 4\n"
                             "Colour: \n"
                             "RGB(0, 0, 0)\n"
                             "CMYK(0, 0, 0, 100)\n"
                             "#000000\n"
                             "Manufacture: Audi\n"
                             "Diameter: 3 Meters\n"
                             "Radius: 3 Meters\n"
                             "Current Air Pressure: 50 psi\n"
                             "Tyre Thread Remaining: 10 mm")
        with self.subTest("Front Left Wheel Object"):
            self.assertEqual(self._vehicle.parts[18].__str__(),
                             "Part Name: Front Left Wheel\n"
                             "Part ID: 1\n"
                             "Colour: \n"
                             "RGB(0, 0, 0)\n"
                             "CMYK(0, 0, 0, 100)\n"
                             "#000000\n"
                             "Manufacture: Audi\n"
                             "Diameter: 3 Meters\n"
                             "Radius: 3 Meters")
        with self.subTest("Front Right Wheel Object"):
            self.assertEqual(self._vehicle.parts[19].__str__(),
                             "Part Name: Front Right Wheel\n"
                             "Part ID: 2\n"
                             "Colour: \n"
                             "RGB(0, 0, 0)\n"
                             "CMYK(0, 0, 0, 100)\n"
                             "#000000\n"
                             "Manufacture: Audi\n"
                             "Diameter: 3 Meters\n"
                             "Radius: 3 Meters")
        with self.subTest("Rear Left Wheel Object"):
            self.assertEqual(self._vehicle.parts[20].__str__(),
                             "Part Name: Rear Left Wheel\n"
                             "Part ID: 3\n"
                             "Colour: \n"
                             "RGB(0, 0, 0)\n"
                             "CMYK(0, 0, 0, 100)\n"
                             "#000000\n"
                             "Manufacture: Audi\n"
                             "Diameter: 3 Meters\n"
                             "Radius: 3 Meters")
        with self.subTest("Rear Right Wheel Object"):
            self.assertEqual(self._vehicle.parts[21].__str__(),
                             "Part Name: Rear Right Wheel\n"
                             "Part ID: 4\n"
                             "Colour: \n"
                             "RGB(0, 0, 0)\n"
                             "CMYK(0, 0, 0, 100)\n"
                             "#000000\n"
                             "Manufacture: Audi\n"
                             "Diameter: 3 Meters\n"
                             "Radius: 3 Meters")
        with self.subTest("Front Driver Side Door Closed Status"):
            self.assertEqual(self._vehicle.parts[7].closed, True)
        with self.subTest("Front Driver Side Door Locked Status"):
            self.assertEqual(self._vehicle.parts[7].locked, True)
        with self.subTest("Front Passenger Side Door Closed Status"):
            self.assertEqual(self._vehicle.parts[8].closed, True)
        with self.subTest("Front Passenger Side Door Locked Status"):
            self.assertEqual(self._vehicle.parts[8].locked, True)
        with self.subTest("Rear Driver Side Door Closed Status"):
            self.assertEqual(self._vehicle.parts[9].closed, True)
        with self.subTest("Rear Driver Side Door Locked Status"):
            self.assertEqual(self._vehicle.parts[9].locked, True)
        with self.subTest("Rear Passenger Side Door Closed Status"):
            self.assertEqual(self._vehicle.parts[10].closed, True)
        with self.subTest("Rear Passenger Side Door Locked Status"):
            self.assertEqual(self._vehicle.parts[10].locked, True)
        with self.subTest("Front Driver Side Door Closed Status"):
            self.assertEqual(self._vehicle.parts[10].closed, True)
        with self.subTest("Engine Size"):
            self.assertEqual(self._vehicle.parts[11].size, 2)
        with self.subTest("Horse Power"):
            self.assertEqual(self._vehicle.parts[11].horse_power, 250)
        with self.subTest("Number Of Cylinders"):
            self.assertEqual(self._vehicle.parts[11].cylinders, 12)
        with self.subTest("Number Of Valves"):
            self.assertEqual(self._vehicle.parts[11].valves, 8)
        with self.subTest("Engine Mode"):
            self.assertEqual(self._vehicle.parts[11].mode, EngineMode.Sport)
        with self.subTest("Trunk Locked Status"):
            self.assertEqual(self._vehicle.parts[13].locked, True)
        with self.subTest("Trunk Shut Status"):
            self.assertEqual(self._vehicle.parts[13].closed, True)
        with self.subTest("Front Left Tyre"):
            self.assertEqual(self._vehicle.parts[14].tyre_pressure, 50)
        with self.subTest("Front Left Tyre"):
            self.assertEqual(self._vehicle.parts[14].tread, 10)
        with self.subTest("Front Right Tyre"):
            self.assertEqual(self._vehicle.parts[15].tyre_pressure, 50)
        with self.subTest("Front Right Tyre"):
            self.assertEqual(self._vehicle.parts[15].tread, 10)
        with self.subTest("Rear Left Tyre"):
            self.assertEqual(self._vehicle.parts[16].tyre_pressure, 50)
        with self.subTest("Rear Left Tyre"):
            self.assertEqual(self._vehicle.parts[16].tread, 10)
        with self.subTest("Rear Right Tyre"):
            self.assertEqual(self._vehicle.parts[17].tyre_pressure, 50)
        with self.subTest("Rear Right Tyre"):
            self.assertEqual(self._vehicle.parts[17].tread, 10)

    def testPartsSetter(self):
        """Testing you can update the list of parts that make up the vehicle by calling the parts setter"""
        part = Part(1, "Shock Absorber", self._black, "Audi", {"Length": 0.5, "Width": 0.2})
        self._vehicle.parts = [part]
        with self.subTest("Part Name"):
            self.assertEqual(self._vehicle.parts[0].name, "Shock Absorber")
        with self.subTest("Part Colour"):
            self.assertEqual(self._vehicle.parts[0].colour, self._black)
        with self.subTest("Part Manufacturer"):
            self.assertEqual(self._vehicle.parts[0].manufacturer, "Audi")
        with self.subTest("Part Dimensions"):
            self.assertEqual(self._vehicle.parts[0].dimensions, {"Length": 0.5, "Width": 0.2})
        with self.subTest("Part Object"):
            self.assertEqual(self._vehicle.parts[0].__str__(),
                             "Part Name: Shock Absorber\n"
                             "Part ID: 1\n"
                             "Colour: \n"
                             "RGB(0, 0, 0)\n"
                             "CMYK(0, 0, 0, 100)\n"
                             "#000000\n"
                             "Manufacture: Audi\n"
                             "Length: 0.5 Meters\n"
                             "Width: 0.2 Meters")

    def testPartsSetterWithNone(self):
        """Testing you can update the list of parts that make up the vehicle by calling the parts setter"""
        self._vehicle.parts = None
        self.assertEqual(self._vehicle.parts, [])

    def testRegistrationNumberGetter(self):
        """Testing the registration number is returned when you call the registration number getter"""
        self.assertEqual(self._vehicle.registration_number, "AB24CDE")

    def testRegistrationNumberSetter(self):
        """Testing you can update the registration number by calling the registration number setter"""
        self._vehicle.registration_number = "FG13HIJ"
        self.assertEqual(self._vehicle.registration_number, "FG13HIJ")

    def testValueErrorRaisedIfTheVehiclesRegistrationNumberSetUsingTheRegistrationNumberSetterIsNotValid(self):
        """Testing a value error is raised when you try to set a non-valid registration number"""
        with self.assertRaises(ValueError):
            self._vehicle.registration_number = "1234567"

    def testRightIndicatorGetter(self):
        """Testing the right indicator status is returned when you call the right indicator getter"""
        self.assertEqual(self._vehicle.right_indicator, False)

    def testRightIndicatorSetter(self):
        """Testing you can update the right indicator status by calling the right indicator setter"""
        self._vehicle.right_indicator = True
        self.assertEqual(self._vehicle.right_indicator, True)

    def testSecuritySystemGetter(self):
        """Testing the security system is returned when you call the security system getter"""
        with self.subTest("Alarm Activated Status"):
            self.assertEqual(self._vehicle.security_system.armed, True)
        with self.subTest("Locked Status"):
            self.assertEqual(self._vehicle.security_system.locked, False)
        with self.subTest("Alarm Triggered Status"):
            self.assertEqual(self._vehicle.security_system.triggered, False)
        with self.subTest("Security System Object"):
            self.assertEqual(self._vehicle.security_system.__str__(),
                             "Alarm Status: Alarm Activated\n"
                             "Vehicle Unlocked\n"
                             "Alarm Not Triggered")

    def testSecuritySystemSetter(self):
        """Testing you can update the security system by calling the security system setter"""
        self._vehicle.security_system = SecuritySystem(True, True)
        self._vehicle.security_system.alarm_triggered()
        with self.subTest("Alarm Activated Status"):
            self.assertEqual(self._vehicle.security_system.armed, True)
        with self.subTest("Locked Status"):
            self.assertEqual(self._vehicle.security_system.locked, True)
        with self.subTest("Alarm Triggered Status"):
            self.assertEqual(self._vehicle.security_system.triggered, True)
        with self.subTest("Security System Object"):
            self.assertEqual(self._vehicle.security_system.__str__(),
                             "Alarm Status: Alarm Activated\n"
                             "Vehicle locked\n"
                             "Alarm Triggered")

    def testSpeedGetter(self):
        """Testing the speed is returned when you call the speed getter"""
        with self.subTest("Current Speed"):
            self.assertEqual(self._vehicle.speed.current_speed, 20)
        with self.subTest("Top Speed"):
            self.assertEqual(self._vehicle.speed.top_speed, 150)
        with self.subTest("Acceleration"):
            self.assertEqual(self._vehicle.speed.acceleration, 5)
        with self.subTest("Speed Object"):
            self.assertEqual(self._vehicle.speed.__str__(),
                             "Current Speed: 20MPH\n"
                             "Top Speed: 150MPH\n"
                             "0-60 MPH Speed: 5 seconds ")

    def testSpeedSetter(self):
        """Testing you can update the speed by calling the speed setter"""
        self._vehicle.speed = Speed(100, 8, 50)
        with self.subTest("Current Speed"):
            self.assertEqual(self._vehicle.speed.current_speed, 50)
        with self.subTest("Top Speed"):
            self.assertEqual(self._vehicle.speed.top_speed, 100)
        with self.subTest("Acceleration"):
            self.assertEqual(self._vehicle.speed.acceleration, 8)
        with self.subTest("Speed Object"):
            self.assertEqual(self._vehicle.speed.__str__(),
                             "Current Speed: 50MPH\n"
                             "Top Speed: 100MPH\n"
                             "0-60 MPH Speed: 8 seconds ")

    def testSteeringGetter(self):
        """Testing the steering object is returned when you call the steering getter"""
        with self.subTest("Wheel Rotation"):
            self.assertEqual(self._vehicle.steering.wheel_rotation, 0)
        with self.subTest("Steering Object"):
            self.assertEqual(self._vehicle.steering.__str__(), "Wheel rotation: 0 degrees")

    def testSteeringSetter(self):
        """Testing you can update the steering object by calling the steering setter"""
        self._vehicle.steering = Steering(50)
        with self.subTest("Wheel Rotation"):
            self.assertEqual(self._vehicle.steering.wheel_rotation, 50)
        with self.subTest("Steering Object"):
            self.assertEqual(self._vehicle.steering.__str__(), "Wheel rotation: 50 degrees")

    def testTransmissionGetter(self):
        """Testing the vehicles transmission is returned when you call the transmission getter"""
        with self.subTest("Part Name"):
            self.assertEqual(self._vehicle.transmission.name, "Transmission")
        with self.subTest("Part ID"):
            self.assertEqual(self._vehicle.transmission.part_id, 1)
        with self.subTest("Colour"):
            self.assertEqual(self._vehicle.transmission.colour.red, 0)
            self.assertEqual(self._vehicle.transmission.colour.green, 0)
            self.assertEqual(self._vehicle.transmission.colour.blue, 0)
        with self.subTest("Manufacturer"):
            self.assertEqual(self._vehicle.transmission.manufacturer, "Audi")
        with self.subTest("Dimensions"):
            self.assertEqual(self._vehicle.transmission.dimensions, {"Length": 0.5, "Width": 0.5, "Height": 0.5})
        with self.subTest("Transmission Type"):
            self.assertEqual(self._vehicle.transmission.transmission_type, TransmissionType.MANUAL)
        with self.subTest("Number of gears"):
            self.assertEqual(self._vehicle.transmission.number_of_gears, 6)
        with self.subTest("Current Gear"):
            self.assertEqual(self._vehicle.transmission.current_gear, 3)

    def testTransmissionSetter(self):
        """Testing the vehicles transmission can be updated by calling the transmission setter"""
        self._vehicle.transmission = Transmission(2, "Transmission", Colour(255, 255, 255), "BMW",
                                                  {"Length": 0.4, "Width": 0.4, "Height": 0.4},
                                                  TransmissionType.AUTOMATIC, 1, 1)
        with self.subTest("Part Name"):
            self.assertEqual(self._vehicle.transmission.name, "Transmission")
        with self.subTest("Part ID"):
            self.assertEqual(self._vehicle.transmission.part_id, 2)
        with self.subTest("Colour"):
            self.assertEqual(self._vehicle.transmission.colour.red, 255)
            self.assertEqual(self._vehicle.transmission.colour.green, 255)
            self.assertEqual(self._vehicle.transmission.colour.blue, 255)
        with self.subTest("Manufacturer"):
            self.assertEqual(self._vehicle.transmission.manufacturer, "BMW")
        with self.subTest("Dimensions"):
            self.assertEqual(self._vehicle.transmission.dimensions, {"Length": 0.4, "Width": 0.4, "Height": 0.4})
        with self.subTest("Transmission Type"):
            self.assertEqual(self._vehicle.transmission.transmission_type, TransmissionType.AUTOMATIC)
        with self.subTest("Number of gears"):
            self.assertEqual(self._vehicle.transmission.number_of_gears, 1)
        with self.subTest("Current Gear"):
            self.assertEqual(self._vehicle.transmission.current_gear, 1)

    def testYearGetter(self):
        """Testing the year the vehicle was made is returned when you call the year getter"""
        self.assertEqual(self._vehicle.year, 2024)

    def testYearSetter(self):
        """Testing you can update the year the vehicle was made by calling the year setter"""
        self._vehicle.year = 2023
        self.assertEqual(self._vehicle.year, 2023)

    def testValueErrorRaisedIfTheYearTheVehiclesWasMadeInSetUsingTheYearSetterIsInTheFuture(self):
        """Testing a value error is raised if you try to set the year the vehicle was made to be in the future"""
        with self.assertRaises(ValueError):
            self._vehicle.year = 10000

    def testCalculatingStoppingDistance(self):
        """Testing the calculate stopping distance function"""
        self.assertEqual(self._vehicle.calculate_stopping_distance(), 20)

    def testAccelerate(self):
        """Testing the accelerate function"""
        self._vehicle.accelerate()
        self.assertEqual(self._vehicle.speed.current_speed, 21)

    def testAccelerateWithCruiseControl(self):
        """Testing the accelerate function when cruise control is on"""
        auto_pilot = AutoPilot(False, self._current_weather, 250)
        cruise_control = CruiseControl(True, 70, self._current_weather, 250)
        self._vehicle = Vehicle(auto_pilot, self._body_type, self._collision_detection_system, self._red,
                                cruise_control,
                                self._current_lane, self._vehicle_dimensions, self._drive_system, self._fuel, self._gps,
                                self._infotainment_system,
                                self._lane_marking_detection_system, self._left_indicator, self._logs, self._make,
                                self._mileage, self._model,
                                self._object_detection_system, self._parts, self._registration_number,
                                self._right_indicator, self._security_system,
                                self._speed, self._steering, self._transmission, self._year)
        self._vehicle.accelerate()
        self.assertEqual(self._vehicle.speed.current_speed, 21)

    def testAccelerateWithoutCruiseControlAndAutoPilot(self):
        """Testing the accelerate function when cruise control is on"""
        auto_pilot = AutoPilot(False, self._current_weather, 250)
        cruise_control = CruiseControl(False, None, self._current_weather, 250)
        self._vehicle = Vehicle(auto_pilot, self._body_type, self._collision_detection_system, self._red,
                                cruise_control,
                                self._current_lane, self._vehicle_dimensions, self._drive_system, self._fuel, self._gps,
                                self._infotainment_system,
                                self._lane_marking_detection_system, self._left_indicator, self._logs, self._make,
                                self._mileage, self._model,
                                self._object_detection_system, self._parts, self._registration_number,
                                self._right_indicator, self._security_system,
                                self._speed, self._steering, self._transmission, self._year)
        self._vehicle.accelerate()
        self.assertEqual(self._vehicle.speed.current_speed, 21)

    def testTriggerAlarm(self):
        """Testing the trigger alarm function"""
        with self.subTest("Vehicle Locked, Alarm Trigger and Emergency Services Called"):
            with patch.object(self._vehicle.infotainment_system.phone, 'call_emergency_services'), \
                    patch.object(self._vehicle.security_system, 'alarm_triggered'), \
                    patch.object(self._vehicle.security_system, 'lock_vehicle') as mock:
                self._vehicle.trigger_alarm()
            mock.assert_called()
        self._vehicle.trigger_alarm()
        with self.subTest("Vehicle Locked"):
            self.assertEqual(self._vehicle.security_system.locked, True)
        with self.subTest("Alarm Triggered"):
            self.assertEqual(self._vehicle.security_system.triggered, True)
        with self.subTest("Emergency Services Called"):
            self.assertEqual(self._vehicle.infotainment_system.phone.call_emergency_services(),
                             "Calling Emergency Services")

    def testAvoidCollisionWithEmergencyStop(self):
        """Testing an emergency stop to avoid a collision if the object is too close"""
        self._vehicle.current_lane = 1
        self._vehicle.object_detection_system.objects_detected[0].distance_to_object = 2
        self._vehicle.avoid_collision()
        self.assertEqual(self._vehicle.current_lane, 1)
        self.assertEqual(self._vehicle.speed.current_speed, 0)

    def testAvoidCollisionBySwitchingToTheRightLane(self):
        """Testing switching to the lane on the right to avoid a collision"""
        self._vehicle.current_lane = 1
        self._vehicle.right_indicator = True
        self._vehicle.object_detection_system.objects_detected[0].distance_to_object = 25
        self._vehicle.avoid_collision()
        self.assertEqual(self._vehicle.current_lane, 2)

    def testAvoidCollisionBySwitchingToTheLeftLane(self):
        """Testing switching to the lane on the left to avoid a collision"""
        self._vehicle.current_lane = 3
        self._vehicle.left_indicator = True
        self._vehicle.object_detection_system.objects_detected[0].lane_object_is_in = 3
        self._vehicle.object_detection_system.objects_detected[0].distance_to_object = 250
        self._vehicle.avoid_collision()
        self.assertEqual(self._vehicle.current_lane, 2)

    def testCollision(self):
        """Testing the collision function"""
        with self.subTest("Emergency Stop Performed and Emergency Services Called After Collision"):
            with patch.object(self._vehicle.infotainment_system.phone, 'call_emergency_services'), \
                    patch.object(self._vehicle.infotainment_system.phone, 'call_emergency_contact'), \
                    patch.object(self._vehicle, 'emergency_stop'), \
                    patch.object(self._vehicle, 'collision') as mock:
                self._vehicle.collision()
            mock.assert_called()
        self._vehicle.collision()
        with self.subTest("Speed after collision"):
            self.assertEqual(self._vehicle.speed.current_speed, 0)
        with self.subTest("Gear after collision"):
            self.assertEqual(self._vehicle.transmission.current_gear, 0)
        with self.subTest("Handbrake status after collision"):
            self.assertEqual(self._vehicle.collision_detection_system.handbrake_engaged, True)
        with self.subTest("Hazard lights status after collision"):
            self.assertEqual(self._vehicle.collision_detection_system.hazard_lights_turned_on, True)
        with self.subTest("Collision status after collision"):
            self.assertEqual(self._vehicle.collision_detection_system.collision_occurred, True)

    def testDecelerate(self):
        """Testing the brake function"""
        self._vehicle.decelerate()
        self.assertEqual(self._vehicle.speed.current_speed, 19)

    def testEmergencyStop(self):
        """Testing the emergency stop function"""
        self._vehicle.emergency_stop()
        with self.subTest("Speed after emergency stop"):
            self.assertEqual(self._vehicle.speed.current_speed, 0)
        with self.subTest("Gear after emergency stop"):
            self.assertEqual(self._vehicle.transmission.current_gear, 0)
        with self.subTest("Handbrake status after emergency stop"):
            self.assertEqual(self._vehicle.collision_detection_system.handbrake_engaged, True)
        with self.subTest("Hazard lights status after emergency stop"):
            self.assertEqual(self._vehicle.collision_detection_system.hazard_lights_turned_on, True)

    def testShiftUpAGear(self):
        """Testing the shift up a gear function"""
        self._vehicle.shift_up_a_gear()
        self.assertEqual(self._vehicle.transmission.current_gear, 4)

    def testShiftDownAGear(self):
        """Testing the shift down a gear function"""
        self._vehicle.shift_down_a_gear()
        self.assertEqual(self._vehicle.transmission.current_gear, 2)

    def testMoveToLeftLane(self):
        """Testing the switch to the left lane function"""
        self._vehicle.left_indicator = True
        self._vehicle.move_to_left_lane()
        self.assertEqual(self._vehicle.current_lane, 2)

    def testMoveToRightLane(self):
        """Testing the switch to the right lane function"""
        self._vehicle.right_indicator = True
        self._vehicle.move_to_right_lane()
        self.assertEqual(self._vehicle.current_lane, 4)

    def testPark(self):
        """Testing the park function"""
        self._vehicle.park()
        with self.subTest("Car stops in neutral"):
            self.assertEqual(self._vehicle.transmission.current_gear, 0)
        with self.subTest("Car stops at 0 MPH"):
            self.assertEqual(self._vehicle.speed.current_speed, 0)
        with self.subTest("Logs updated for parking"):
            self.assertEqual(self._vehicle.logs[-1], "Parked")
            self.assertEqual(self._vehicle.logs.__contains__("Parked"), True)

    def testReverseBayPark(self):
        """Testing the reverse bay park function"""
        self._vehicle.reverse_bay_park()
        with self.subTest("Car stops in neutral"):
            self.assertEqual(self._vehicle.transmission.current_gear, 0)
        with self.subTest("Car stops at 0 MPH"):
            self.assertEqual(self._vehicle.speed.current_speed, 0)
        with self.subTest("Logs updated for parking"):
            self.assertEqual(self._vehicle.logs[-1], "Reverse Bay Parked")
            self.assertEqual(self._vehicle.logs.__contains__("Reverse Bay Parked"), True)

    def testStopVehicle(self):
        """Testing the stop function"""
        self._vehicle.stop()
        with self.subTest("Car stops in neutral"):
            self.assertEqual(self._vehicle.transmission.current_gear, 0)
        with self.subTest("Car stops at 0 MPH"):
            self.assertEqual(self._vehicle.speed.current_speed, 0)

    def testStartVehicle(self):
        """Testing the start function"""
        self._vehicle.start()
        with self.subTest("Car starts in neutral"):
            self.assertEqual(self._vehicle.transmission.current_gear, 0)
        with self.subTest("Car starts at 0 MPH"):
            self.assertEqual(self._vehicle.speed.current_speed, 0)

    def testClearLogs(self):
        """Testing the clear logs function"""
        self._vehicle.clear_logs()
        self.assertEqual(self._vehicle.logs, [])

    def testVehicleObject(self):
        """Testing the vehicle object"""
        self.assertEqual(self._vehicle.__str__(),
                         "Vehicle:\n"
                         "Make: Audi\n"
                         "Model: A4\n"
                         "Drive System: AWD\n"
                         "Dimensions:\n"
                         "Length (meters): 5\n"
                         "Width (meters): 2\n"
                         "Height (meters): 2\n"
                         "Weight (tons): 2\n"
                         "Body Type: Coupe\n"
                         "Year: 2024\n"
                         "Registration Number: AB24CDE\n"
                         "Colour:\n"
                         "RGB(255, 0, 0)\n"
                         "CMYK(0, 100, 100, 0)\n"
                         "#FF0000\n"
                         "MPG: 40\n"
                         "Current Mileage: 100000 Miles\n"
                         "Fuel Type: Diesel\n"
                         "Fuel Tank Capacity: 100L\n"
                         "Amount of fuel remaining: 50L\n"
                         "AutoPilot: Enabled\n"
                         "Distance From The Closest Car: 30 meters\n"
                         "Weather Condition: Sunny\n"
                         "Temperature: 25 degrees\n"
                         "Recommended Following Distance: 2 Meters\n"
                         "Cruise Control Deactivated\n"
                         "Target Speed: 70MPH\n"
                         "Recommended Following Distance: 2 Meters\n"
                         "Distance From The Closest Car: 50 Meters\n"
                         "GPS:\n"
                         "Current Location:\n"
                         "Longitude: 10\n"
                         "Latitude: 50\n"
                         "Altitude: 0 Meters\n"
                         "Road Name: Maple Drive\n"
                         "Number Of Lanes: 4 lanes\n"
                         "Road Type: C Road\n"
                         "Traffic Status: No Traffic ahead\n"
                         "Speed Limit: 30MPH\n"
                         "Destination:\n"
                         "Longitude: 10\n"
                         "Latitude: 60\n"
                         "Altitude: 0 Meters\n"
                         "Road Name: Pine Lane\n"
                         "Number Of Lanes: 4 lanes\n"
                         "Road Type: C Road\n"
                         "Traffic Status: No Traffic ahead\n"
                         "Speed Limit: 30MPH\n"
                         "Routes:\n"
                         "Route 1:\n"
                         "Distance to destination: 10 Miles\n"
                         "Duration to destination: 10 Minuets\n"
                         "Directions:\n"
                         "In 500 yards turn left\n"
                         "In 300 yards turn right\n"
                         "In 2 miles you have reached your destination\n"
                         "Route 2:\n"
                         "Distance to destination: 1 Miles\n"
                         "Duration to destination: 10 Minuets\n"
                         "Directions:\n"
                         "In 1 mile turn left\n"
                         "In 500 yards you have reached your destination\n"
                         "Route 3:\n"
                         "Distance to destination: 10 Miles\n"
                         "Duration to destination: 1 Minuets\n"
                         "Directions:\n"
                         "In 1.2 miles turn left\n"
                         "In 200 yards you have reached your destination\n"
                         "Collision Detection System:\n"
                         "No Collision Detected\n"
                         "Handbrake not engaged\n"
                         "Hazard Lights Off\n"
                         "Object Detection System:\n"
                         "Cameras:\n"
                         "Camera 1:\n"
                         "Camera Quality: 1920 x 1080\n"
                         "Frames:\n"
                         "Frame 1\n"
                         "File Name: File.MP4\n"
                         "Camera 2:\n"
                         "Camera Quality: 1920 x 1080\n"
                         "Frames:\n"
                         "Frame 1\n"
                         "File Name: File.MP4\n"
                         "Camera 3:\n"
                         "Camera Quality: 1920 x 1080\n"
                         "Frames:\n"
                         "File Name: File.MP4\n"
                         "Sensors:\n"
                         "Sensor 1:\n"
                         "Sensor: Cone Sensor\n"
                         "Sensor 2:\n"
                         "Sensor: Person Sensor\n"
                         "Sensor 3:\n"
                         "Sensor: Car Sensor\n"
                         "Objects Detected:\n"
                         "Object 1:\n"
                         "Object Name: Cone\n"
                         "Object Dimensions:\n"
                         "Length: 0.5 Meters\n"
                         "Width: 0.2 Meters\n"
                         "Height: 1 Meters\n"
                         "Object in Lane 1\n"
                         "Distance to object: 5 Meters\n"
                         "Time until impact with object at current speed: 10 Seconds\n"
                         "Object 2:\n"
                         "Object Name: Person\n"
                         "Object Dimensions:\n"
                         "Width: 0.1 Meters\n"
                         "Height: 2 Meters\n"
                         "Object in Lane 1\n"
                         "Distance to object: 5 Meters\n"
                         "Time until impact with object at current speed: 10 Seconds\n"
                         "Security System:\n"
                         "Alarm Status: Alarm Activated\n"
                         "Vehicle Unlocked\n"
                         "Alarm Not Triggered\n"
                         "Lane Marking Detection System:\n"
                         "Distance from left lane marking: 5 Meters\n"
                         "Distance from right lane marking: 0 Meters\n"
                         "In Lane\n"
                         "Infotainment System:\n"
                         "Phone Number: +447123456789\n"
                         "Emergency Contact:\n"
                         "First Name: Emergency\n"
                         "Last Name: Contact\n"
                         "Contact Number: +447987654321\n"
                         "Contacts:\n"
                         "Contact 1:\n"
                         "First Name: Emergency\n"
                         "Last Name: Contact\n"
                         "Contact Number: +447987654321\n"
                         "Messages:\n"
                         "Radio:\n"
                         "Station Name: Capital\n"
                         "FM: 95.8\n"
                         "AM: 0Hz\n"
                         "Language: English\n"
                         "Parts:\n"
                         "Part Name: Axel\n"
                         "Part ID: 1\n"
                         "Colour: \n"
                         "RGB(0, 0, 0)\n"
                         "CMYK(0, 0, 0, 100)\n"
                         "#000000\n"
                         "Manufacture: Audi\n"
                         "Length: 0.5 Meters\n"
                         "Width: 1 Meters\n"
                         "Part Name: Bonnet\n"
                         "Part ID: 1\n"
                         "Colour: \n"
                         "RGB(255, 0, 0)\n"
                         "CMYK(0, 100, 100, 0)\n"
                         "#FF0000\n"
                         "Manufacture: Audi\n"
                         "Length: 1 Meters\n"
                         "Width: 1 Meters\n"
                         "Part Name: Front Left Brake\n"
                         "Part ID: 1\n"
                         "Colour: \n"
                         "RGB(0, 0, 0)\n"
                         "CMYK(0, 0, 0, 100)\n"
                         "#000000\n"
                         "Manufacture: Audi\n"
                         "Length: 0.1 Meters\n"
                         "Width: 0.1 Meters\n"
                         "Part Name: Front Right Brake\n"
                         "Part ID: 2\n"
                         "Colour: \n"
                         "RGB(0, 0, 0)\n"
                         "CMYK(0, 0, 0, 100)\n"
                         "#000000\n"
                         "Manufacture: Audi\n"
                         "Length: 0.1 Meters\n"
                         "Width: 0.1 Meters\n"
                         "Part Name: Rear Left Brake\n"
                         "Part ID: 3\n"
                         "Colour: \n"
                         "RGB(0, 0, 0)\n"
                         "CMYK(0, 0, 0, 100)\n"
                         "#000000\n"
                         "Manufacture: Audi\n"
                         "Length: 0.1 Meters\n"
                         "Width: 0.1 Meters\n"
                         "Part Name: Rear Right Brake\n"
                         "Part ID: 4\n"
                         "Colour: \n"
                         "RGB(0, 0, 0)\n"
                         "CMYK(0, 0, 0, 100)\n"
                         "#000000\n"
                         "Manufacture: Audi\n"
                         "Length: 0.1 Meters\n"
                         "Width: 0.1 Meters\n"
                         "Part Name: Chassis\n"
                         "Part ID: 1\n"
                         "Colour: \n"
                         "RGB(0, 0, 0)\n"
                         "CMYK(0, 0, 0, 100)\n"
                         "#000000\n"
                         "Manufacture: Audi\n"
                         "Length: 1.5 Meters\n"
                         "Width: 2 Meters\n"
                         "Part Name: Front Driver Side Door\n"
                         "Part ID: 1\n"
                         "Colour: \n"
                         "RGB(255, 0, 0)\n"
                         "CMYK(0, 100, 100, 0)\n"
                         "#FF0000\n"
                         "Manufacture: Audi\n"
                         "Length: 1 Meters\n"
                         "Width: 1 Meters\n"
                         "Door Shut\n"
                         "Door Locked\n"
                         "Part Name: Front Passenger Side Door\n"
                         "Part ID: 2\n"
                         "Colour: \n"
                         "RGB(255, 0, 0)\n"
                         "CMYK(0, 100, 100, 0)\n"
                         "#FF0000\n"
                         "Manufacture: Audi\n"
                         "Length: 1 Meters\n"
                         "Width: 1 Meters\n"
                         "Door Shut\n"
                         "Door Locked\n"
                         "Part Name: Rear Driver Side Door\n"
                         "Part ID: 3\n"
                         "Colour: \n"
                         "RGB(255, 0, 0)\n"
                         "CMYK(0, 100, 100, 0)\n"
                         "#FF0000\n"
                         "Manufacture: Audi\n"
                         "Length: 1 Meters\n"
                         "Width: 1 Meters\n"
                         "Door Shut\n"
                         "Door Locked\n"
                         "Part Name: Rear Passenger Side Door\n"
                         "Part ID: 4\n"
                         "Colour: \n"
                         "RGB(255, 0, 0)\n"
                         "CMYK(0, 100, 100, 0)\n"
                         "#FF0000\n"
                         "Manufacture: Audi\n"
                         "Length: 1 Meters\n"
                         "Width: 1 Meters\n"
                         "Door Shut\n"
                         "Door Locked\n"
                         "Part Name: Engine\n"
                         "Part ID: 1\n"
                         "Colour: \n"
                         "RGB(0, 0, 0)\n"
                         "CMYK(0, 0, 0, 100)\n"
                         "#000000\n"
                         "Manufacture: Audi\n"
                         "Length: 0.5 Meters\n"
                         "Width: 0.5 Meters\n"
                         "Height: 0.5 Meters\n"
                         "Engine Size: 2L\n"
                         "Break Horse Power: 250\n"
                         "Number of Cylinders: 12\n"
                         "Number of Valves: 8\n"
                         "Mode: Sport\n"
                         "Part Name: Suspension\n"
                         "Part ID: 1\n"
                         "Colour: \n"
                         "RGB(0, 0, 0)\n"
                         "CMYK(0, 0, 0, 100)\n"
                         "#000000\n"
                         "Manufacture: Audi\n"
                         "Length: 1.5 Meters\n"
                         "Width: 2 Meters\n"
                         "Part Name: Trunk\n"
                         "Part ID: 1\n"
                         "Colour: \n"
                         "RGB(255, 0, 0)\n"
                         "CMYK(0, 100, 100, 0)\n"
                         "#FF0000\n"
                         "Manufacture: Audi\n"
                         "Length: 1 Meters\n"
                         "Width: 1 Meters\n"
                         "Trunk Shut\n"
                         "Trunk Locked\n"
                         "Part Name: Front Left Tyre\n"
                         "Part ID: 1\n"
                         "Colour: \n"
                         "RGB(0, 0, 0)\n"
                         "CMYK(0, 0, 0, 100)\n"
                         "#000000\n"
                         "Manufacture: Audi\n"
                         "Diameter: 3 Meters\n"
                         "Radius: 3 Meters\n"
                         "Current Air Pressure: 50 psi\n"
                         "Tyre Thread Remaining: 10 mm\n"
                         "Part Name: Front Right Tyre\n"
                         "Part ID: 2\n"
                         "Colour: \n"
                         "RGB(0, 0, 0)\n"
                         "CMYK(0, 0, 0, 100)\n"
                         "#000000\n"
                         "Manufacture: Audi\n"
                         "Diameter: 3 Meters\n"
                         "Radius: 3 Meters\n"
                         "Current Air Pressure: 50 psi\n"
                         "Tyre Thread Remaining: 10 mm\n"
                         "Part Name: Rear Left Tyre\n"
                         "Part ID: 3\n"
                         "Colour: \n"
                         "RGB(0, 0, 0)\n"
                         "CMYK(0, 0, 0, 100)\n"
                         "#000000\n"
                         "Manufacture: Audi\n"
                         "Diameter: 3 Meters\n"
                         "Radius: 3 Meters\n"
                         "Current Air Pressure: 50 psi\n"
                         "Tyre Thread Remaining: 10 mm\n"
                         "Part Name: Rear Right Tyre\n"
                         "Part ID: 4\n"
                         "Colour: \n"
                         "RGB(0, 0, 0)\n"
                         "CMYK(0, 0, 0, 100)\n"
                         "#000000\n"
                         "Manufacture: Audi\n"
                         "Diameter: 3 Meters\n"
                         "Radius: 3 Meters\n"
                         "Current Air Pressure: 50 psi\n"
                         "Tyre Thread Remaining: 10 mm\n"
                         "Part Name: Front Left Wheel\n"
                         "Part ID: 1\n"
                         "Colour: \n"
                         "RGB(0, 0, 0)\n"
                         "CMYK(0, 0, 0, 100)\n"
                         "#000000\n"
                         "Manufacture: Audi\n"
                         "Diameter: 3 Meters\n"
                         "Radius: 3 Meters\n"
                         "Part Name: Front Right Wheel\n"
                         "Part ID: 2\n"
                         "Colour: \n"
                         "RGB(0, 0, 0)\n"
                         "CMYK(0, 0, 0, 100)\n"
                         "#000000\n"
                         "Manufacture: Audi\n"
                         "Diameter: 3 Meters\n"
                         "Radius: 3 Meters\n"
                         "Part Name: Rear Left Wheel\n"
                         "Part ID: 3\n"
                         "Colour: \n"
                         "RGB(0, 0, 0)\n"
                         "CMYK(0, 0, 0, 100)\n"
                         "#000000\n"
                         "Manufacture: Audi\n"
                         "Diameter: 3 Meters\n"
                         "Radius: 3 Meters\n"
                         "Part Name: Rear Right Wheel\n"
                         "Part ID: 4\n"
                         "Colour: \n"
                         "RGB(0, 0, 0)\n"
                         "CMYK(0, 0, 0, 100)\n"
                         "#000000\n"
                         "Manufacture: Audi\n"
                         "Diameter: 3 Meters\n"
                         "Radius: 3 Meters\n"
                         "Current Lane: Lane 3\n"
                         "Part Name: Transmission\n"
                         "Part ID: 1\n"
                         "Colour: \n"
                         "RGB(0, 0, 0)\n"
                         "CMYK(0, 0, 0, 100)\n"
                         "#000000\n"
                         "Manufacture: Audi\n"
                         "Length: 0.5 Meters\n"
                         "Width: 0.5 Meters\n"
                         "Height: 0.5 Meters\n"
                         "Transmission: Manual\n"
                         "Number of Gears: 6\n"
                         "Current Gear: 3\n"
                         "Speed:\n"
                         "Current Speed: 20MPH\n"
                         "Top Speed: 150MPH\n"
                         "0-60 MPH Speed: 5 seconds \n"
                         "Steering:\n"
                         "Wheel rotation: 0 degrees\n"
                         "Indicators:\n"
                         "Right Indicator Off\n"
                         "Left Indicator Off\n"
                         "Logs:\n"
                         "Car Unlocked\n"
                         "Driver Authenticated\n"
                         "Car Started\n"
                         "Destination Set\n"
                         "Accelerating\n"
                         "Decelerating\n"
                         "Arrived")


if __name__ == '__main__':
    unittest.main()
