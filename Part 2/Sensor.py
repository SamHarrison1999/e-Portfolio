from ObjectDetection import ObjectDetection
from collections import OrderedDict
from Utils import is_null_or_white_space


class Sensor:

    def __init__(self, sensor_type: str, obstacles_detected: list[ObjectDetection]):
        """
        Constructor for a Sensor object
        Parameters:
            self (Sensor): A sensor object
            sensor_type (str): The type of sensor
            obstacles_detected (list[ObjectDetection]): A list of the objects detected
        Returns:
            None
        """
        # If the sensor has no type throw an error
        if is_null_or_white_space(sensor_type):
            raise ValueError("A sensor must have a type")
        else:
            self.__sensor_type = sensor_type
        # If no obstacles have been detected the list of obstacles detected should be an empty list
        if obstacles_detected:
            self.__obstacles_detected = obstacles_detected
        else:
            self.__obstacles_detected = []

    def __str__(self):
        """
        Returns a Sensor object as a string
        Parameters:
            self (Sensor): A sensor object
        Returns:
            The Sensor object as a string
        """
        return f"Sensor: {self.__sensor_type}\n" + f"".join(
            f"{obstacle_detected}" for obstacle_detected in self.__obstacles_detected)

    @property
    def sensor_type(self):
        """
        Returns the type of sensor
        Parameters:
            self (Sensor): A sensor object
        Returns:
            self.__sensor_type (str): The type of sensor
        """
        return self.__sensor_type

    @sensor_type.setter
    def sensor_type(self, sensor_type):
        """
        Set the type of sensor
        Parameters:
            self (Sensor): A sensor object
            sensor_type (str): The type of sensor
        Returns:
            None
        """
        # If the sensor has no type throw an error
        if is_null_or_white_space(sensor_type):
            raise ValueError("A sensor must have a type")
        else:
            self.__sensor_type = sensor_type

    @property
    def obstacles_detected(self):
        """
        Returns a list of the objects detected
        Parameters:
            self (Sensor): A sensor object
        Returns:
            self.__obstacles_detected (list[ObjectDetection]): A list of the objects detected
        """
        return self.__obstacles_detected

    @obstacles_detected.setter
    def obstacles_detected(self, obstacles_detected):
        """
        Set the list of the objects detected
        Parameters:
            self (Sensor): A sensor object
            obstacles_detected (list[ObjectDetection]): A list of the objects detected
        Returns:
            None
        """
        # If no obstacles have been detected the list of obstacles detected should be an empty list
        if obstacles_detected:
            self.__obstacles_detected = obstacles_detected
        else:
            self.__obstacles_detected = []


def main():
    location_of_object = OrderedDict()
    location_of_object["latitude"] = 10
    location_of_object["longitude"] = 50
    size_of_object = OrderedDict()
    size_of_object["length"] = 5
    size_of_object["width"] = 5
    size_of_object["height"] = 10
    object_detection = ObjectDetection("Cone", size_of_object, 5, 10, location_of_object, 5)
    objects = [object_detection]
    sensor = Sensor("Object Sensor", objects)
    print(sensor)


if __name__ == "__main__":
    main()
