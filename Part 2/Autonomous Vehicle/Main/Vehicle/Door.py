from Main.Colour.Colour import Colour
from Main.Vehicle.Part import Part


class Door(Part):

    def __init__(self, part_id: int, name: str, colour: Colour, manufacturer: str,
                 dimensions: dict[str, float], closed: bool, locked: bool) -> None:
        """
        Constructor for a door object
        :parameter Door self: The door object
        :parameter int part_id: The part ID number
        :parameter str name: The name of the part
        :parameter Colour colour: The colour of the part
        :parameter str manufacturer: The parts manufacture
        :parameter dict[str, float] dimensions: The parts dimensions
        :parameter bool closed: If the door is closed
        :parameter bool locked: If the door is locked
        :raises ValueError: if the part has a negative part id no name or manufacture or the dimensions aren't valid
        :returns: None
        """
        # The door class inherits from the part class so uses the parent class constructor.
        # I did this, so I wouldn't have to rewrite the same code over and over again
        # (following the DRY principle).
        super().__init__(part_id, name, colour, manufacturer, dimensions)
        self._closed = closed
        # A door can't be locked unless its shut
        if self._closed and locked:
            self._locked = True
        else:
            self._locked = False

    def __str__(self) -> str:
        """
        Returns a door object as a string
        :parameter Door self: The door object
        :returns: A door object as a string
        """
        door_shut = f'Door Shut' if self._closed else "Door Open"
        door_locked = f'Door Locked' if self._locked else "Door Unlocked"
        return f"{super().__str__()}\n" + f"{door_shut}\n{door_locked}"

    @property
    def closed(self) -> bool:
        """
        Returns if the door is shut or not
        :parameter Door self: The door object
        :returns: If the door is shut
        """
        return self._closed

    @closed.setter
    def closed(self, closed: bool) -> None:
        """
        Update the shut status
        :parameter closed: If the door is shut or not
        :returns: None
        """
        self._closed = closed

    @property
    def locked(self) -> bool:
        """
        Returns if the door is locked or not
        :parameter Door self: The door object
        :returns: If the door is locked
        """
        return self._locked

    @locked.setter
    def locked(self, locked: bool) -> None:
        """
        Update the locked status
        :parameter Door self: The door object
        :parameter locked:  If the door is locked or not
        :returns: none
        """
        # A door can't be locked unless its shut
        if self._closed and locked:
            self._locked = True
        else:
            self._locked = False
