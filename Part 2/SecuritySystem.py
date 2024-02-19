class SecuritySystem:
    def __init__(self, alarm_triggered):
        """
        Constructor for the Security System Object
        Parameters:
            self (SecuritySystem): Security System Object
            alarm_triggered (bool): Whether the alarm has been triggered
        Returns:
            None
        """
        self.__alarm_triggered = alarm_triggered

    def __str__(self):
        """
        Returns the security system object as a string
        Parameters:
            self (SecuritySystem): Security System Object
        Returns:
            The security system object as a string
        """
        return f'Alarm Status: {"Alarm Triggered" if self.__alarm_triggered else "Alarm Not Triggered"}'

    @property
    def alarm_triggered(self):
        """
        Checks whether the alarm has been triggered
        Parameters:
            self (SecuritySystem): Security System Object
        Returns:
            self.__alarm_triggered (bool): Whether the alarm has been triggered
        """
        return self.__alarm_triggered

    @alarm_triggered.setter
    def alarm_triggered(self, alarm_triggered):
        """
        Set whether the alarm has been triggered
        Parameters:
            self (SecuritySystem): Security System Object
            alarm_triggered (bool): Whether the alarm has been triggered
        Returns:
            None
        """
        self.__alarm_triggered = alarm_triggered

    def alarm_trigger(self):
        """
        Alarm activated
        Parameters:
            self (SecuritySystem): Security System Object
        Returns:
            None
        """
        self.__alarm_triggered = True

    def disarm_alarm(self):
        """
        Deactivate the alarm
        Parameters:
            self (SecuritySystem): Security System Object
        Returns:
            None
        """
        self.__alarm_triggered = False


def main():
    security_system = SecuritySystem(True)
    security_system.disarm_alarm()
    print(security_system)


if __name__ == "__main__":
    main()
