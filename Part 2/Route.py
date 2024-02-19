from collections import deque


class Route:
    def __init__(self, distance: float, duration: float, directions: deque):
        """
        Constructor for the Route Object
        Parameters:
            self (Route): The Route object
            distance (float): The current distance to the destination
            duration (float): The time taken to reach the destination
            directions (deque): The directions to get from your current location to the destination
        Returns:
            None
        """
        # If the distance to the destination is a negative number throw an error
        if distance >= 0:
            self.__distance = distance
        else:
            raise ValueError("The distance to the destination must be more than 0.0 miles away")
        # If the duration to the destination is a negative number throw an error
        if duration >= 0:
            self.__duration = duration
        else:
            raise ValueError("The duration to the destination must more than 0 seconds away")
        # If there are no directions in the direction queue set the directions queue to an empty queue
        if directions:
            self.__directions = directions
        else:
            self.__directions = deque()

    def __str__(self):
        return f"Distance to destination: {self.__distance} Miles\nDuration to destination: {self.__duration} Minuets\nDirections:" + f"".join(f'\n{direction}' for direction in self.__directions)

    @property
    def distance(self):
        """
        Get the current distance to the destination
        Parameters:
            self (Route): The Route object
        Returns:
            self.__distance (float): The current distance to the destination
        """
        return self.__distance

    @distance.setter
    def distance(self, distance):
        """
        Set the current distance to the destination
        Parameters:
            self (Route): The Route object
            distance (float): The current distance to the destination
        Returns:
            None
        """
        self.__distance = distance

    @property
    def duration(self):
        """
        Get the time taken to reach the destination
        Parameters:
            self (Route): The Route object
        Returns:
            self.__duration (float): The time taken to reach the destination
        """
        return self.__duration

    @duration.setter
    def duration(self, duration):
        """
        Set the time taken to reach the destination
        Parameters:
            self (Route): The Route object
            duration (float): The time taken to reach the destination
        Returns:
            None
        """
        self.__duration = duration

    @property
    def directions(self):
        """
        Return the directions to get from your current location to the destination
        Parameters:
            self (Route): The Route object
        Returns:
            self.__directions (deque): The directions to get from your current location to the destination
        """
        return self.__directions

    @directions.setter
    def directions(self, directions: deque):
        """
        Set the directions to get from your current location to the destination
        Parameters:
            self (Route): The Route object
            directions (deque): The directions to get from your current location to the destination
        Returns:
            None
        """
        # If there are no directions in the direction queue set the directions queue to an empty queue
        if directions:
            self.__directions = directions
        else:
            self.__directions = deque()

    def next_direction(self):
        """
        Returns the next direction from the queue
        Parameters:
            self (Route): The Route object
        Returns:
            self.__directions[0]: the next direction from the queue
        """
        # Remove from the first direction from the queue of directions
        self.__directions.popleft()
        return f'The next direction is : {self.__directions[0]}'


def main():
    directions_to_destination = deque()
    directions_to_destination.append("In 500 yards turn left")
    directions_to_destination.append("In 300 yards turn right")
    directions_to_destination.append("In 2 miles you have reached your destination")
    route = Route(10, 10, directions_to_destination)
    print(route)
    print(route.next_direction())


if __name__ == "__main__":
    main()
