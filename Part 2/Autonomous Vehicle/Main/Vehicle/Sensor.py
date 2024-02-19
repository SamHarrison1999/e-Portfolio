from Main.Utils.Utils import is_null_or_white_space


class Sensor:

    def __init__(self, sensor_type: str) -> None:
        """
        Constructor for a Sensor object
        :parameter Sensor self: A sensor object
        :parameter str sensor_type: The type of sensor
        :raises ValueError: If the sensor has no type
        :returns: None
        """
        # If the sensor has no type throw an error
        if is_null_or_white_space(sensor_type):
            raise ValueError("A sensor must have a type")
        else:
            self.__sensor_type = sensor_type

    def __str__(self) -> str:
        """
        Returns a sensor object as a string
        :parameter Sensor self: A sensor object
        :returns: The sensor object as a string
        """
        return f"Sensor: {self.__sensor_type}"

    @property
    def sensor_type(self) -> str:
        """
        Returns the type of sensor
        :parameter Sensor self: A sensor object
        :returns: The type of sensor
        """
        return self.__sensor_type

    @sensor_type.setter
    def sensor_type(self, sensor_type: str) -> None:
        """
        Set the type of sensor
        :parameter Sensor self: A sensor object
        :parameter str sensor_type: The type of sensor
        :returns: None
        :raises ValueError: If the sensor has no type
        """
        # If the sensor has no type throw an error
        if is_null_or_white_space(sensor_type):
            raise ValueError("A sensor must have a type")
        else:
            self.__sensor_type = sensor_type
