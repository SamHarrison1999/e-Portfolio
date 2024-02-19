from collections import deque


from Vehicle.Camera import Camera
from Vehicle.Contact import Contact
from Vehicle.FuelType import FuelType
from Vehicle.Location import Location
from Vehicle.Message import Message
from Vehicle.Object import Object
from Vehicle.Phone import Phone
from Vehicle.Radio import Radio
from Vehicle.RoadType import RoadType
from Vehicle.Route import Route
from Vehicle.Sensor import Sensor
from Vehicle.TransmissionType import TransmissionType
from Vehicle.Vehicle import *
from People.Person import Driver, Passenger
from Vehicle.Vehicle import Vehicle
from Weather.Weather import Weather


def print_vehicle(vehicle: Vehicle) -> None:
    """
    prints the relevant vehicle information
    :parameter vehicle: The vehicle
    :returns: None
    """
    # If cruise control is on display the target speed
    # If cruise control isn't the target speed information isn't relevant, so it is not displayed
    cruise_control_status = f'Activated\nTarget Speed: {vehicle.cruise_control.target_speed}MPH' if vehicle.cruise_control.activated else 'Deactivated'
    # Display the correct information is autopilot is on or off
    auto_pilot_status = f'Activated' if vehicle.auto_pilot.enabled else 'Deactivated'
    # Display the correct information if the left indicator is on or off
    left_indicator_status = f'Left indicator is on' if vehicle.left_indicator else 'Left indicator is not on'
    # Display the correct information if the right indicator is on or off
    right_indicator_status = f'Right indicator is on' if vehicle.left_indicator else 'Right indicator is not on'
    # If the current gear is -1 the vehicle is in reverse
    # If the current gear is 0 the vehicle is in neutral
    if vehicle.transmission.current_gear == -1:
        current_gear = "Reverse"
    elif vehicle.transmission.current_gear == 0:
        current_gear = "Neutral"
    else:
        current_gear = "Gear " + str(vehicle.transmission.current_gear)
    # Works out how many times the steering wheel has been turned in each direction
    # from 0 degrees using the wheels rotation
    number_of_turns = vehicle.steering.wheel_rotation / 360
    if number_of_turns < 0:
        number_of_turns_string = "Wheel fully turned left " + str(abs(number_of_turns)) + " times"
    else:
        number_of_turns_string = "Wheel fully turned right " + str(number_of_turns) + " times"
    # Display the correct information if the vehicle is locked or unlocked
    locked_status = f'Vehicle locked' if vehicle.security_system.locked else 'Vehicle not locked'
    print(f"""
    Make: {vehicle.make.capitalize()}
    Model: {vehicle.model.capitalize()}
    Year: {vehicle.year}
    Registration Number: {vehicle.registration_number}
    Current Mileage: {vehicle.mileage.current_mileage}
    Transmission: {str(vehicle.transmission.transmission_type.value).capitalize()}
    Fuel Remaining: {vehicle.fuel.fuel_remaining} Liters
    Speed: {vehicle.speed.current_speed}MPH
    Current Gear: {current_gear}
    Steering: {number_of_turns_string}
    Cruise Control: {cruise_control_status}
    Auto Pilot: {auto_pilot_status}
    Destination: {vehicle.gps.destination.road_name}
    Current Lane: Lane {vehicle.current_lane}
    Left Indicator: {left_indicator_status}
    Right Indicator: {right_indicator_status}
    Locked: {locked_status}
    """)


def display_main_menu() -> None:
    """
    Displays the options available from the main menu
    :returns: None
    """
    # Options available from the main menu
    print("""
    --------------------------------------------------------------
    |           Enter create a driver to create a driver         |
    --------------------------------------------------------------
    |       Enter create a passenger to create a passenger       |
    --------------------------------------------------------------
    |         Enter create a vehicle to create a vehicle         |
    --------------------------------------------------------------
    |             Enter exit to exit the application             |
    --------------------------------------------------------------
    """)


def display_vehicle_menu() -> None:
    """
    Displays the options available after creating the vehicle object
    :returns: None
    """
    # Options available from the vehicle menu
    print("""
    ------------------------------------------------------------------------------------
    |                          Enter accelerate to accelerate                          |
    ------------------------------------------------------------------------------------
    |                    Enter trigger alarm to trigger the alarm                      |
    ------------------------------------------------------------------------------------
    |                    Enter avoid collision to avoid a collision                    |
    ------------------------------------------------------------------------------------
    |                         Enter decelerate to decelerate                           |
    ------------------------------------------------------------------------------------
    |                Enter emergency stop to perform an emergency stop                 |
    ------------------------------------------------------------------------------------
    |                       Enter gear down to shift down a gear                       |
    ------------------------------------------------------------------------------------
    |                         Enter gear up to shift up a gear                         |
    ------------------------------------------------------------------------------------
    |                 Enter move to left lane to move to the left lane                 |
    ------------------------------------------------------------------------------------
    |                Enter move to right lane to move to the right lane                |
    ------------------------------------------------------------------------------------
    |                                Enter park to park                                |
    ------------------------------------------------------------------------------------
    |                    Enter reverse bay park to reverse bay park                    |
    ------------------------------------------------------------------------------------
    |                          Enter stop to stop the vehicle                          |
    ------------------------------------------------------------------------------------
    |                         Enter start to start the vehicle                         |
    ------------------------------------------------------------------------------------
    | Enter stopping distance to calculate the stopping distance at your current speed |
    ------------------------------------------------------------------------------------
    |                 Enter collision occurred to simulate a collision                 |
    ------------------------------------------------------------------------------------
    """)


def create_driver() -> Driver:
    """
    Create a driver object
    :returns: The driver
    """
    # Creates a driver object based on the users input
    # The drivers vitals
    number_of_drivers_vitals = int(input("How many different vitals do you wish to enter?\n"))
    driver_vitals = {}
    for i in range(number_of_drivers_vitals):
        keys = input("What is the type of vital? (E.G. Heart Rate)\n")
        values = float(input("What is the value of " + keys + "?\n"))
        driver_vitals[keys] = values
    # Creates the driver object and returns it, so you can edit the driver object
    driver = Driver(input("What is the drivers username?\n"), input("What is the drivers password?\n"),
                    driver_vitals)
    return driver


def create_passenger() -> Passenger:
    """
    Create a passenger object
    :returns: The passenger
    """
    # Creates a passenger object based on the users input
    # The passengers vitals
    number_of_passenger_vitals = int(input("How many different vitals do you wish to enter?\n"))
    passenger_vitals = {}
    for i in range(number_of_passenger_vitals):
        keys = input("What is the type of vital? (E.G. Heart Rate)\n")
        values = float(input("What is the value of " + keys + "?\n"))
        passenger_vitals[keys] = values
    # Creates a driver object and returns it, so you can edit the passenger object
    passenger = Passenger(passenger_vitals)
    return passenger


def create_vehicle() -> Vehicle:
    """
    Create a vehicle object
    :raises ValueError: If the parameters aren't valid
    :returns: The created vehicle
    """
    # Create the weather object used by autopilot and cruise control to work out the recommended following distance
    weather_condition: str = input("What is the current weather condition?\n")
    temperature: int = int(input("What is the current temperature in degrees?\n"))
    current_weather: Weather = Weather(weather_condition, temperature)
    # Create the autopilot object based off the users inputs
    auto_pilot_activated: str = input("Is Auto Pilot on or off?\n")
    distance_to_closest_vehicle: float = float(
        input("How close is the car in front of you in meters?\n"))
    # If autopilot isn't either turned on or off raise a value error
    # which is caught by the try catch statement, so it returns the user to the
    # main menu after displaying the cause of the error that occurred when creating the autopilot object
    # I converted the users input case fold instead of lower case
    # because case fold works with Unicode strings whereas lower doesn't
    if auto_pilot_activated.casefold() == 'on':
        auto_pilot: AutoPilot = AutoPilot(True, current_weather, distance_to_closest_vehicle)
    elif auto_pilot_activated.casefold() == "off":
        auto_pilot: AutoPilot = AutoPilot(False, current_weather, distance_to_closest_vehicle)
    else:
        raise ValueError(auto_pilot_activated + " is not a valid input. Auto pilot can only be either on or off.")
    # Create the collision detection system objet based off the users input
    collision_occurred: str = input("Has a collision occurred? (yes/no)\n")
    handbrake_engaged: str = input("Have you engaged the handbrake? (yes/no)\n")
    hazard_lights: str = input("Are your hazard lights on or off?\n")
    # If the collision occurred input is not either yes or no raise a value error as a collision either has or hasn't
    # happened. The value error is then caught by the try catch statement, so it returns the user to the
    # main menu after displaying the cause of the error that occurred when creating the
    # collision detection system object. I converted the users input case fold instead of lower case
    # because case fold works with Unicode strings whereas lower doesn't
    if collision_occurred.casefold() == "yes":
        collision_status: bool = True
    elif collision_occurred.casefold() == "no":
        collision_status: bool = False
    else:
        raise ValueError(collision_occurred + " is not a valid option. A collision either has happened or it hasn't.")
    # If the handbrake engaged input is not either yes or no raise a value error as your handbrake can only be either
    # on or off. The value error is then caught by the try catch statement, so it returns the user to the
    # main menu after displaying the cause of the error that occurred when creating the
    # collision detection system object. I converted the users input case fold instead of lower case
    # because case fold works with Unicode strings whereas lower doesn't
    if handbrake_engaged.casefold() == "yes":
        handbrake_status: bool = True
    elif handbrake_engaged.casefold() == 'no':
        handbrake_status: bool = False
    else:
        raise ValueError(handbrake_engaged + " is not a valid option. The handbrake can only be on or off.")
    # If the hazards lights input is not either on or off raise a value error as your hazard lights can only be either
    # on or off. The value error is then caught by the try catch statement, so it returns the user to the
    # main menu after displaying the cause of the error that occurred when creating the
    # collision detection system object. I converted the users input case fold instead of lower case
    # because case fold works with Unicode strings whereas lower doesn't
    if hazard_lights.casefold() == "on":
        hazard_lights_status: bool = True
    elif hazard_lights.casefold() == "off":
        hazard_lights_status: bool = False
    else:
        raise ValueError(hazard_lights + " is not a valid option. Your hazard lights can only be on or off.")
    collision_detection_system: CollisionDetectionSystem = CollisionDetectionSystem(collision_status, handbrake_status,
                                                                                    hazard_lights_status)
    cruise_control_activated: str = input("Is Cruise Control on or off?\n")
    # If cruise control is not either on or off raise a value error as cruise control can only be either
    # on or off. The value error is then caught by the try catch statement, so it returns the user to the
    # main menu after displaying the cause of the error that occurred when creating the
    # cruise control object. I converted the users input case fold instead of lower case
    # because case fold works with Unicode strings whereas lower doesn't
    if cruise_control_activated.casefold() == 'on':
        target_speed: int = int(input("What is your target speed?\n"))
        cruise_control: CruiseControl = CruiseControl(True, target_speed, current_weather, distance_to_closest_vehicle)
    elif cruise_control_activated.casefold() == 'off':
        cruise_control: CruiseControl = CruiseControl(False, None, current_weather, distance_to_closest_vehicle)
    else:
        raise ValueError(cruise_control_activated + " is not a valid option. Cruise control can only be on or off.")
    current_lane: int = int(input("What lane are you in?\n"))
    # Input vehicles dimensions
    number_of_vehicle_dimensions: int = int(input("How many vehicle dimensions do you know?\n"))
    vehicle_dimensions: dict[str, float] = {}
    for i in range(number_of_vehicle_dimensions):
        keys: str = input("What is the type of dimension? (E.G. Weight in tonnes)\n")
        values: float = float(input("What is the value of " + keys + "?\n"))
        vehicle_dimensions[keys] = values
    drive_system_prompt = input("What is your vehicles drive system? (E.G. AWD)\n")
    # If the drive system is not support raise a value error.
    # The value error is then caught by the try catch statement, so it returns the user to the
    # main menu after displaying the cause of the error that occurred when creating the
    # drive system object. I converted the users input case fold instead of lower case
    # because case fold works with Unicode strings whereas lower doesn't
    if drive_system_prompt.casefold() == "fwd":
        drive_system = DriveSystem.FWD
    elif drive_system_prompt.casefold() == "rwd":
        drive_system = DriveSystem.RWD
    elif drive_system_prompt.casefold() == "awd":
        drive_system = DriveSystem.AWD
    elif drive_system_prompt.casefold() == "4x4":
        drive_system = DriveSystem.FourByFour
    else:
        raise ValueError(
            drive_system_prompt + " is not a valid option. The drive systems supported are FWD, RWD, AWD and 4x4")
    body_type_prompt = input("What is your vehicles body type? (E.G. Coupe)\n")
    # If the body type is not support raise a value error.
    # The value error is then caught by the try catch statement, so it returns the user to the
    # main menu after displaying the cause of the error that occurred when creating the
    # body type object. I converted the users input case fold instead of lower case
    # because case fold works with Unicode strings whereas lower doesn't
    if body_type_prompt.casefold() == "convertible":
        body_type = BodyType.Convertible
    elif body_type_prompt.casefold() == "coupe":
        body_type = BodyType.Coupe
    elif body_type_prompt.casefold() == "estate":
        body_type = BodyType.Estate
    elif body_type_prompt.casefold() == "hatchback":
        body_type = BodyType.Hatchback
    elif body_type_prompt.casefold() == "mvp":
        body_type = BodyType.MVP
    elif body_type_prompt.casefold() == "pickup":
        body_type = BodyType.Pickup
    elif body_type_prompt.casefold() == "saloon":
        body_type = BodyType.Saloon
    elif body_type_prompt.casefold() == "suv":
        body_type = BodyType.SUV
    else:
        raise ValueError(
            body_type_prompt + "not supported. The Supported body types are Convertible, Coupe, Estate, Hatchback, "
                               "MVP, Pickup, Saloon & SUV")
    fuel_type_prompt = input("What type of fuel does your vehicle run on? (E.G. Diesel)\n")
    # If the fuel type is not support raise a value error.
    # The value error is then caught by the try catch statement, so it returns the user to the
    # main menu after displaying the cause of the error that occurred when creating the
    # fuel type object. I converted the users input case fold instead of lower case
    # because case fold works with Unicode strings whereas lower doesn't
    if fuel_type_prompt.casefold() == 'diesel':
        fuel_type = FuelType.Diesel
    elif fuel_type_prompt.casefold() == 'unleaded':
        fuel_type = FuelType.Unleaded
    elif fuel_type_prompt.casefold() == 'electric':
        fuel_type = FuelType.Electric
    elif fuel_type_prompt.casefold() == 'hybrid':
        fuel_type = FuelType.Hybrid
    else:
        raise ValueError(
            fuel_type_prompt + "is not a valid type of fuel. The supported fuel types are Diesel, Unleaded, Electric "
                               "and Hybrid")
    # Create the fuel object from the users input
    fuel: Fuel = Fuel(fuel_type,
                      int(input("What is the size of the fuel tank in liters?\n")),
                      float(input("How many liters of fuel is left in the tank?\n")))
    # Create the current location object from the users input
    current_location_longitude: float = float(input("What is your current locations longitude?\n"))
    current_location_latitude: float = float(input("What is your current locations latitude?\n"))
    current_location_altitude: float = float(input("What is your current locations altitude?\n"))
    name_of_road_your_on: str = input("What is the name of the road you are on?\n")
    number_of_lanes_on_the_road_your_on: int = int(input("How many lanes does the road have?\n"))
    type_of_road_your_on = road_type_prompt()
    current_traffic_status: str = input("Are you currently in traffic? (yes/no)\n")
    # If the traffic status is not yes or no raise a value error as you can only either be in traffic or not.
    # The value error is then caught by the try catch statement, so it returns the user to the
    # main menu after displaying the cause of the error that occurred when creating the
    # drive system object. I converted the users input case fold instead of lower case
    # because case fold works with Unicode strings whereas lower doesn't
    if current_traffic_status.casefold() == "yes":
        in_traffic: bool = True
    elif current_traffic_status.casefold() == "no":
        in_traffic: bool = False
    else:
        raise ValueError(current_traffic_status + " is not a valid option. You can only be in traffic or not "
                                                  "in traffic")
    speed_limit_on_road_your_on: int = int(input("What is the speed limit on the road your on?\n"))
    current_location: Location = Location(current_location_longitude, current_location_latitude,
                                          current_location_altitude, name_of_road_your_on,
                                          number_of_lanes_on_the_road_your_on, type_of_road_your_on,
                                          in_traffic, speed_limit_on_road_your_on)
    # Create destination object based on the users input
    destinations_longitude: float = float(input("What is the destinations longitude?\n"))
    destinations_latitude: float = float(input("What is the destinations latitude?\n"))
    destinations_altitude: float = float(input("What is the destinations altitude?\n"))
    name_of_road_destination_is_on: str = input("What is the name of the road you want to go to?\n")
    number_of_lanes_for_the_road_the_destination_is_on: int = int(
        input("How many lanes does the road you want to go to have?\n"))
    type_of_road_destination_is_on = road_type_prompt()
    speed_limit_on_the_road_the_destination_is_on: int = int(
        input("What is the speed limit on the road?\n"))
    destination: Location = Location(destinations_longitude, destinations_latitude,
                                     destinations_altitude, name_of_road_destination_is_on,
                                     number_of_lanes_for_the_road_the_destination_is_on,
                                     type_of_road_destination_is_on, in_traffic,
                                     speed_limit_on_the_road_the_destination_is_on)
    number_of_directions_to_reach_the_destination: int = int(
        input("How many directions to reach the destination?\n"))
    directions: deque = deque()
    for i in range(number_of_directions_to_reach_the_destination):
        i = input("What is the direction?\n")
        directions.append(i)
    route: Route = Route(float(input("How many miles away is the destination?\n")),
                         float(input("How long in minuets until you reach the destination?\n")),
                         directions)
    # Create the GPS object based on the users input
    gps: GPS = GPS(current_location, destination, [route])
    # Create an emergency contact object based on the users input
    emergency_contact: Contact = Contact(input("What is your emergency contacts first name?\n"),
                                         input("What is your emergency contacts last name?\n"), input(
            "What is your emergency contacts mobile number? (E.G. +447123456789)\n"))
    # Crete a phone object, contacts list and messages list based on the user input
    # Add the contacts list and messages list to the phone object
    number_of_contacts: int = int(input("How many contacts are in your phone?\n"))
    contacts: list[Contact] = []
    messages: list[Message] = []
    for i in range(number_of_contacts):
        i = Contact(input("What is the contacts first name?\n"),
                    input("What is the contacts last name?\n"),
                    input("What is their contacts mobile number? (E.G. +447123456789)\n"))
        contacts.append(i)
    number_of_messages: int = int(input("How many messages do you have on your phone?\n"))
    for i in range(number_of_messages):
        message_sender: Contact = Contact(
            input("What is the first name of the person who sent the message?\n"),
            input("What is the last name of the person who sent the message?\n"),
            input("What is their contacts mobile number? (E.G. +447123456789)\n"))
        message_receiver: Contact = Contact(
            input("What is the first name of the person who received the message?\n"),
            input("What is the last name of the person who received the message?\n"),
            input("What is their contacts mobile number? (E.G. +447123456789)\n"))
        i = Message(message_sender, message_receiver, input("What was the message sent?\n"))
        messages.append(i)
    phone_connected_to_vehicle: Phone = Phone(input("What is your phone number?\n"), emergency_contact,
                                              contacts, messages)
    # The vehicles radio object
    radio_station_name: str = input("What is the name of the radio station?\n")
    radio_station_type: str = input(
        "Is the radio station an FM radio station or an AM radio station? (Type FM or AM)\n")
    # If radio station type is not supported raise a value error.
    # The value error is then caught by the try catch statement, so it returns the user to the
    # main menu after displaying the cause of the error that occurred when creating the
    # radio object. I converted the users input case fold instead of lower case
    # because case fold works with Unicode strings whereas lower doesn't
    if radio_station_type.casefold() == "fm":
        car_radio: Radio = Radio(radio_station_name,
                                 float(input("What is the radio stations FM number?\n")), None)
    elif radio_station_type.casefold() == "am":
        car_radio: Radio = Radio(radio_station_name, None,
                                 int(input("What is the radio stations AM number?\n")))
    else:
        raise ValueError(radio_station_type + "is not a valid option. The only types of radio stations supported are "
                                              "FM and AM")
    language = input("What is your first language?\n")
    # The infotainment system object created using the users input
    infotainment_system: InfotainmentSystem = InfotainmentSystem(phone_connected_to_vehicle, car_radio,
                                                                 language)
    # The lane marking detection system object created using the users input
    distance_to_left_lane_marking = float(
        input("How close in meters are you to the lane marking on your left?\n"))
    distance_to_right_lane_marking = float(
        input("How close in meters are you to the lane marking on your right?\n"))
    lane_marking_detection_system: LaneMarkingDetectionSystem = LaneMarkingDetectionSystem(
        distance_to_left_lane_marking, distance_to_right_lane_marking)
    left_indicator_status: str = input("Is your left indicator on or off?\n")
    # If indicator isn't either on or off raise a value error.
    # The value error is then caught by the try catch statement, so it returns the user to the
    # main menu after displaying the cause of the error that occurred when creating the
    # indicator object. I converted the users input case fold instead of lower case
    # because case fold works with Unicode strings whereas lower doesn't
    if left_indicator_status.casefold() == "on":
        left_indicator: bool = True
    elif left_indicator_status.casefold() == "off":
        left_indicator: bool = False
    else:
        raise ValueError(left_indicator_status + " is not a valid option. Your indicator can only be on or off")
    logs: list[str] = []
    make: str = input("What make is the vehicle?\n")
    model: str = input("What model " + make + " is it?\n")
    # Create the vehicles colour object based on the users input
    vehicle_colour: Colour = Colour(int(input("What is the vehicles colours red value?\n")),
                                    int(input("What is the vehicles colours green value?\n")),
                                    int(input("What is the vehicles colours blue value?\n")))
    # Create the vehicles mileage object based on the users input
    mileage: Mileage = Mileage(float(input("What is the vehicles miles per gallon?\n")),
                               float(input("What is the vehicles current mileage?\n")))
    number_of_cameras: int = int(input("How many cameras are in the vehicle?\n"))
    # Create the vehicles object detection system using on the cameras, sensors and objects detected created by the user
    cameras: list[Camera] = []
    for i in range(number_of_cameras):
        frames: deque = deque()
        number_of_frames_being_recorded: int = int(input("How long do you want to record for?\n"))
        for frame in range(number_of_frames_being_recorded):
            frames.append("Frame " + str(frame))
        i = Camera((int(input("What is the camera quality in pixels?\n")), int(input())), frames,
                   input("What file format do you want to save the recording as? (E.G. MP4)\n"))
        cameras.append(i)
    number_of_sensors: int = int(input("How many sensors are in the vehicle?\n"))
    sensors: list[Sensor] = []
    for i in range(number_of_sensors):
        i = Sensor(input("What type of sensor is it?\n"))
        sensors.append(i)
    number_of_objects_detected: int = int(input("How many objects have been detected?\n"))
    objects_detected: list[Object] = []
    for i in range(number_of_objects_detected):
        # Object dimensions
        number_of_objects_dimensions: int = int(
            input("How many dimensions of the object do you know?\n"))
        object_dimensions: dict[str, float] = {}
        for x in range(number_of_objects_dimensions):
            keys: str = input("What is the type of dimension? (E.G. Length)\n")
            values: float = float(input("What is the value of " + keys + "?\n"))
            object_dimensions[keys] = values
        i = Object(input("What is the object?\n"), object_dimensions,
                   int(input("What lane is the object in?\n")),
                   float(input("What is the distance in meters to the object?\n")),
                   float(input("How long until you collide with the object at your current speed?\n")))
        objects_detected.append(i)
    object_detection_system: ObjectDetectionSystem = ObjectDetectionSystem(cameras, sensors,
                                                                           objects_detected)
    # Set up the parts for the vehicle based on the users input
    number_of_parts: int = int(input("How many parts do you want to add to the vehicle?\n"))
    parts: list[Part] = []
    for i in range(number_of_parts):
        part_name: str = input("What is the part? (E.G. Suspension)\n")
        part_id: int = int(input("What is the parts ID number?\n"))
        part_manufacture: str = input("Who made the part?\n")
        # Create the colour object for the part based on the users input
        part_colour: Colour = Colour(int(input("What is the " + part_name + "s colours red value?\n")),
                                     int(input(
                                         "What is the " + part_name + "s colours green value?\n")),
                                     int(input("What is the " + part_name + "s colours red value?\n")))
        # Parts dimensions
        number_of_part_dimensions: int = int(input("How many dimensions of the part do you know?\n"))
        part_dimensions: dict[str, float] = {}
        for x in range(number_of_part_dimensions):
            keys: str = input("What is the type of dimension? (E.G. Width)\n")
            values: float = float(input("What is the value of " + keys + "?\n"))
            part_dimensions[keys] = values
        i = Part(part_id, part_name, part_colour, part_manufacture, part_dimensions)
        parts.append(i)
    registration_number: str = input("What is vehicles registration number?\n")
    right_indicator_status: str = input("Is your right indicator on or off?\n")
    # If the indicator isn't either on or off raise a value error.
    # The value error is then caught by the try catch statement, so it returns the user to the
    # main menu after displaying the cause of the error that occurred when creating the
    # indicator object. I converted the users input case fold instead of lower case
    # because case fold works with Unicode strings whereas lower doesn't
    if right_indicator_status.casefold() == "on":
        right_indicator: bool = True
    elif right_indicator_status.casefold() == "off":
        right_indicator: bool = False
    else:
        raise ValueError(right_indicator_status + " is not a valid option. Your indicator can only be on or off")
    alarm_activated_status: str = input("Is the vehicle alarm activated or deactivated?\n")
    # If the alarm isn't either on or off raise a value error.
    # The value error is then caught by the try catch statement, so it returns the user to the
    # main menu after displaying the cause of the error that occurred when creating the
    # security system object. I converted the users input case fold instead of lower case
    # because case fold works with Unicode strings whereas lower doesn't
    if alarm_activated_status.casefold() == "activated":
        alarm_activated: bool = True
    elif alarm_activated_status.casefold() == "deactivated":
        alarm_activated: bool = False
    else:
        raise ValueError(alarm_activated_status + "is not a valid option. "
                                                  "Your alarm can only be activated or deactivated")
    vehicle_locked_status: str = input("Is the vehicle locked or unlocked?\n")
    # If the vehicle isn't either locked or unlocked raise a value error.
    # The value error is then caught by the try catch statement, so it returns the user to the
    # main menu after displaying the cause of the error that occurred when creating the
    # security system object. I converted the users input case fold instead of lower case
    # because case fold works with Unicode strings whereas lower doesn't
    if vehicle_locked_status.casefold() == "locked":
        vehicle_locked: bool = True
    elif vehicle_locked_status.casefold() == "unlocked":
        vehicle_locked: bool = False
    else:
        raise ValueError(vehicle_locked_status + " is not a valid option. Your vehicle can only be locked or unlocked")
    security_system: SecuritySystem = SecuritySystem(alarm_activated, vehicle_locked)
    # Create the vehicles speed object based on the users input
    speed: Speed = Speed(int(input("What is the vehicles top speed?\n")),
                         float(input("What is the vehicles 0 to 60 speed in seconds?\n")),
                         float(input("What is your current speed?\n")))
    # Create the vehicles steering object based on the users input
    steering: Steering = Steering(
        float(input("What is the angle of the steering wheel in degrees? (E.G. 0 is straight) \n")))
    # Create the vehicles transmission object based on the users input
    transmission_colour: Colour = Colour(int(input("What is the transmissions colours red value?\n")),
                                         int(input("What is the transmissions colours green value?\n")),
                                         int(input("What is the transmissions colours blue value?\n")))
    # Transmission dimensions
    number_of_transmission_dimensions: int = int(
        input("How many dimensions of the transmission do you know?\n"))
    transmission_dimensions: dict[str, float] = {}
    for x in range(number_of_transmission_dimensions):
        keys: str = input("What is the type of dimension? (E.G. Weight)\n")
        values: float = float(input("What is the value of " + keys))
        transmission_dimensions[keys] = values
    transmission_type_prompt = input("What is your vehicles transmission type? (E.G. Manual)\n")
    # If the transmission type isn't supported raise a value error.
    # The value error is then caught by the try catch statement, so it returns the user to the
    # main menu after displaying the cause of the error that occurred when creating the
    # transmission type object. I converted the users input case fold instead of lower case
    # because case fold works with Unicode strings whereas lower doesn't
    if transmission_type_prompt.casefold() == 'automatic':
        transmission_type = TransmissionType.AUTOMATIC
    elif transmission_type_prompt.casefold() == 'semi automatic':
        transmission_type = TransmissionType.SEMI_AUTOMATIC
    elif transmission_type_prompt.casefold() == 'manual':
        transmission_type = TransmissionType.MANUAL
    else:
        raise ValueError(
            transmission_type_prompt + "is not a valid transmission type. "
                                       "The supported transmission types are automatic, semi automatic and manual")
    transmission: Transmission = Transmission(1, "Transmission", transmission_colour,
                                              input("Who made the transmission?\n"),
                                              transmission_dimensions, transmission_type, int(input("How many gears "
                                                                                                    "does your "
                                                                                                    "vehicle have? ("
                                                                                                    "enter 1 if its "
                                                                                                    "an automatic)\n")),
                                              int(input("What gear are you currently in?\n")))
    year: int = int(input("When was the vehicle made?\n"))
    # Create the vehicle object based off the users input and return it, so you can perform functions on it
    vehicle: Vehicle = Vehicle(auto_pilot, body_type, collision_detection_system, vehicle_colour,
                               cruise_control, current_lane, vehicle_dimensions, drive_system, fuel,
                               gps, infotainment_system, lane_marking_detection_system, left_indicator,
                               logs, make, mileage, model, object_detection_system, parts,
                               registration_number, right_indicator, security_system, speed, steering,
                               transmission, year)
    return vehicle


def road_type_prompt():
    """
    Checks what type of road you on
    :raises ValueError: If the type of road is not valid
    :returns: The type of road your on
    """
    type_of_road_prompt = input("What type of road is it? (E.G. A Road)\n")
    # If the road type isn't valid raise a value error.
    # The value error is then caught by the try catch statement, so it returns the user to the
    # main menu after displaying the cause of the error that occurred when creating the
    # road type object. I converted the users input case fold instead of lower case
    # because case fold works with Unicode strings whereas lower doesn't
    if type_of_road_prompt.casefold() == 'a road':
        type_of_road_your_on = RoadType.ARoad
    elif type_of_road_prompt.casefold() == 'b road':
        type_of_road_your_on = RoadType.BRoad
    elif type_of_road_prompt.casefold() == 'c road':
        type_of_road_your_on = RoadType.CRoad
    elif type_of_road_prompt.casefold() == 'motorway':
        type_of_road_your_on = RoadType.Motorway
    else:
        raise ValueError(
            type_of_road_prompt + "is not a valid option. The only types of road are a road, b road, c road "
                                  "and motorway")
    return type_of_road_your_on


def main():
    while True:
        # Displays the main menu
        display_main_menu()
        choice: str = input()
        # Redirects the user to the appropriate menu based on the users input
        match choice.casefold():
            case 'create a driver':
                try:
                    driver = create_driver()
                    print(driver)
                except ValueError as exception:
                    # Prints the error then returns you to the menu
                    print(exception)
                    continue
            case 'create a passenger':
                try:
                    passenger = create_passenger()
                    print(passenger)
                except ValueError as exception:
                    # Prints the error then returns you to the menu
                    print(exception)
                    continue
            case 'create a vehicle':
                try:
                    vehicle = create_vehicle()
                    print_vehicle(vehicle)
                    arg = None
                    while arg not in ["no"]:
                        # Display the vehicle menu
                        display_vehicle_menu()
                        choice: str = input()
                        # Perform operations based on the users input
                        match choice.casefold():
                            case 'accelerate':
                                vehicle.accelerate()
                            case 'trigger alarm':
                                vehicle.trigger_alarm()
                            case 'avoid collision':
                                vehicle.avoid_collision()
                            case 'decelerate':
                                vehicle.decelerate()
                            case 'emergency stop':
                                vehicle.emergency_stop()
                            case 'gear down':
                                vehicle.shift_down_a_gear()
                            case 'gear up':
                                vehicle.shift_up_a_gear()
                            case 'move to left lane':
                                vehicle.left_indicator = True
                                vehicle.move_to_left_lane()
                            case 'move to right lane':
                                vehicle.right_indicator = True
                                vehicle.move_to_right_lane()
                            case 'park':
                                vehicle.park()
                            case 'reverse bay park':
                                vehicle.reverse_bay_park()
                            case 'stop':
                                vehicle.stop()
                            case 'start':
                                vehicle.start()
                            case 'stopping distance':
                                print(vehicle.calculate_stopping_distance())
                            case 'collision occurred':
                                vehicle.collision()
                            case _:
                                print(choice + " is not a valid option")
                                continue
                        # Display the vehicle information after performing an action
                        print_vehicle(vehicle)
                        # Allows the user to perform another action on the vehicle
                        arg = input("Would you like to perform another action? (yes/no)\n").casefold()
                except ValueError as ex:
                    print(ex)
                    continue
            case 'exit':
                break
            case _:
                print(choice + " is not a valid option")
                continue


if __name__ == "__main__":
    main()
