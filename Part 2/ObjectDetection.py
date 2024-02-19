from collections import OrderedDict

from Collision import Collision
from Utils import is_null_or_white_space


class ObjectDetection:

    def __init__(self, object_type: str, object_size: OrderedDict[str, float], distance_to_object: float,
                 time_until_impact_with_object: float, location_of_object: OrderedDict[str, float],
                 lane_object_is_in: int, collision: Collision):
        """
        Constructor for the Object Detection Object
        Parameters:
            self (ObjectDetection): The Object Detection Object
            object_type (str): The type of object (E.G. Cone)
            object_size (OrderedDict[str, float]): The size of the object
            distance_to_object (float): The distance to the object
            time_until_impact_with_object (float):  The time until collision with the object at current speed
            location_of_object (OrderedDict[str, float]): The location of the object
            lane_object_is_in (int): The lane the object is in
            collision (Collision): The collision object
        Returns:
            None
        """
        # If the object has no type associated with it throw an error
        if is_null_or_white_space(object_type):
            raise ValueError("A detected object must have a type associated with it")
        else:
            self.__object_type = object_type
        # If the object has a negative size throw an error
        if object_size["length"] > 0 and object_size["width"] > 0 and object_size["height"] > 0:
            self.__object_size = object_size
        else:
            raise ValueError("An Objects Length, Width and Height must be a positive number")
        # If the object is closer than 0 meters from the vehicle throw an error
        if distance_to_object >= 0:
            self.__distance_to_object = distance_to_object
        else:
            raise ValueError("Distance to the object must be at least 0 meters")
        # If the object is closer than 0 seconds away from the vehicle throw an error
        if time_until_impact_with_object >= 0:
            self.__time_until_impact_with_object = time_until_impact_with_object
        else:
            raise ValueError("The time until impact with the object must be at least 0 seconds")
        # If the location of the object isn't valid throw an error
        if -90 <= location_of_object['latitude'] <= 90 and -180 <= location_of_object['longitude'] <= 180 and len(
                location_of_object) == 2:
            self.__location_of_object = location_of_object
        else:
            raise ValueError("The locations longitude has to be between -180 and 180 and the location latitude has tp be between -90 and 90")
        # If the object is on the road set the lane the object is in
        if lane_object_is_in > 0:
            self.__lane_object_is_in = lane_object_is_in
        else:
            self.__lane_object_is_in = "The object is not on the road"
        self.__collision = collision

    def __str__(self):
        return f'Object Detected:\nObject Type: {self.__object_type}\nObject Size:' + f"".join(
            f"\n{key.capitalize()}: {value}" for key, value in
            self.object_size.items()) + f"\nDistance to Object: {self.__distance_to_object} Meters\nTime until collision with object at current speed: {self.__time_until_impact_with_object} seconds\nLocation of Object:" + f"".join(
            f"\n{key.capitalize()}: {value}" for key, value in
            self.__location_of_object.items()) + f"\nLane object is in: Lane {self.__lane_object_is_in}\n{self.__collision}"

    @property
    def object_type(self):
        """
        Returns the type of object
        Parameters:
            self (ObjectDetection): The Object Detection Object
        Returns:
            self.__object_type (str): The type of object (E.G. Cone)
        """
        return self.__object_type

    @object_type.setter
    def object_type(self, object_type: str):
        """
        Set the type of object
        Parameters:
            self (ObjectDetection): The Object Detection Object
            object_type (str): The type of object (E.G. Cone)
        Returns:
            None
        """
        # If the object has no type associated with it throw an error
        if is_null_or_white_space(object_type):
            raise ValueError("A detected object must have a type associated with it")
        else:
            self.__object_type = object_type

    @property
    def object_size(self):
        """
        Returns the size of object
        Parameters:
            self (ObjectDetection): The Object Detection Object
        Returns:
            self.__object_size (OrderedDict[str, float]): The size of the object
        """
        return self.__object_size

    @object_size.setter
    def object_size(self, object_size: OrderedDict[str, float]):
        """
        Set the size of object
        Parameters:
            self (ObjectDetection): The Object Detection Object
            object_size (OrderedDict[str, float]): The size of the object
        Returns:
            None
        """
        # If the object has a negative size throw an error
        if object_size["length"] > 0 and object_size["width"] > 0 and object_size["height"] > 0:
            self.__object_size = object_size
        else:
            raise ValueError("An Objects Length, Width and Height must be a positive number")

    @property
    def distance_to_object(self):
        """
        Returns the distance to the object
        Parameters:
            self (ObjectDetection): The Object Detection Object
        Returns:
            self.__distance_to_object (float): The distance to the object
        """
        return self.__distance_to_object

    @distance_to_object.setter
    def distance_to_object(self, distance_to_object: float):
        """
        Set the distance to the object
        Parameters:
            self (ObjectDetection): The Object Detection Object
            distance_to_object (float): The distance to the object
        Returns:
            None
        """
        # If the object is closer than 0 meters from the vehicle throw an error
        if distance_to_object >= 0:
            self.__distance_to_object = distance_to_object
        else:
            raise ValueError("Distance to the object must be at least 0 meters")

    @property
    def time_until_impact_with_object(self):
        """
        Returns the time until collision with the object at current speed
        Parameters:
            self (ObjectDetection): The Object Detection Object
        Returns:
            self.__time_until_impact_with_object (float):  The time until collision with the object at current speed
        """
        return self.__time_until_impact_with_object

    @time_until_impact_with_object.setter
    def time_until_impact_with_object(self, time_until_impact_with_object: float):
        """
        Set the time until collision with the object at current speed
        Parameters:
            self (ObjectDetection): The Object Detection Object
            time_until_impact_with_object (float):  The time until collision with the object at current speed
        Returns:
            None
        """
        # If the object is closer than 0 seconds away from the vehicle throw an error
        if time_until_impact_with_object >= 0:
            self.__time_until_impact_with_object = time_until_impact_with_object
        else:
            raise ValueError("The time until impact with the object must be at least 0 seconds")

    @property
    def location_of_object(self):
        """
        Returns the location of the object
        Parameters:
            self (ObjectDetection): The Object Detection Object
        Returns:
            self.__location_of_object (OrderedDict[str, float]): The location of the object
        """
        return self.__location_of_object

    @location_of_object.setter
    def location_of_object(self, location_of_object: OrderedDict[str, float]):
        """
        Set the location of the object
        Parameters:
            self (ObjectDetection): The Object Detection Object
            location_of_object (OrderedDict[str, float]): The location of the object
        Returns:
            None
        """
        # If the location of the object isn't valid throw an error
        if -90 <= location_of_object['latitude'] <= 90 and -180 <= location_of_object['longitude'] <= 180 and len(
                location_of_object) == 2:
            self.__location_of_object = location_of_object
        else:
            raise ValueError(
                "The locations longitude has to be between -180 and 180 and the location latitude has tp be between -90 and 90")

    @property
    def lane_object_is_in(self):
        """
        Returns the lane the object is in
        Parameters:
            self (ObjectDetection): The Object Detection Object
        Returns:
            self.__lane_object_is_in (int): The lane the object is in
        """
        return self.__lane_object_is_in

    @lane_object_is_in.setter
    def lane_object_is_in(self, lane_object_is_in: int):
        """
        Set the lane the object is in
        Parameters:
            self (ObjectDetection): The Object Detection Object
            lane_object_is_in (int): The lane the object is in
        Returns:
            None
        """
        # If the object is on the road set the lane the object is in
        if lane_object_is_in > 0:
            self.__lane_object_is_in = lane_object_is_in
        else:
            self.__lane_object_is_in = "The object is not on the road"

    @property
    def collision(self):
        return self.__collision

    @collision.setter
    def collision(self, collision):
        self.__collision = collision


def main():
    location_of_object = OrderedDict()
    location_of_object["latitude"] = 10
    location_of_object["longitude"] = 50
    size_of_object = OrderedDict()
    size_of_object["length"] = 5
    size_of_object["width"] = 5
    size_of_object["height"] = 10
    collision_detection = Collision(False, False, False)
    object_detection = ObjectDetection("Cone", size_of_object, 5, 10, location_of_object, 5, collision_detection)
    print(object_detection)


if __name__ == "__main__":
    main()
