from collections import deque


class Route:
    def __init__(self, distance: float, duration: float, directions: deque) -> None:
        """
        Constructor for a route object
        :parameter Route self: The route object
        :parameter float distance: The current distance to the destination
        :parameter float duration: The time taken to reach the destination
        :parameter deque directions: The directions to get from your current location to the destination
        :returns: None
        :raises Value Error: If the distance to the destination or the time until you reach the destination is a negative number
        """
        # If the distance to the destination is a negative number throw an error
        if distance >= 0:
            self._distance = distance
        else:
            raise ValueError("The distance to the destination must be at least 0.0 miles away")
        # If the duration to the destination is a negative number throw an error
        if duration >= 0:
            self._duration = duration
        else:
            raise ValueError("The duration to reach the set destination must be at least 0 seconds away")
        # If there are no directions in the direction queue set the directions queue to an empty queue
        if directions:
            self._directions = directions
        else:
            self._directions = deque()

    def __str__(self) -> str:
        """
        Returns a route object as a string
        :parameter Route self: The route object
        :returns: The route object as a string
        """
        return (f"Distance to destination: {self._distance} Miles\nDuration to destination: "
                f"{self._duration} Minuets\nDirections:") + f"".join(f'\n{direction}' for direction in self._directions)

    @property
    def distance(self) -> float:
        """
        Get the current distance to the destination
        :parameter Route self: The route object
        :returns: The current distance to the destination
        """
        return self._distance

    @distance.setter
    def distance(self, distance: float) -> None:
        """
        Set the current distance to the destination
        :parameter Route self: The route object
        :parameter float distance: The current distance to the destination
        :raises Value Error: If the distance to the destination is a negative number
        :returns: None
        """
        # If the distance to the destination is a negative number throw an error
        if distance >= 0:
            self._distance = distance
        else:
            raise ValueError("The distance to the destination must be at least 0.0 miles away")

    @property
    def duration(self) -> float:
        """
        Get the time taken to reach the destination
        :parameter Route self: The route object
        :returns: The time taken to reach the destination
        """
        return self._duration

    @duration.setter
    def duration(self, duration: float) -> None:
        """
        Set the time taken to reach the destination
        :parameter Route self: The route object
        :parameter float duration: The time taken to reach the destination
        :raises Value Error: If the time until you reach the destination is a negative number
        :returns: None
        """
        # If the duration to the destination is a negative number throw an error
        if duration >= 0:
            self._duration = duration
        else:
            raise ValueError("The duration to reach the set destination must be at least 0 seconds away")

    @property
    def directions(self) -> deque:
        """
        Return the directions to get from your current location to the destination
        :parameter Route self: The route object
        :returns: The directions to get from your current location to the destination
        """
        return self._directions

    @directions.setter
    def directions(self, directions: deque) -> None:
        """
        Set the directions to get from your current location to the destination
        :parameter Route self: The route object
        :parameter deque directions: The directions to get from your current location to the destination
        :returns: None
        """
        # If there are no directions in the direction queue set the directions queue to an empty queue
        if directions:
            self._directions = directions
        else:
            self._directions = deque()

    def next_direction(self) -> str:
        """
        Returns the next direction from the queue
        :parameter Route self: The route object
        :returns: The next direction from the queue
        """
        # Remove from the first direction from the queue of directions
        self._directions.popleft()
        return f'The next direction is: {self._directions[0]}'
