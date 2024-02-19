import datetime
import re

from Main.Colour.Colour import Colour
from Main.Utils.Utils import is_null_or_white_space
from Main.Vehicle.AutoPilot import AutoPilot
from Main.Vehicle.BodyType import BodyType
from Main.Vehicle.CollisionDetectionSystem import CollisionDetectionSystem
from Main.Vehicle.CruiseControl import CruiseControl
from Main.Vehicle.DriveSystem import DriveSystem
from Main.Vehicle.Fuel import Fuel
from Main.Vehicle.GPS import GPS
from Main.Vehicle.InfotainmentSystem import InfotainmentSystem
from Main.Vehicle.LaneMarkingDetectionSystem import LaneMarkingDetectionSystem
from Main.Vehicle.Mileage import Mileage
from Main.Vehicle.ObjectDetectionSystem import ObjectDetectionSystem
from Main.Vehicle.Part import Part
from Main.Vehicle.SecuritySystem import SecuritySystem
from Main.Vehicle.Speed import Speed
from Main.Vehicle.Steering import Steering
from Main.Vehicle.Transmission import Transmission

# Regex for a vehicle registration number
REGISTRATION_NUMBER_REGEX = re.compile(
    r'(^[A-Z]{2}[0-9]{2}\s?[A-Z]{3}$)|(^[A-Z][0-9]{1,3}[A-Z]{3}$)|(^[A-Z]{3}[0-9]{1,3}[A-Z]$)|(^[0-9]{1,4}[A-Z]{1,'
    r'2}$)|(^[0-9]{1,3}[A-Z]{1,3}$)|(^[A-Z]{1,2}[0-9]{1,4}$)|(^[A-Z]{1,3}[0-9]{1,3}$)|(^[A-Z]{1,3}[0-9]{1,'
    r'4}$)|(^[0-9]{3}[DX][0-9]{3}$)')


class Vehicle:

    def __init__(self, auto_pilot: AutoPilot, body_type: BodyType, collision_detection_system: CollisionDetectionSystem,
                 colour: Colour, cruise_control: CruiseControl, current_lane: int, dimensions: dict[str, float],
                 drive_system: DriveSystem, fuel: Fuel, gps: GPS, infotainment_system: InfotainmentSystem,
                 lane_marking_detection_system: LaneMarkingDetectionSystem, left_indicator: bool, logs: list, make: str,
                 mileage: Mileage, model: str, object_detection_system: ObjectDetectionSystem, parts: list[Part],
                 registration_number: str,
                 right_indicator: bool, security_system: SecuritySystem, speed: Speed, steering: Steering,
                 transmission: Transmission,
                 year: int) -> None:
        """
        Constructor for a vehicle object
        :parameter Vehicle self: The vehicle
        :parameter AutoPilot auto_pilot: The vehicles auto pilot system
        :parameter BodyType body_type: The body type of the vehicle
        :parameter CollisionDetectionSystem collision_detection_system: The vehicles collision detection system
        :parameter Colour colour: The colour of the vehicle
        :parameter CruiseControl cruise_control: The vehicles cruise control system
        :parameter int current_lane: The lane the vehicle is in
        :parameter dict[str,float] dimensions: The dimensions of the vehicle
        :parameter DriveSystem drive_system: The vehicles drive system
        :parameter Fuel fuel: The vehicles fuel
        :parameter GPS gps: The vehicles GPS
        :parameter InfotainmentSystem infotainment_system: The vehicles infotainment system
        :parameter LaneMarkingDetectionSystem lane_marking_detection_system: The vehicles lane marking detection system
        :parameter bool left_indicator: Weather the left indicator is on or off
        :parameter list logs: The vehicle logs
        :parameter str make: The make of the vehicle
        :parameter Mileage mileage: The vehicles mileage
        :parameter str model: The model of the vehicle
        :parameter ObjectDetectionSystem object_detection_system: The vehicles object detection system
        :parameter list parts: The parts that make up the vehicle
        :parameter str registration_number: The vehicles registration number
        :parameter bool right_indicator: Weather the right indicator is on or off
        :parameter SecuritySystem security_system: The vehicles security system
        :parameter Speed speed: The vehicles speed
        :parameter Steering steering: The vehicles steering
        :parameter Transmission transmission: The vehicles transmission
        :parameter int year: The year the vehicle was made
        :raises ValueError if any of the parts that make up the vehicle produce an error or any of the vehicles dimensions are negative or the lane your trying to go in doesn't exist or the vehicle has no make or model or is not made
        :returns: None
        """
        # I used the vehicle class as a controller class to hide the logic for my application
        self._auto_pilot = auto_pilot
        self._body_type = body_type
        self._collision_detection_system = collision_detection_system
        self._colour = colour
        self._cruise_control = cruise_control
        # If the object has a negative dimensions throw an error
        if any(value < 0 for value in dimensions.values()):
            raise ValueError("An vehicles dimensions must all positive numbers")
        else:
            self._dimensions = dimensions
        self._drive_system = drive_system
        self._fuel = fuel
        self._gps = gps
        # If the lane is not available throw an error
        if 1 <= current_lane <= self.gps.current_location.number_of_lanes:
            self._current_lane = current_lane
        else:
            raise ValueError("Not able to switch to a lane that doesn't exist")
        self._infotainment_system = infotainment_system
        self._lane_marking_detection_system = lane_marking_detection_system
        self._left_indicator = left_indicator
        if logs:
            self._logs = logs
        else:
            self._logs = []
        # If the vehicle has no make associated with it throw an error
        if is_null_or_white_space(make):
            raise ValueError("A vehicle must have a make")
        else:
            self._make = make
        self._mileage = mileage
        # If the vehicle has no model associated with it throw an error
        if is_null_or_white_space(model):
            raise ValueError("A vehicle must have a model name")
        else:
            self._model = model
        self._object_detection_system = object_detection_system
        if parts:
            self._parts = parts
        else:
            self._parts = []
        # If not valid registration number throw an error
        if is_null_or_white_space(registration_number) or not REGISTRATION_NUMBER_REGEX.search(registration_number):
            raise ValueError("Registration number is not valid")
        else:
            self._registration_number = registration_number
        self._right_indicator = right_indicator
        self._security_system = security_system
        self._speed = speed
        self._stopping_distance = self.calculate_stopping_distance()
        self._steering = steering
        self._transmission = transmission
        # If the vehicle has been made in the future throw an error
        if year > datetime.date.today().year:
            raise ValueError("A vehicle can't be made in the future")
        else:
            self._year = year

    def __str__(self):
        """
        Return the vehicle object as a string
        :parameter Vehicle self: The vehicle object
        :returns: The vehicle object as a string
        """
        left_indicator_status = f'Left Indicator On' if self._left_indicator else "Left Indicator Off"
        right_indicator_status = f'Right Indicator On' if self._right_indicator else "Right Indicator Off"
        return ((f'Vehicle:\nMake: {self.make}\nModel: {self.model}\nDrive System: {self._drive_system.value}\n'
                f'Dimensions:') + "".join(
            f"\n{key.capitalize()}: {value}" for key, value in self._dimensions.items()) + "" +
                f'\nBody Type: {self._body_type.value}\nYear: {self._year}\nRegistration Number: '
                f'{self.registration_number}\nColour:\n{self._colour}\n{self._mileage}\n{self._fuel}\n'
                f'{self._auto_pilot}\n{self._cruise_control}\nGPS:\n{self._gps}\nCollision Detection System:\n'
                f'{self._collision_detection_system}\nObject Detection System:\n'
                f'{self._object_detection_system}Security System:\n{self._security_system}\n'
                f'Lane Marking Detection System:\n{self._lane_marking_detection_system}\n'
                f'Infotainment System:\n{self._infotainment_system}\n'
                + "Parts:" + "".join(f"\n{part}" for part in self._parts) + "" +
                f"\nCurrent Lane: Lane {self._current_lane}\n{self._transmission}\n"
                f"Speed:\n{self._speed}\nSteering:\n{self._steering}\nIndicators:\n{right_indicator_status}\n"
                f"{left_indicator_status}\nLogs:" + "" + "".join(f"\n{log}" for log in self._logs))

    @property
    def auto_pilot(self) -> AutoPilot:
        """
        Get the vehicles autopilot system
        :parameter Vehicle self: The vehicle
        :returns: The vehicles autopilot system
        """
        return self._auto_pilot

    @auto_pilot.setter
    def auto_pilot(self, auto_pilot: AutoPilot) -> None:
        """
        Update the vehicles autopilot system
        :parameter Vehicle self: The vehicle
        :parameter AutoPilot auto_pilot: The vehicles autopilot system
        :returns: None
        """
        self._auto_pilot = auto_pilot

    @property
    def body_type(self) -> BodyType:
        """
        Returns the vehicles body type
        :parameter Vehicle self: The vehicle
        :returns: The body type of the vehicle
        """
        return self._body_type

    @body_type.setter
    def body_type(self, body_type: BodyType) -> None:
        """
        Update the vehicles body type
        :parameter Vehicle self: The vehicle
        :parameter BodyType body_type: The body type of the vehicle
        :returns: None
        """
        self._body_type = body_type

    @property
    def collision_detection_system(self) -> CollisionDetectionSystem:
        """
        Get the vehicles collision detection system
        :parameter Vehicle self: The vehicle
        :returns: The vehicles collision detection system
        """
        return self._collision_detection_system

    @collision_detection_system.setter
    def collision_detection_system(self, collision_detection_system: CollisionDetectionSystem):
        """
        Update the vehicles collision detection system
        :parameter Vehicle self: The vehicle
        :parameter CollisionDetectionSystem collision_detection_system: The vehicles collision detection system
        :returns: None
        """
        self._collision_detection_system = collision_detection_system

    @property
    def colour(self) -> Colour:
        """
        Returns the vehicles colour
        :parameter Vehicle self: The vehicle
        :returns: The colour of the vehicle
        """
        return self._colour

    @colour.setter
    def colour(self, colour: Colour) -> None:
        """
        Update the vehicles colour
        :parameter Vehicle self: The vehicle
        :parameter Colour colour: The colour of the vehicle
        :returns: None
        """
        self._colour = colour

    @property
    def cruise_control(self) -> CruiseControl:
        """
        Get the vehicles cruise control system
        :parameter Vehicle self: The vehicle
        :returns: The vehicles cruise control system
        """
        return self._cruise_control

    @cruise_control.setter
    def cruise_control(self, cruise_control: CruiseControl) -> None:
        """
        Update the vehicles cruise control system
        :parameter Vehicle self: The vehicle
        :parameter CruiseControl cruise_control: The vehicles cruise control system
        :returns: None
        """
        self._cruise_control = cruise_control

    @property
    def current_lane(self):
        """
        Get the lane the vehicle is in
        :parameter Vehicle self: The vehicle
        :returns: The lane the vehicle is in
        """
        return self._current_lane

    @current_lane.setter
    def current_lane(self, current_lane: int) -> None:
        """
        Update the lane the vehicle is in
        :parameter Vehicle self: The vehicle
        :parameter int current_lane: The lane the vehicle is in
        :raises ValueError if the lane is not available
        :returns: None
        """
        # If the lane is not available throw an error
        if 1 <= current_lane <= self.gps.current_location.number_of_lanes:
            self._current_lane = current_lane
        else:
            raise ValueError("Not able to switch to a lane that doesn't exist")

    @property
    def dimensions(self):
        """
        Returns the vehicles dimensions
        :parameter Vehicle self: The vehicle
        :returns: The dimensions of the vehicle
        """
        return self._dimensions

    @dimensions.setter
    def dimensions(self, dimensions: dict[str, float]) -> None:
        """
        Update the vehicles dimensions
        :parameter Vehicle self: The vehicle
        :parameter dict[str,float] dimensions: The dimensions of the vehicle
        :raises ValueError: If any of the dimensions are below 0
        :returns: None
        """
        # If the vehicle has a negative dimensions throw an error
        if any(value < 0 for value in dimensions.values()):
            raise ValueError("An vehicles dimensions must all positive numbers")
        else:
            self._dimensions = dimensions

    @property
    def drive_system(self) -> DriveSystem:
        """
        Get the vehicles drive system
        :parameter Vehicle self: The vehicle
        :returns: The vehicles drive system
        """
        return self._drive_system

    @drive_system.setter
    def drive_system(self, drive_system: DriveSystem) -> None:
        """
        Set the vehicles drive system
        :parameter Vehicle self: The vehicle
        :parameter DriveSystem drive_system: The vehicles drive system
        :returns: None
        """
        self._drive_system = drive_system

    @property
    def fuel(self) -> Fuel:
        """
        Get the vehicles fuel information
        :parameter Vehicle self: The vehicle
        :returns: The vehicles fuel information
        """
        return self._fuel

    @fuel.setter
    def fuel(self, fuel: Fuel) -> None:
        """
        Set the vehicles fuel information
        :parameter Vehicle self: The vehicle
        :parameter Fuel fuel: The vehicles fuel
        :returns: None
        """
        self._fuel = fuel

    @property
    def gps(self) -> GPS:
        """
        Get the vehicles GPS
        :parameter Vehicle self: The vehicle
        :returns: The vehicles GPS
        """
        return self._gps

    @gps.setter
    def gps(self, gps: GPS) -> None:
        """
        Update the vehicles GPS
        :parameter Vehicle self: The vehicle
        :parameter GPS gps: The vehicles GPS
        :returns: None
        """
        self._gps = gps

    @property
    def infotainment_system(self) -> InfotainmentSystem:
        """
        Get the vehicles infotainment system
        :parameter Vehicle self: The vehicle
        :returns: The vehicles infotainment system
        """
        return self._infotainment_system

    @infotainment_system.setter
    def infotainment_system(self, infotainment_system: InfotainmentSystem) -> None:
        """
        Update the vehicles infotainment system
        :parameter Vehicle self: The vehicle
        :parameter InfotainmentSystem infotainment_system: The vehicles infotainment system
        :returns: None
        """
        self._infotainment_system = infotainment_system

    @property
    def lane_marking_detection_system(self) -> LaneMarkingDetectionSystem:
        """
        Get the vehicles lane marking detection system
        :parameter Vehicle self: The vehicle
        :returns: The vehicles lane marking detection system
        """
        return self._lane_marking_detection_system

    @lane_marking_detection_system.setter
    def lane_marking_detection_system(self, lane_marking_detection_system: LaneMarkingDetectionSystem) -> None:
        """
        Update the vehicles lane marking detection system
        :parameter Vehicle self: The vehicle
        :parameter LaneMarkingDetectionSystem lane_marking_detection_system: The vehicles lane marking detection system
        :returns: None
        """
        self._lane_marking_detection_system = lane_marking_detection_system

    @property
    def left_indicator(self) -> bool:
        """
        Get the vehicles left indicator status
        :parameter Vehicle self: The vehicle
        :returns: Weather the left indicator is on or off
        """
        return self._left_indicator

    @left_indicator.setter
    def left_indicator(self, left_indicator: bool) -> None:
        """
        Update the vehicles left indicator status
        :parameter Vehicle self: The vehicle
        :parameter bool left_indicator: Weather the left indicator is on or off
        :returns: None
        """
        self._left_indicator = left_indicator

    @property
    def logs(self) -> list:
        """
        Get the vehicle logs
        :parameter Vehicle self: The vehicle object
        :return: The vehicle logs
        """
        return self._logs

    @logs.setter
    def logs(self, logs: list) -> None:
        """
        Update the vehicle logs
        :parameter Vehicle self: The vehicle object
        :parameter list logs: The vehicle logs
        :returns: None
        """
        if logs:
            self._logs = logs
        else:
            self._logs = []

    @property
    def make(self) -> str:
        """
        Return the vehicle manufacture
        :parameter Vehicle self: The vehicle
        :returns: The make of the vehicle
        """
        return self._make

    @make.setter
    def make(self, make: str) -> None:
        """
        Update the vehicles manufacture
        :parameter Vehicle self: The vehicle
        :parameter str make: The make of the vehicle
        :raises ValueError: If the vehicle has no make
        :returns: None
        """
        # If the vehicle has no make associated with it throw an error
        if is_null_or_white_space(make):
            raise ValueError("A vehicle must have a make")
        else:
            self._make = make

    @property
    def mileage(self) -> Mileage:
        """
        Get the vehicles mileage
        :parameter Vehicle self: The vehicle
        :returns: The vehicles mileage
        """
        return self._mileage

    @mileage.setter
    def mileage(self, mileage: Mileage) -> None:
        """
        Update the vehicles mileage
        :parameter Vehicle self: The vehicle
        :parameter Mileage mileage: The vehicles mileage
        :returns: None
        """
        self._mileage = mileage

    @property
    def model(self) -> str:
        """
        Returns the model name
        :parameter Vehicle self: The vehicle
        :returns: The model of the vehicle
        """
        return self._model

    @model.setter
    def model(self, model: str):
        """
        Update the model name
        :parameter Vehicle self: The vehicle
        :parameter str model: The model of the vehicle
        :raises ValueError: If the vehicle has no model name
        :returns: None
        """
        # If the vehicle has no model associated with it throw an error
        if is_null_or_white_space(model):
            raise ValueError("A vehicle must have a model name")
        else:
            self._model = model

    @property
    def object_detection_system(self):
        """
        Get the vehicles object detection system
        :parameter Vehicle self: The vehicle
        :returns: The vehicles object detection system
        """
        return self._object_detection_system

    @object_detection_system.setter
    def object_detection_system(self, object_detection_system: ObjectDetectionSystem) -> None:
        """
        Update the vehicles object detection system
        :parameter Vehicle self: The vehicle
        :parameter ObjectDetectionSystem object_detection_system: The vehicles object detection system
        :returns: None
        """
        self._object_detection_system = object_detection_system

    @property
    def parts(self) -> list:
        """
        Get a list of the parts a vehicle is made up of
        :parameter Vehicle self: The vehicle
        :return: The parts that make up the vehicle
        """
        return self._parts

    @parts.setter
    def parts(self, parts: list[Part]) -> None:
        """
        Update a list of the parts that a vehicle is made up of
        :parameter Vehicle self: The vehicle
        :parameter list parts: The parts that make up the vehicle
        :returns: None
        """
        if parts:
            self._parts.clear()
            self._parts += parts
        else:
            self._parts = []

    @property
    def registration_number(self) -> str:
        """
        Get the vehicles registration number
        :parameter Vehicle self: The vehicle
        :return: The vehicles registration number
        """
        return self._registration_number

    @registration_number.setter
    def registration_number(self, registration_number: str) -> None:
        """
        Update the vehicles registration number
        :parameter Vehicle self: The vehicle
        :parameter str registration_number: The vehicles registration number
        :returns: None
        """
        # If not valid registration number throw an error
        if is_null_or_white_space(registration_number) or not REGISTRATION_NUMBER_REGEX.search(registration_number):
            raise ValueError("Registration number is not valid")
        else:
            self._registration_number = registration_number

    @property
    def right_indicator(self) -> bool:
        """
        Get the vehicles right indicator status
        :parameter Vehicle self: The vehicle
        :returns: Weather the right indicator is on or off
        """
        return self._right_indicator

    @right_indicator.setter
    def right_indicator(self, right_indicator: bool) -> None:
        """
        Update the vehicles right indicator status
        :parameter Vehicle self: The vehicle
        :parameter bool right_indicator: Weather the right indicator is on or off
        :returns: None
        """
        self._right_indicator = right_indicator

    @property
    def security_system(self) -> SecuritySystem:
        """
        Get the vehicles security system
        :parameter Vehicle self: The vehicle
        :returns: The vehicles security system
        """
        return self._security_system

    @security_system.setter
    def security_system(self, security_system: SecuritySystem) -> None:
        """
        Update the vehicles security system
        :parameter Vehicle self: The vehicle
        :parameter SecuritySystem security_system: The vehicles security system
        :returns: None
        """
        self._security_system = security_system

    @property
    def speed(self) -> Speed:
        """
        Get the vehicles speed
        :parameter Vehicle self: The vehicle
        :returns: The vehicles speed
        """
        return self._speed

    @speed.setter
    def speed(self, speed: Speed) -> None:
        """
        Update the vehicles speed
        :parameter Vehicle self: The vehicle
        :parameter Speed speed: The vehicles speed
        :returns: None
        """
        self._speed = speed

    @property
    def steering(self):
        """
        Get the vehicles steering
        :parameter Vehicle self: The vehicle
        :returns: The vehicles steering
        """
        return self._steering

    @steering.setter
    def steering(self, steering: Steering):
        """
        Update the vehicles steering
        :parameter Vehicle self: The vehicle
        :parameter Steering steering: The vehicles steering
        :returns: None
        """
        self._steering = steering

    @property
    def transmission(self):
        """
        Get the vehicles transmission
        :parameter Vehicle self: The vehicle
        :returns: The vehicles transmission
        """
        return self._transmission

    @transmission.setter
    def transmission(self, transmission: Transmission):
        """
        Updates the vehicles transmission
        :parameter Vehicle self: The vehicle
        :parameter Transmission transmission: The vehicles transmission
        """
        self._transmission = transmission

    @property
    def year(self) -> int:
        """
        Get the year the vehicle was made
        :parameter Vehicle self: The vehicle
        :returns: The year the vehicle was made
        """
        return self._year

    @year.setter
    def year(self, year: int) -> None:
        """
        Update the year the vehicle was made
        :parameter Vehicle self: The vehicle
        :parameter int year: The year the vehicle was made
        :returns: None
        """
        # If the vehicle has been made in the future throw an error
        if year > datetime.date.today().year:
            raise ValueError("A vehicle can't be made in the future")
        else:
            self._year = year

    def accelerate(self):
        """
        Speed up
        :parameter Vehicle self: The vehicle
        :returns: None
        """
        # If autopilot is on, the following distance is greater than the recommended following distance and the
        # current speed is less than the speed limit speed up
        if (self._auto_pilot.enabled and
                self._auto_pilot.following_distance > self._auto_pilot.weather.recommended_following_distance() and
                self._speed.current_speed < self._gps.current_location.speed_limit):
            self._logs.append("Accelerating")
            print("Accelerating when auto pilot is on, the distance to the closest car is greater than the "
                  "recommended following distance and the current speed is less than the speed limit speed up")
            self._speed.accelerate()
        # If cruise control is on, the following distance is greater than the recommended following distance and the
        # current speed is less than the target speed increase the current speed of the vehicle
        elif (self._cruise_control.activated and
              self._speed.current_speed < self._cruise_control.target_speed and
              self._cruise_control.following_distance > self._cruise_control.weather.recommended_following_distance()):
            self._logs.append("Accelerating when cruise control is on, the distance to the closest car is greater "
                              "than the recommended following distance and the current speed is less than the target "
                              "speed speed up")
            self._speed.accelerate()
        # If autopilot and cruise control aren't on speed up
        elif not self._cruise_control.activated and not self._auto_pilot.enabled:
            self._logs.append("Accelerating when cruise control and auto pilot are not on")
            self._speed.accelerate()

    def trigger_alarm(self):
        """
        Triggers the alarm
        :parameter Vehicle self: The vehicle
        :returns: None
        """
        # Trigger the alarm, lock the vehicle and call emergency services
        print("Triggering the alarm, locking the vehicle and alerting the authorities of an attempted brake in")
        self._logs.append("Alarm Triggered")
        self._security_system.alarm_triggered()
        self._security_system.lock_vehicle()
        self._infotainment_system.phone.call_emergency_services()

    def avoid_collision(self):
        """
        Attempts to avoid a collision
        :parameter Vehicle self: The vehicle
        :returns: None
        """
        stopping_distance = self.calculate_stopping_distance()

        # Collision Avoidance Strategy
        # First it attempts to switch to the right lane to avoid the collision,
        # If it can't switch to the right lane it attempts to switch to the left lane
        # Otherwise it performs an emergency stop

        # If the object is in the current lane, is further away than the stopping distance, there is a
        # lane on the right and the right indicator is on switch to the right lane
        if (self.current_lane == self.object_detection_system.objects_detected[0].lane_object_is_in and
                self._object_detection_system.objects_detected[0].distance_to_object > stopping_distance and
                self.current_lane + 1 < self._gps.current_location.number_of_lanes and self.right_indicator):
            print("Avoiding a collision by switching to the right lane")
            self.move_to_right_lane()
        # If the object is in the current lane, is further away than the stopping distance and there is a
        # lane on the left and the left indicator is on switch to the left lane
        elif (self.current_lane == self.object_detection_system.objects_detected[0].lane_object_is_in and
              self._object_detection_system.objects_detected[0].distance_to_object > stopping_distance and
              self.current_lane - 1 > 0 and self.left_indicator):
            print("Avoiding a collision by switching to the left lane")
            self.move_to_left_lane()
        else:
            print("Avoiding a collision by performing an emergency stop")
            self.emergency_stop()
        self._logs.append("Collision Avoided")

    def collision(self):
        """
        In the event of a collision perform an emergency stop and call the emergency services and your emergency contact
        :parameter Vehicle self: The vehicle
        :returns: None
        """
        # Performing an emergency stop and notifying emergency services and your emergency contact after a collision
        print("Performing an emergency stop and notifying emergency services and your emergency contact that you have "
              "been involved in a collision")
        self.emergency_stop()
        self.collision_detection_system.collision_occurred = True
        self._infotainment_system.phone.call_emergency_services()
        self._infotainment_system.phone.call_emergency_contact()
        self._logs.append("Collision Occurred")

    def decelerate(self):
        """
        Slow down
        :parameter Vehicle self: The vehicle
        :returns: None
        """
        self._logs.append("Decelerating")
        print("Slowing down")
        self._speed.decelerate()

    def emergency_stop(self):
        """
        Perform an emergency stop
        :parameter Vehicle self: The vehicle
        :returns: None
        """
        print("Performing an emergency stop")
        self._logs.append("Performing Emergency Stop")
        # Brake until you stop, switch to neutral, engage the handbrake and switch on your hazard lights
        while self._speed.current_speed > 0:
            self.decelerate()
        self._transmission.current_gear = 0
        self._collision_detection_system.emergency_stop()

    def shift_down_a_gear(self):
        """
        Go down a gear
        :parameter Vehicle self: The vehicle
        :return:
        """
        print("Going down a gear")
        self._logs.append("Gear Down")
        self._transmission.gear_down()

    def shift_up_a_gear(self):
        """
        Go up a gear
        :parameter Vehicle self: The vehicle
        :return:
        """
        print("Going up a gear")
        self._logs.append("Gear Up")
        self._transmission.gear_up()

    def move_to_left_lane(self):
        """
        Switch to the lane on your left
        :parameter Vehicle self: The vehicle
        :returns: None
        """
        self._logs.append("Switched to left lane")
        print("Switched to left lane")
        self._current_lane -= 1

    def move_to_right_lane(self):
        """
        Switch to the lane on your right
        :parameter Vehicle self: The vehicle
        :returns: None
        """
        self._logs.append("Switched to right lane")
        print("Switched to right lane")
        self._current_lane += 1

    def park(self):
        """
        Park
        :parameter Vehicle self: The vehicle
        :returns: None
        """
        # Parks the car
        self.stop()
        self._logs.append("Parked")
        print("Parked")

    def reverse_bay_park(self):
        """
        Reverse Bay Park
        :parameter Vehicle self: The vehicle
        :returns: None
        """
        # Reverse bay parking maneuver
        self.stop()
        self.transmission.reverse()
        self.accelerate()
        self.stop()
        self._logs.append("Reverse Bay Parked")
        print("Reverse Bay Parked")

    def stop(self):
        """
        Stop the vehicle by decelerating until your current speed is 0 MPH
        :parameter Vehicle self: The vehicle
        ::returns:
        """
        # Slow down to 0 and switch to neutral
        while self._speed.current_speed > 0:
            self.speed.decelerate()
        self.transmission.neutral()
        self._logs.append("Stopped")
        print("Stopped")

    def start(self):
        """
        Start the vehicle
        :returns:
        """
        # Start the car
        print("Started the vehicle")
        self.transmission.neutral()
        self._speed.current_speed = 0

    def clear_logs(self):
        """
        Clear the vehicle logs
        :parameter Vehicle self: The vehicle
        :returns: None
        """
        self._logs.clear()

    def calculate_stopping_distance(self) -> float:
        """
        Calculate the stopping distance at your current speed
        :parameter Vehicle self: The vehicle
        :returns: The stopping distance at your current speed
        """
        # Stopping Distance = ((First Digit of Speed [in MPH] / 2) x Speed)
        return (int(str(self.speed.current_speed)[0]) / 2) * self.speed.current_speed
