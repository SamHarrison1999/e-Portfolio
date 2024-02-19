import re
from abc import ABC, abstractmethod
from collections import OrderedDict, deque

from AutoPilot import AutoPilot
from Body import Body
from Camera import Camera
from Collision import Collision
from Colour import Colour
from CruiseControl import CruiseControl
from Engine import Engine, Mode
from Fuel import Fuel, FuelType
from GPS import GPS
from InfotainmentSystem import InfotainmentSystem
from LaneMarkingDetection import LaneMarkingDetection
from Mileage import Mileage
from ObjectDetection import ObjectDetection
from Part import Part
from Person import Driver, Passenger
from Phone import Phone
from Radio import Radio
from Road import Road, RoadType
from RoadSign import RoadSign
from Route import Route
from SecuritySystem import SecuritySystem
from Sensor import Sensor
from Speed import Speed
from Steering import Steering
from Tyre import Tyre
from Transmission import Transmission, TransmissionType
from Utils import is_null_or_white_space
from Weather import Weather

# TODO Add comments throughout

class Vehicle(ABC):

    @property
    @abstractmethod
    def auto_pilot(self) -> AutoPilot:
        pass

    @auto_pilot.setter
    @abstractmethod
    def auto_pilot(self, auto_pilot: AutoPilot):
        pass

    @property
    @abstractmethod
    def body(self) -> Body:
        pass

    @body.setter
    @abstractmethod
    def body(self, body: Body):
        pass

    @property
    @abstractmethod
    def cameras(self) -> list[Camera]:
        pass

    @cameras.setter
    @abstractmethod
    def cameras(self, cameras: list[cameras]):
        pass

    @property
    @abstractmethod
    def chassis(self) -> list[Part]:
        pass

    @chassis.setter
    @abstractmethod
    def chassis(self, chassis: list[Part]):
        pass

    @property
    @abstractmethod
    def colour(self) -> Colour:
        pass

    @colour.setter
    @abstractmethod
    def colour(self, colour: Colour):
        pass

    @property
    @abstractmethod
    def cruise_control(self) -> CruiseControl:
        pass

    @cruise_control.setter
    @abstractmethod
    def cruise_control(self, cruise_control: CruiseControl):
        pass

    @property
    @abstractmethod
    def dimensions(self) -> OrderedDict[str, int]:
        pass

    @dimensions.setter
    @abstractmethod
    def dimensions(self, dimensions: OrderedDict[str, int]):
        pass

    @property
    @abstractmethod
    def drive_train(self) -> str:
        pass

    @drive_train.setter
    @abstractmethod
    def drive_train(self, drive_train: str):
        pass

    @property
    @abstractmethod
    def engine(self) -> Engine:
        pass

    @engine.setter
    @abstractmethod
    def engine(self, engine: Engine):
        pass

    @property
    @abstractmethod
    def fuel(self) -> Fuel:
        pass

    @fuel.setter
    @abstractmethod
    def fuel(self, fuel: Fuel):
        pass

    @property
    @abstractmethod
    def gps(self) -> GPS:
        pass

    @gps.setter
    @abstractmethod
    def gps(self, gps: GPS):
        pass

    @property
    @abstractmethod
    def infotainment_system(self) -> InfotainmentSystem:
        pass

    @infotainment_system.setter
    @abstractmethod
    def infotainment_system(self, infotainment_system):
        pass

    @property
    @abstractmethod
    def interior(self) -> list[Part]:
        pass

    @interior.setter
    @abstractmethod
    def interior(self, interior: list[Part]):
        pass

    @property
    @abstractmethod
    def lane(self):
        pass

    @lane.setter
    def lane(self, lane):
        pass

    @property
    @abstractmethod
    def lane_marking_detection(self) -> LaneMarkingDetection:
        pass

    @lane_marking_detection.setter
    @abstractmethod
    def lane_marking_detection(self, lane_marking_detection):
        pass

    @property
    @abstractmethod
    def make(self) -> str:
        pass

    @make.setter
    @abstractmethod
    def make(self, make: str):
        pass

    @property
    @abstractmethod
    def mileage(self) -> Mileage:
        pass

    @mileage.setter
    @abstractmethod
    def mileage(self, mileage: Mileage):
        pass

    @property
    @abstractmethod
    def model(self) -> str:
        pass

    @model.setter
    @abstractmethod
    def model(self, model: str):
        pass

    @property
    @abstractmethod
    def object_detection(self) -> ObjectDetection:
        pass

    @object_detection.setter
    @abstractmethod
    def object_detection(self, object_detection):
        pass

    @property
    @abstractmethod
    def driver(self) -> Driver:
        pass

    @driver.setter
    @abstractmethod
    def driver(self, driver: Driver):
        pass

    @property
    @abstractmethod
    def passengers(self) -> list[Passenger]:
        pass

    @passengers.setter
    @abstractmethod
    def passengers(self, passengers: list[Passenger]):
        pass

    @property
    @abstractmethod
    def registration_number(self) -> str:
        pass

    @registration_number.setter
    @abstractmethod
    def registration_number(self, registration_number: str):
        pass

    @property
    @abstractmethod
    def running_costs(self) -> dict[str, int]:
        pass

    @running_costs.setter
    @abstractmethod
    def running_costs(self, running_costs: dict[str, int]):
        pass

    @property
    @abstractmethod
    def security_system(self) -> SecuritySystem:
        pass

    @security_system.setter
    @abstractmethod
    def security_system(self, security_system: SecuritySystem):
        pass

    @property
    @abstractmethod
    def sensors(self) -> list[Sensor]:
        pass

    @sensors.setter
    @abstractmethod
    def sensors(self, sensors: list[Sensor]):
        pass

    @property
    @abstractmethod
    def speed(self) -> Speed:
        pass

    @speed.setter
    @abstractmethod
    def speed(self, speed: Speed):
        pass

    @property
    @abstractmethod
    def steering(self) -> Steering:
        pass

    @steering.setter
    @abstractmethod
    def steering(self, steering: Steering):
        pass

    @property
    @abstractmethod
    def suspension(self) -> list[Part]:
        pass

    @suspension.setter
    @abstractmethod
    def suspension(self, suspension: list[Part]):
        pass

    @property
    @abstractmethod
    def tyres(self) -> list[Tyre]:
        pass

    @tyres.setter
    @abstractmethod
    def tyres(self, tires: list[Tyre]):
        pass

    @property
    @abstractmethod
    def transmission(self) -> Transmission:
        pass

    @transmission.setter
    @abstractmethod
    def transmission(self, transmission: Transmission):
        pass

    @property
    @abstractmethod
    def weight(self) -> float:
        pass

    @weight.setter
    @abstractmethod
    def weight(self, weight: float):
        pass

    @property
    @abstractmethod
    def year(self) -> int:
        pass

    @year.setter
    @abstractmethod
    def year(self, year: int):
        pass

    @abstractmethod
    def accelerate(self):
        pass

    @abstractmethod
    def alarm_triggered(self):
        pass

    @abstractmethod
    def avoid_collision(self):
        pass

    @abstractmethod
    def decelerate(self):
        pass

    @abstractmethod
    def emergency_stop(self):
        pass

    @abstractmethod
    def gear_down(self):
        pass

    @abstractmethod
    def gear_up(self):
        pass

    @abstractmethod
    def move_to_left_lane(self):
        pass

    @abstractmethod
    def move_to_right_lane(self):
        pass

    @abstractmethod
    def park(self):
        pass

    @abstractmethod
    def reverse(self):
        pass

    @abstractmethod
    def reverse_bay_park(self):
        pass

    @abstractmethod
    def set_recommended_following_distance_for_auto_pilot(self):
        pass

    @abstractmethod
    def redirect_to_closest_petrol_station(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):

    def __init__(self, auto_pilot: AutoPilot, body: Body, cameras: list[Camera], chassis: list[Part], colour: Colour,
                 cruise_control: CruiseControl, dimensions: OrderedDict[str, int], drive_train: str, engine: Engine,
                 fuel: Fuel, gps: GPS, infotainment_system: InfotainmentSystem, interior: list[Part], lane: int,
                 lane_marking_detection: LaneMarkingDetection, make: str, mileage: Mileage, model: str,
                 object_detection: ObjectDetection, driver: Driver, passengers: list[Passenger],
                 registration_number: str, running_costs: dict[str, int], security_system: SecuritySystem,
                 sensors: list[Sensor], speed: Speed, steering: Steering, suspension: list[Part], tyres: list[Tyre],
                 transmission: Transmission, weight: float, year: int):
        self.__auto_pilot = auto_pilot
        self.__body = body
        # If there are no camera in the car set the list of camera to an empty list
        if cameras:
            self.__cameras = cameras
        else:
            self.__cameras = []
        # If there is no chassis throw an error
        if chassis:
            self.__chassis = chassis
        else:
            raise ValueError("The chassis has to be made up of parts")
        self.__colour = colour
        self.__cruise_control = cruise_control
        # If the dimensions of the vehicle aren't positive numbers throw an error
        if dimensions["Length"] > 0 and dimensions["Width"] > 0 and dimensions["Height"] > 0:
            self.__dimensions = dimensions
        else:
            raise ValueError("The length, width and height of the vehicle must be a positive number")
        # If the drive train is empty throw an error
        if is_null_or_white_space(drive_train):
            raise ValueError("Drive train can't be null")
        else:
            self.__drive_train = drive_train
        self.__engine = engine
        self.__fuel = fuel
        self.__gps = gps
        self.__infotainment_system = infotainment_system
        # If there is no interior throw an error
        if interior:
            self.__interior = interior
        else:
            raise ValueError("The vehicle must have an interior")
        # If current lane is not a positive number throw an error
        if lane > 0:
            self.__lane = lane
        else:
            raise ValueError("Current lane must be a positive number")
        self.__lane_marking_detection = lane_marking_detection
        # If the vehicle has no make throw an error
        if is_null_or_white_space(make):
            raise ValueError("A vehicle must have a make")
        else:
            self.__make = make
        self.__mileage = mileage
        # If the vehicle has no model name throw an error
        if is_null_or_white_space(model):
            raise ValueError("A vehicle must have a model")
        else:
            self.__model = model
        self.__object_detection = object_detection
        self.__driver = driver
        # If there are no passengers set the list of passenger to am empty list
        if passengers:
            self.__passengers = passengers
        else:
            self.__passengers = []
        # If the reg number is not valid throw an error
        regex = re.compile(
            r'(^[A-Z]{2}[0-9]{2}\s?[A-Z]{3}$)|(^[A-Z][0-9]{1,3}[A-Z]{3}$)|(^[A-Z]{3}[0-9]{1,3}[A-Z]$)|(^[0-9]{1,4}[A-Z]{1,2}$)|(^[0-9]{1,3}[A-Z]{1,3}$)|(^[A-Z]{1,2}[0-9]{1,4}$)|(^[A-Z]{1,3}[0-9]{1,3}$)|(^[A-Z]{1,3}[0-9]{1,4}$)|(^[0-9]{3}[DX][0-9]{3}$)')
        if is_null_or_white_space(registration_number) or not regex.search(registration_number):
            raise ValueError("Registration number is not valid")
        else:
            self.__registration_number = registration_number
        for cost in running_costs.values():
            if cost < 0:
                raise ValueError("Running cost can't be less than 0")
        self.__running_costs = running_costs
        self.__security_system = security_system
        # If there are no sensors the list of sensors is an empty list
        if sensors:
            self.__sensors = sensors
        else:
            self.__sensors = []
        self.__speed = speed
        self.__steering = steering
        # If there is no suspension throw an error
        if suspension:
            self.__suspension = suspension
        else:
            raise ValueError("A vehicle has to have a suspension")
        # If there are no tyres the list of tyres is an empty list
        if tyres:
            self.__tyres = tyres
        else:
            self.__tyres = []
        self.__transmission = transmission
        if weight > 0:
            self.__weight = weight
        else:
            raise ValueError("The weight of the vehicle must be a positive number")
        if year > 0:
            self.__year = year
        else:
            raise ValueError("The year the vehicle was made must be greater than 0")

    def __str__(self):
        return f'{self.__auto_pilot}\n{self.__body}' + f''.join(f"\nCamera:\n{camera}" for camera in self.__cameras) + \
               f''.join(f"\nChassis:\n{chassis_part}" for chassis_part in
                        self.__chassis) + f'\nVehicle Colour: \n{self.__colour}\n{self.__cruise_control}' + \
               f"\nVehicle Dimensions:" + f"".join(
            f"\n{key.capitalize()}: {value}" for key, value in self.__dimensions.items()) + \
               f'\nDrive Train: {self.__drive_train}\n{self.__engine}\n{self.__fuel}\n{self.__gps}\n{self.__infotainment_system}' + \
               f'\n'.join(f"\n{interior_part}" for interior_part in
                          self.__interior) + f'\nLane: {self.__lane}\n{self.__lane_marking_detection}\n' + \
               f'Make: {self.__make}\n{self.__mileage}\nModel: {self.__model}\n{self.__object_detection}\n{self.__driver}\n' + \
               f'\n'.join(f"{passenger}" for passenger in
                          self.__passengers) + f'\nRegistration Number: {self.__registration_number}' + \
               f'\nRunning Costs: ' + f"".join(
            f"\n{key.capitalize()}: £{value}" for key, value in self.__running_costs.items()) + \
               f'\n{self.__security_system}' + f''.join(
            f"\n{sensor}" for sensor in self.__sensors) + f'\n{self.__speed}\n{self.__steering}' + \
               f'\nSuspension: \n' + f'\n'.join(f"{suspension_part}" for suspension_part in self.__suspension) + \
               f'\nTyres: \n' + f'\n'.join(f"{tyre}" for tyre in
                                           self.__tyres) + f'\n{self.__transmission}\nWeight: {self.__weight}\nYear: {self.__year}'

    @property
    def auto_pilot(self):
        return self.__auto_pilot

    @auto_pilot.setter
    def auto_pilot(self, auto_pilot: AutoPilot):
        self.__auto_pilot = auto_pilot

    @property
    def body(self):
        return self.__body

    @body.setter
    def body(self, body: Body):
        self.__body = body

    @property
    def cameras(self):
        return self.__cameras

    @cameras.setter
    def cameras(self, cameras: list[cameras]):
        # If there are no camera in the car set the list of camera to an empty list
        if cameras:
            self.__cameras = cameras
        else:
            self.__cameras = []

    @property
    def chassis(self):
        return self.__chassis

    @chassis.setter
    def chassis(self, chassis: list[Part]):
        # If there is no chassis throw an error
        if chassis:
            self.__chassis = chassis
        else:
            raise ValueError("The chassis has to be made up of parts")

    @property
    def colour(self):
        return self.__colour

    @colour.setter
    def colour(self, colour: Colour):
        self.__colour = colour

    @property
    def cruise_control(self):
        return self.__cruise_control

    @cruise_control.setter
    def cruise_control(self, cruise_control: CruiseControl):
        self.__cruise_control = cruise_control

    @property
    def dimensions(self):
        return self.__dimensions

    @dimensions.setter
    def dimensions(self, dimensions: OrderedDict[str, int]):
        # If the dimensions of the vehicle aren't positive numbers throw an error
        if dimensions["Length"] > 0 and dimensions["Width"] > 0 and dimensions["Height"] > 0:
            self.__dimensions = dimensions
        else:
            raise ValueError("The length, width and height of the vehicle must be a positive number")

    @property
    def drive_train(self) -> str:
        return self.__drive_train

    @drive_train.setter
    def drive_train(self, drive_train: str):
        # If the drive train is empty throw an error
        if is_null_or_white_space(drive_train):
            self.__drive_train = drive_train
        else:
            raise ValueError("Drive train can't be null")

    @property
    def engine(self):
        return self.__engine

    @engine.setter
    def engine(self, engine: Engine):
        self.__engine = engine

    @property
    def fuel(self):
        return self.__fuel

    @fuel.setter
    def fuel(self, fuel: Fuel):
        self.__fuel = fuel

    @property
    def gps(self):
        return self.__gps

    @gps.setter
    def gps(self, gps: GPS):
        self.__gps = gps

    @property
    def infotainment_system(self):
        return self.__infotainment_system

    @infotainment_system.setter
    def infotainment_system(self, infotainment_system):
        self.__infotainment_system = infotainment_system

    @property
    def interior(self):
        return self.__interior

    @interior.setter
    def interior(self, interior: list[Part]):
        # If there is no interior throw an error
        if interior:
            self.__interior = interior
        else:
            raise ValueError("The vehicle must have an interior")

    @property
    def lane(self):
        return self.__lane

    @lane.setter
    def lane(self, lane: int):
        # If current lane is not a positive number throw an error
        if lane > 0:
            self.__lane = lane
        else:
            raise ValueError("Current lane must be a positive number")

    @property
    def lane_marking_detection(self):
        return self.__lane_marking_detection

    @lane_marking_detection.setter
    def lane_marking_detection(self, lane_marking_detection):
        self.__lane_marking_detection = lane_marking_detection

    @property
    def make(self):
        return self.__make

    @make.setter
    def make(self, make: str):
        # If the vehicle has no make throw an error
        if is_null_or_white_space(make):
            self.__make = make
        else:
            raise ValueError("A vehicle must have a make")

    @property
    def mileage(self):
        return self.__mileage

    @mileage.setter
    def mileage(self, mileage: Mileage):
        self.__mileage = mileage

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model: str):
        # If the vehicle has no model name throw an error
        if is_null_or_white_space(model):
            self.__model = model
        else:
            raise ValueError("A vehicle must have a model")

    @property
    def object_detection(self):
        return self.__object_detection

    @object_detection.setter
    def object_detection(self, object_detection):
        self.__object_detection = object_detection

    @property
    def driver(self):
        return self.__driver

    @driver.setter
    def driver(self, driver: Driver):
        self.__driver = driver

    @property
    def passengers(self):
        return self.__passengers

    @passengers.setter
    def passengers(self, passengers: list[Passenger]):
        # If there are no passengers set the list of passenger to am empty list
        if passengers:
            self.__passengers = passengers
        else:
            self.__passengers = []

    @property
    def registration_number(self):
        return self.__registration_number

    @registration_number.setter
    def registration_number(self, registration_number: str):
        # If the reg number is not valid throw an error
        regex = re.compile(
            r'^([A-Z]{2}[0-9]{2}\s?[A-Z]{3}$) | (^[A-Z][0-9]{1, 3}[A-Z]{3}$) | (^[A-Z]{3}[0-9]{1, 3}[A-Z]$) | (^[0-9]{1, 4}[A-Z]{1, 2}$) | (^[0-9]{1, 3}[A-Z]{1, 3}$) | (^[A-Z]{1, 2}[0-9]{1, 4}$) | (^[A-Z]{1, 3}[0-9]{1, 3}$)')
        if is_null_or_white_space(registration_number) or not regex.search(registration_number):
            raise ValueError("Registration number is not valid")
        else:
            self.__registration_number = registration_number

    @property
    def running_costs(self):
        return self.__running_costs

    @running_costs.setter
    def running_costs(self, running_costs: dict[str, int]):
        for cost in running_costs.values():
            if cost < 0:
                raise ValueError("Running cost can't be less than 0")
        self.__running_costs = running_costs

    @property
    def security_system(self):
        return self.__security_system

    @security_system.setter
    def security_system(self, security_system: SecuritySystem):
        self.__security_system = security_system

    @property
    def sensors(self):
        return self.__sensors

    @sensors.setter
    def sensors(self, sensors: list[Sensor]):
        # If there are no sensors the list of sensors is an empty list
        if sensors:
            self.__sensors = sensors
        else:
            self.__sensors = []

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, speed: Speed):
        self.__speed = speed

    @property
    def steering(self):
        return self.__steering

    @steering.setter
    def steering(self, steering: Steering):
        self.__steering = steering

    @property
    def suspension(self):
        return self.__suspension

    @suspension.setter
    def suspension(self, suspension: list[Part]):
        # If there is no suspension throw an error
        if suspension:
            self.__suspension = suspension
        else:
            raise ValueError("A vehicle has to have a suspension")

    @property
    def tyres(self):
        return self.__tyres

    @tyres.setter
    def tyres(self, tyres: list[Tyre]):
        # If there are no tyres the list of tyres is an empty list
        if tyres:
            self.__tyres = tyres
        else:
            self.__tyres = []

    @property
    def transmission(self):
        return self.__transmission

    @transmission.setter
    def transmission(self, transmission: Transmission):
        self.__transmission = transmission

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight: float):
        if weight > 0:
            self.__weight = weight
        else:
            raise ValueError("The weight of the vehicle must be a positive number")

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year: int):
        if year > 0:
            self.__year = year
        else:
            raise ValueError("The year the vehicle was made must be greater than 0")

    def accelerate(self):
        if self.__auto_pilot.enabled and self.__auto_pilot.following_distance > self.__auto_pilot.recommended_following_distance and self.__speed.current_speed < self.__gps.road.speed_limit:
            self.__speed.accelerate()
        elif self.__cruise_control.activated and self.__speed.current_speed < self.__cruise_control.speed and self.__cruise_control.following_distance > self.__cruise_control.recommended_following_distance:
            self.__speed.accelerate()
        elif not self.__cruise_control.activated:
            self.__speed.accelerate()

    def alarm_triggered(self):
        if self.__security_system.alarm_triggered:
            self.__infotainment_system.call_emergency_services()

    def avoid_collision(self):
        if self.__object_detection.distance_to_object >= self.__auto_pilot.following_distance and self.__auto_pilot.enabled and not self.__gps.road.traffic_jam():
            if self.__lane < self.__gps.road.number_of_lanes:
                self.move_to_right_lane()
            else:
                self.move_to_left_lane()
        elif self.__cruise_control.activated and self.__object_detection.distance_to_object > self.__cruise_control.following_distance and not self.__gps.road.traffic_jam():
            if self.__lane < self.__gps.road.number_of_lanes:
                self.move_to_right_lane()
            else:
                self.move_to_left_lane()
        else:
            self.emergency_stop()

    def decelerate(self):
        if self.__auto_pilot.enabled and self.__speed.current_speed > self.__gps.road.speed_limit:
            self.__speed.decelerate()
        elif self.__auto_pilot.enabled and self.__auto_pilot.following_distance < self.__auto_pilot.recommended_following_distance:
            self.__speed.decelerate()
        elif self.__cruise_control.activated and self.__cruise_control.following_distance < self.__cruise_control.recommended_following_distance:
            self.__speed.decelerate()
        elif self.__cruise_control.activated and self.__speed.current_speed > self.__cruise_control.speed:
            self.__speed.decelerate()
        elif not self.__cruise_control.activated and not self.__auto_pilot.enabled:
            self.__speed.decelerate()

    def emergency_stop(self):
        self.__object_detection.collision.emergency_stop()
        self.stop()

    def gear_down(self):
        self.__transmission.gear_up()

    def gear_up(self):
        self.__transmission.gear_down()

    def move_to_left_lane(self):
        if self.__lane < self.__gps.road.number_of_lanes:
            self.__lane += 1

    def move_to_right_lane(self):
        if self.__lane - 1 > 0:
            self.__lane -= 1

    def park(self):
        self.stop()

    def reverse(self):
        self.__transmission.current_gear = 0
        self.accelerate()

    def reverse_bay_park(self):
        self.stop()
        self.reverse()
        self.stop()

    def set_recommended_following_distance_for_auto_pilot(self):
        self.__auto_pilot.recommended_following_distance = self.__speed.current_speed * 1  # 1 metre for every one mile per hour, of your speed

    def redirect_to_closest_petrol_station(self):
        if self.__auto_pilot.enabled and self.__fuel.fuel_remaining < 10:
            self.__gps.destination = self.__fuel.closest_petrol_station

    def stop(self):
        self.__speed.current_speed = 0


def main():
    weather = Weather("Sunny", 25)
    auto_pilot = AutoPilot(True, ["Rock", "Cone"], 30, 30, weather)
    trunk_colour = Colour(1, 0.2, 0.3, 0.4)
    trunk_dimensions = OrderedDict()
    trunk_dimensions["Length"] = 200
    trunk_dimensions["Width"] = 100
    trunk_dimensions["Height"] = 2000
    trunk = Part(1, "Trunk", trunk_colour, "Audi", trunk_dimensions)
    car_body_parts = [trunk]
    body = Body("Coupe", car_body_parts)
    camera_one_pixels = frozenset([1920, 1080])
    camera_one_frames = deque()
    camera_one_frames.append("Frame 1")
    camera_one_frames.append("Frame 2")
    camera_one = Camera(camera_one_pixels, camera_one_frames, "MP4")
    camera_two_pixels = frozenset([1920, 1080])
    camera_two_frames = deque()
    camera_two_frames.append("Frame 1")
    camera_two_frames.append("Frame 2")
    camera_two = Camera(camera_two_pixels, camera_two_frames, "MP4")
    cameras = [camera_one, camera_two]
    front_axel_colour = Colour(1, 0.2, 0.3, 0.4)
    front_axel_dimensions = OrderedDict()
    front_axel_dimensions["Length"] = 200
    front_axel_dimensions["Width"] = 100
    front_axel_dimensions["Height"] = 2000
    front_axel = Part(1, "Front Axel", front_axel_colour, "Audi", front_axel_dimensions)
    car_chassis_parts = [front_axel]
    car_colour = Colour(1, 0.2, 0.3, 0.4)
    speed = Speed(100, 5, 30)
    cruise_control = CruiseControl(True, 70, 30, 30, speed)
    car_dimensions = OrderedDict()
    car_dimensions["Length"] = 2000
    car_dimensions["Width"] = 1000
    car_dimensions["Height"] = 2000
    gear_box_colour = Colour(1, 0.2, 0.3, 0.4)
    crankshaft_colour = Colour(0.2, 0.5, 0.7, 0.8)
    gearbox_dimensions = OrderedDict()
    gearbox_dimensions["Length"] = 100
    gearbox_dimensions["Width"] = 50
    gearbox_dimensions["Height"] = 200
    crankshaft_dimensions = OrderedDict()
    crankshaft_dimensions["Length"] = 50
    crankshaft_dimensions["Width"] = 50
    crankshaft_dimensions["Height"] = 250
    gearbox = Part(1, "Gear Box", gear_box_colour, "Audi", gearbox_dimensions)
    crankshaft = Part(2, "Crankshaft", crankshaft_colour, "Audi", crankshaft_dimensions)
    parts = [gearbox, crankshaft]
    engine = Engine(2, 250, 12, 8, 1000, 100, Mode.SPORT, parts)
    closest_petrol_station = OrderedDict()
    closest_petrol_station["latitude"] = 10
    closest_petrol_station["longitude"] = 50
    fuel = Fuel(FuelType.DIESEL, 100, 50, closest_petrol_station)
    current_location = OrderedDict()
    current_location["latitude"] = 10
    current_location["longitude"] = 50
    destination = OrderedDict()
    destination["latitude"] = 10
    destination["longitude"] = 60
    directions_to_destination = deque()
    directions_to_destination_using_shortest_route = deque()
    directions_to_destination_using_quickest_route = deque()
    directions_to_destination.append("In 500 yards turn left")
    directions_to_destination.append("In 300 yards turn right")
    directions_to_destination.append("In 2 miles you have reached your destination")
    directions_to_destination_using_shortest_route.append("In 1 mile turn left")
    directions_to_destination_using_shortest_route.append("In 500 yards you have reached your destination")
    directions_to_destination_using_quickest_route.append("In 1.2 miles turn left")
    directions_to_destination_using_quickest_route.append("in 200 yards you have reached your destination")
    route = Route(10, 10, directions_to_destination)
    shortest_route = Route(1, 10, directions_to_destination_using_shortest_route)
    quickest_route = Route(10, 1, directions_to_destination_using_quickest_route)
    routes = [route, shortest_route, quickest_route]
    sign = RoadSign(30)
    road = Road("M25", 3, RoadType.MOTORWAY, current_location, False, sign)
    gps = GPS(current_location, destination, 500, routes, road)
    emergency_contact = OrderedDict()
    emergency_contact["Name"] = "Emergency Contact"
    emergency_contact["number"] = "+447987654321"
    phone = Phone("+447123456789", emergency_contact, [], [])
    radio = Radio("Capital", 95.8, None)
    infotainment_system = InfotainmentSystem(phone, radio, "English")
    infotainment_system.change_radio_station("Kiss", 100.0, None)
    seat_colour = Colour(1, 0.2, 0.3, 0.4)
    seat_dimensions = OrderedDict()
    seat_dimensions["Length"] = 200
    seat_dimensions["Width"] = 100
    seat_dimensions["Height"] = 2000
    seat = Part(1, "Seat", seat_colour, "Audi", seat_dimensions)
    car_interior_parts = [seat]
    vehicle_size = OrderedDict()
    vehicle_size["length"] = 100
    vehicle_size["width"] = 50
    left_lane_marking_position = OrderedDict()
    left_lane_marking_position["latitude"] = 10
    left_lane_marking_position["longitude"] = 50
    right_lane_marking_position = OrderedDict()
    right_lane_marking_position["latitude"] = 10
    right_lane_marking_position["longitude"] = 50
    vehicle_position = OrderedDict()
    vehicle_position["latitude"] = 10
    vehicle_position["longitude"] = 50
    lane_marking_detection = LaneMarkingDetection(vehicle_size, left_lane_marking_position, right_lane_marking_position,
                                                  vehicle_position,
                                                  100, True)
    mileage = Mileage(40, 100000)
    location_of_object = OrderedDict()
    location_of_object["latitude"] = 10
    location_of_object["longitude"] = 50
    size_of_object = OrderedDict()
    size_of_object["length"] = 5
    size_of_object["width"] = 5
    size_of_object["height"] = 10
    collision_detection = Collision(False, False, False)
    object_detection = ObjectDetection("Cone", size_of_object, 5, 10, location_of_object, 5, collision_detection)
    driver_vitals = {
        "heart rate": 100,
        "blood pressure": 50,
        "pulse": 30
    }
    passenger_vitals = {
        "heart rate": 120,
        "blood pressure": 60,
        "pulse": 80
    }
    credentials = OrderedDict()
    credentials["username"] = "test"
    credentials["password"] = "qwerty"
    driver = Driver(credentials, driver_vitals)
    passenger = Passenger(passenger_vitals)
    passengers = [passenger]
    running_costs = {
        "Road Tax": 120,
        "Insurance": 600
    }
    security_system = SecuritySystem(True)
    objects = [object_detection]
    sensor = Sensor("Object Sensor", objects)
    sensors = [sensor]
    speed = Speed(150, 5, 70)
    steering = Steering(50)
    shock_absorber_colour = Colour(1, 0.2, 0.3, 0.4)
    shock_absorber_dimensions = OrderedDict()
    shock_absorber_dimensions["Length"] = 200
    shock_absorber_dimensions["Width"] = 100
    shock_absorber_dimensions["Height"] = 2000
    shock_absorber = Part(1, "Shock Absorber", shock_absorber_colour, "Audi", shock_absorber_dimensions)
    car_suspension_parts = [shock_absorber]
    wheel_colour = Colour(0, 0, 0, 1)
    rim_colour = Colour(0, 0, 0, 0)
    wheel_dimensions = OrderedDict()
    wheel_dimensions["Width"] = 200
    wheel_dimensions["Length"] = 200
    wheel_dimensions["Height"] = 20
    rim_dimensions = OrderedDict()
    rim_dimensions["Width"] = 100
    rim_dimensions["Length"] = 10
    rim_dimensions["Height"] = 10
    wheel = Part(1, "wheel", wheel_colour, "Audi", wheel_dimensions)
    rim = Part(2, "rim", rim_colour, "Audi", rim_dimensions)
    parts = [wheel, rim]
    tyre = Tyre(parts, 10, 50)
    tyres = [tyre, tyre, tyre, tyre]
    transmission = Transmission(TransmissionType.MANUAL, 6, 3)
    car = Car(auto_pilot, body, cameras, car_chassis_parts, car_colour, cruise_control, car_dimensions, "4x4", engine,
              fuel, gps, infotainment_system, car_interior_parts, 1, lane_marking_detection, "Audi", mileage,
              "A4", object_detection, driver, passengers, "KD19OCL", running_costs, security_system, sensors, speed,
              steering, car_suspension_parts, tyres, transmission, 2, 2024)
    print(car)


if __name__ == "__main__":
    main()
