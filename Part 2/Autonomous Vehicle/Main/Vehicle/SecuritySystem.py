class SecuritySystem:

    def __init__(self, armed: bool, locked: bool) -> None:
        """
        Constructor for the security system
        :parameter SecuritySystem self: The security system
        :parameter armed: If the security system is activated
        :parameter locked: If the vehicle is locked
        """
        # If the alarm status is none the alarm is not activated
        if armed is None:
            self._armed = False
        else:
            self._armed = armed
        # If the locked status is none the vehicle is not locked
        if locked is None:
            self._locked = False
        else:
            self._locked = locked
        self._triggered = False

    def __str__(self) -> str:
        """
        Returns the security system object as a string
        Parameters:
            self (SecuritySystem): Security System Object
        Returns:
            The security system object as a string
        """
        alarm_status = f'Alarm Status: {"Alarm Activated" if self._armed else "Alarm Not Activate"}'
        locked_status = f'{"Vehicle locked" if self._locked else "Vehicle Unlocked"}'
        triggered_status = f'{"Alarm Triggered" if self._triggered else "Alarm Not Triggered"}'
        return f'{alarm_status}\n{locked_status}\n{triggered_status}'

    @property
    def armed(self) -> bool:
        """
        Checks the security system status (activated or deactivated)
        :parameter SecuritySystem self: The security system
        :return: If the security system is activated
        """
        return self._armed

    @armed.setter
    def armed(self, armed: bool) -> None:
        """
        Update the security alarm status
        :parameter SecuritySystem self: The security system
        :parameter armed: If the security system is activated
        :returns: None
        """
        # If the alarm status is none the alarm is not activated
        if armed is None:
            self._armed = False
        else:
            self._armed = armed

    @property
    def locked(self) -> bool:
        """
        Checks if the vehicle is locked or unlocked
        :parameter SecuritySystem self: The security system
        :returns: If the vehicle is locked or unlocked
        """
        return self._locked

    @locked.setter
    def locked(self, locked: bool) -> None:
        """
        Update the locked status
        :parameter SecuritySystem self: The security system
        :parameter locked: If the vehicle is locked or unlocked
        :returns: None
        """
        # If the locked status is none the vehicle is not locked
        if locked is None:
            self._locked = False
        else:
            self._locked = locked

    @property
    def triggered(self) -> bool:
        """
        Checks whether the alarm has been triggered
        :parameter SecuritySystem self: The security system
        :returns: Whether the alarm has been triggered
        """
        return self._triggered

    @triggered.setter
    def triggered(self, alarm_triggered: bool) -> None:
        """
        Set whether the alarm has been triggered
        :parameter SecuritySystem self: The security system
        :parameter bool alarm_triggered: Whether the alarm has been triggered
        :returns: None
        """
        self._triggered = alarm_triggered

    def arm_security_system(self) -> None:
        """
        Activates the security system
        :parameter SecuritySystem self: The security system
        :returns: None
        """
        # Only activates if the security system if it is not already activated
        if not self._armed:
            self._armed = True

    def disarm_security_system(self) -> None:
        """
        Deactivates the security system
        :parameter SecuritySystem self: The security system
        :returns: None
        """
        # Only deactivates if the security system if its activated
        if self._armed:
            self._armed = False

    def lock_vehicle(self) -> None:
        """
        Locks the vehicle
        :parameter SecuritySystem self: The security system
        :returns: None
        """
        # Only locks the vehicle if it is not already locked
        if not self._locked:
            self._locked = True

    def unlock_vehicle(self) -> None:
        """
        Unlocks the vehicle
        :parameter SecuritySystem self: The security system
        :returns: None
        """
        # Only unlocks the vehicle if its locked
        if self._locked:
            self._locked = False

    def alarm_triggered(self):
        """
        Lock the vehicle after the alarm has been triggered
        :parameter SecuritySystem self: The security system
        :return: None
        """
        # Alarm can't be triggered if it has not been activated
        if self._armed:
            # Only trigger alarm if it has not already triggered
            if not self._triggered:
                self._triggered = True
            # Lock vehicle if it is not locked
            if not self.locked:
                self._locked = True
