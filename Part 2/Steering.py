class Steering:

    def __init__(self, wheel_rotation: float):
        """
        Constructor for the steering object
        Parameters:
            self (Steering): The steering object
            wheel_rotation (float): The angle the steering wheel has be turned by
        Returns:
            None
        """
        self.__wheel_rotation = wheel_rotation

    def __str__(self):
        """
        Returns the steering object as a string
        Parameters:
            self (Steering): The steering object
        Returns:
            The steering object as a string
        """
        return f'Wheel rotation: {self.__wheel_rotation} degrees'

    @property
    def wheel_rotation(self):
        """
        Get the rotation of the the wheel
        Parameters:
            self (Steering): The steering object
        Returns:
            self.__wheel_rotation (float): The angle the steering wheel has be turned by
        """
        return self.__wheel_rotation

    @wheel_rotation.setter
    def wheel_rotation(self, wheel_rotation):
        """
        Set the rotation of the the wheel
        Parameters:
            self (Steering): The steering object
            wheel_rotation (float): The angle the steering wheel has be turned by
        Returns:
            None
        """
        self.__wheel_rotation = wheel_rotation

    def turn_steering_wheel_left(self, wheel_rotation: float):
        """
        Turn the wheel to the left
        Parameters:
            self (Steering): The steering object
            wheel_rotation (float): The angle the steering wheel has be turned by
        Returns:
            None
        """
        self.__wheel_rotation -= wheel_rotation

    def turn_steer_wheel_right(self, wheel_rotation: float):
        """
        Turn the wheel to the right
        Parameters:
            self (Steering): The steering object
            wheel_rotation (float): The angle the steering wheel has be turned by
        Returns:
            None
        """
        self.__wheel_rotation += wheel_rotation

    def straighten_up(self):
        """
        Straight up the steering
        Parameters:
            self (Steering): The steering object
        Returns:
            None
        """
        self.__wheel_rotation = 0


def main():
    steering = Steering(50)
    print(steering)
    steering.straighten_up()
    print(steering)
    steering.turn_steering_wheel_left(90)
    print(steering)
    steering.turn_steer_wheel_right(180)
    print(steering)


if __name__ == "__main__":
    main()
