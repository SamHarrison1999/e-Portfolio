class Steering:

    def __init__(self, wheel_rotation: float) -> None:
        """
        Constructor for the steering object
        :parameter Steering self: The steering object
        :parameter float wheel_rotation: The angle the steering wheel has been turned by
        :returns: None
        """
        self._wheel_rotation = wheel_rotation

    def __str__(self) -> str:
        """
        Returns the steering object as a string
        :parameter Steering self: The steering object
        :returns: The steering object as a string
        """
        return f'Wheel rotation: {self._wheel_rotation} degrees'

    @property
    def wheel_rotation(self) -> float:
        """
        Get the rotation of the wheel
        :parameter Steering self: The steering object
        :returns: The angle the steering wheel has been turned by
        """
        return self._wheel_rotation

    @wheel_rotation.setter
    def wheel_rotation(self, wheel_rotation: float) -> None:
        """
        Set the rotation of the wheel
        :parameter Steering self: The steering object
        :parameter float wheel_rotation: The angle the steering wheel has been turned by
        :returns: None
        """
        self._wheel_rotation = wheel_rotation

    def turn_steering_wheel_left(self, wheel_rotation: float) -> None:
        """
        Turn the wheel to the left
        :parameter Steering self: The steering object
        :parameter float wheel_rotation: The angle the steering wheel has been turned by
        :returns: None
        """
        # Turn the wheel to the left
        self._wheel_rotation -= wheel_rotation

    def turn_steer_wheel_right(self, wheel_rotation: float) -> None:
        """
        Turn the wheel to the right
        :parameter Steering self: The steering object
        :parameter float wheel_rotation: The angle the steering wheel has been turned by
        :returns: None
        """
        # Turn the wheel to the right
        self._wheel_rotation += wheel_rotation

    def straighten_up(self) -> None:
        """
        Straight up your steering
        :parameter Steering self: The steering object
        :returns: None
        """
        # Straighten up steering
        self._wheel_rotation = 0
