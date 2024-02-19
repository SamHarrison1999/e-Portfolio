class Colour:
    def __init__(self, cyan: float, magenta: float, yellow: float, black: float):
        """
        Constructor for a Colour Object
        Parameters:
            self (Colour): Colour object
            cyan (float): Value between 0 and 1 representing cyan percentage in the CYMK colour scale
            magenta (float): Value between 0 and 1 representing magenta percentage in the CYMK colour scale
            yellow (float): Value between 0 and 1 representing yellow percentage in the CYMK colour scale
            black (float): Value between 0 and 1 representing black percentage in the CYMK colour scale
        Returns:
            None
        """
        # Colour system used in Painting is CMYK
        # If the value for cyan is between 0 and 1 set the cyan value otherwise throw an error
        if 0 <= cyan <= 1:
            self.__cyan = cyan
        else:
            raise ValueError("Cyan value must be between 0 and 1")
        # If the value for magenta is between 0 and 1 set the magenta value otherwise throw an error
        if 0 <= magenta <= 1:
            self.__magenta = magenta
        else:
            raise ValueError("Magenta value must be between 0 and 1")
        # If the value for yellow is between 0 and 1 set the yellow value otherwise throw an error
        if 0 <= yellow <= 1:
            self.__yellow = yellow
        else:
            raise ValueError("Yellow value must be between 0 and 1")
        # If the value for black is between 0 and 1 set the black value otherwise throw an error
        if 0 <= black <= 1:
            self.__black = black
        else:
            raise ValueError("Black value must be between 0 and 1")

    def __str__(self):
        """
        Print the CMYK, RGB and Hexadecimal values for a colour object
        Parameters:
            self (Colour): Colour object
        Returns:
             Formatted string of a Colour object
        """
        rgb: list = self.cmky_to_rgb()
        return f"cymk({int(self.cyan*100)}%, {int(self.magenta*100)}%, {int(self.yellow*100)}%, {int(self.black*100)}%)\nrgb({rgb[0]}, {rgb[1]}, {rgb[2]})\n" + Colour.rgb_hex_code(rgb[0], rgb[1], rgb[2])

    def cmky_to_rgb(self):
        """
        Convert the colour to the RGB format then display the RGB values and hexadecimal values of the colour
        Parameters:
            self (Colour): Colour object
        Returns:
            A list containing the colour in the RGB format
        """
        # Colour system used in computers is RGB
        red: int = int(255 * (1 - self.__cyan) * (1 - self.__black))
        green: int = int(255 * (1 - self.__magenta) * (1 - self.__black))
        blue: int = int(255 * (1 - self.__yellow) * (1 - self.__black))
        return [red, green, blue]

    @staticmethod
    def rgb_hex_code(red: int, green: int, blue: int):
        """
        Convert RGB colour to hexadecimal
        Parameters:
            red (int): Value between 0 and 255 representing Red value in the RGB colour scale
            green (int): Value between 0 and 255 representing Green value in the RGB colour scale
            blue (int): Value between 0 and 255 representing Blue value in the RGB colour scale
        Returns:
           Formatted hexadecimal string for RGB colour
        """
        return f'#{red:02X}{green:02X}{blue:02X}'

    @property
    def cyan(self):
        """
        Get the cyan value in the CYMK colour scale
        Parameters:
            self (Colour): Colour object
        Returns:
            self.__cyan (float): Value between 0 and 1 representing cyan percentage in the CYMK colour scale
        """
        return self.__cyan

    @cyan.setter
    def cyan(self, cyan: float):
        """
        Set the cyan value in the CYMK colour scale
        Parameters:
            self (Colour): Colour object
            cyan (float): Value between 0 and 1 representing cyan percentage in the CYMK colour scale
        Returns:
            None
        """
        # If the value for cyan is between 0 and 1 set the cyan value otherwise throw an error
        if 0 <= cyan <= 1:
            self.__cyan = cyan
        else:
            raise ValueError("Cyan value must be between 0 and 1")

    @property
    def magenta(self):
        """
        Get the magenta value in the CYMK colour scale
        Parameters:
            self (Colour): Colour object
        Returns:
            self.__magenta (float): Value between 0 and 1 representing magenta percentage in the CYMK colour scale
        """
        return self.__magenta

    @magenta.setter
    def magenta(self, magenta: float):
        """
        Set the magenta value in the CYMK colour scale
        Parameters:
            self (Colour): Colour object
            magenta (float): Value between 0 and 1 representing magenta percentage in the CYMK colour scale
        Returns:
            None
        """
        # If the value for magenta is between 0 and 1 set the magenta value otherwise throw an error
        if 0 <= magenta <= 1:
            self.__magenta = magenta
        else:
            raise ValueError("Magenta value must be between 0 and 1")

    @property
    def yellow(self):
        """
        Get the yellow value in the CYMK colour scale
        Parameters:
            self (Colour): Colour object
        Returns:
            self.__yellow (float): Value between 0 and 1 representing yellow percentage in the CYMK colour scale
        """
        return self.__yellow

    @yellow.setter
    def yellow(self, yellow: float):
        """
        Set the yellow value in the CYMK colour scale
        Parameters:
            self (Colour): Colour object
            yellow (float): Value between 0 and 1 representing yellow percentage in the CYMK colour scale
        Returns:
            None
        """
        # If the value for yellow is between 0 and 1 set the yellow value otherwise throw an error
        if 0 <= yellow <= 1:
            self.__yellow = yellow
        else:
            raise ValueError("Yellow value must be between 0 and 1")

    @property
    def black(self):
        """
        Get the black value in the CYMK colour scale
        Parameters:
            self (Colour): Colour object
        Returns:
            self.__black (float): Value between 0 and 1 representing black percentage in the CYMK colour scale
        """
        return self.__black

    @black.setter
    def black(self, black: float):
        """
        Set the black value in the CYMK colour scale
        Parameters:
            self (Colour): Colour object
            black (float): Value between 0 and 1 representing black percentage in the CYMK colour scale
        Returns:
            None
        """
        # If the value for black is between 0 and 1 set the black value otherwise throw an error
        if 0 <= black <= 1:
            self.__black = black
        else:
            raise ValueError("Black value must be between 0 and 1")


def main():
    colour = Colour(1, 0.2, 0.3, 0.4)
    print(colour)


if __name__ == "__main__":
    main()
