# Max colour value for RGB and CMYK
RGB_SCALE = 255
CMYK_SCALE = 100


class Colour:

    def __init__(self, red: int, green: int, blue: int):
        """
        Constructor for a Colour Object
        :parameter Colour self: The colour object
        :parameter int red: Value between 0 and 255 representing red number in the RGB colour scale
        :parameter int green: Value between 0 and 255 representing green number in the RGB colour scale
        :parameter int blue: Value between 0 and 255 representing blue number in the RGB colour scale
        :returns: None
        :raises ValueError: if the RGB values aren't valid
        """
        # If the red value is between 0 and 255 set the red value otherwise throw an error
        if 0 <= red <= RGB_SCALE:
            self._red = red
        else:
            raise ValueError("Red value must be between 0 and 255")
        # If the green value is between 0 and 255 set the green value otherwise throw an error
        if 0 <= green <= RGB_SCALE:
            self._green = green
        else:
            raise ValueError("Green value must be between 0 and 255")
        # If the blue value is between 0 and 255 set the blue value otherwise throw an error
        if 0 <= blue <= RGB_SCALE:
            self._blue = blue
        else:
            raise ValueError("Blue value must be between 0 and 255")

    def __str__(self):
        """
        Returns the colour object as a string
        :parameter Colour self: Colour object
        :returns: The colour object as a string
        """
        return (f"RGB({self._red}, {self._green}, {self._blue})\nCMYK{self.cmyk(self._red, self._green, self._blue)}\n"
                f"{self.hex_code(self._red, self._green, self._blue)}")

    @staticmethod
    def hex_code(red: int, green: int, blue: int):
        """
        Convert RGB colour to hexadecimal
        :parameter int red: Value between 0 and 255 representing Red value in the RGB colour scale
        :parameter int green: Value between 0 and 255 representing Green value in the RGB colour scale
        :parameter int blue: Value between 0 and 255 representing Blue value in the RGB colour scale
        :returns: The hexadecimal value for the RGB colour
        """
        return f'#{red:02X}{green:02X}{blue:02X}'

    @staticmethod
    def cmyk(red, green, blue):
        """
        Convert RGB Colour to CMYK
        :parameter int red: Value between 0 and 255 representing red number in the RGB colour scale
        :parameter int green: Value between 0 and 255 representing green number in the RGB colour scale
        :parameter int blue: Value between 0 and 255 representing blue number in the RGB colour scale
        :returns: The CMYK values for the colour as a tuple
        """
        # Colour system used in Painting is CMYK
        if (red, green, blue) == (0, 0, 0):
            # black
            return 0, 0, 0, CMYK_SCALE

        # rgb values are between 0 and 255
        # cmyk values are between 0 and 100
        cyan = 1 - red / RGB_SCALE
        magenta = 1 - green / RGB_SCALE
        yellow = 1 - blue / RGB_SCALE

        # extract out key value
        min_cmy = min(cyan, magenta, yellow)
        cyan = (cyan - min_cmy) / (1 - min_cmy)
        magenta = (magenta - min_cmy) / (1 - min_cmy)
        yellow = (yellow - min_cmy) / (1 - min_cmy)
        key = min_cmy

        # rescale to the range for the cmyk scale
        return round(cyan * CMYK_SCALE), round(magenta * CMYK_SCALE), round(yellow * CMYK_SCALE), round(
            key * CMYK_SCALE)

    @property
    def red(self):
        """
        Get the red value in the RGB colour scale
        :parameter Colour self: Colour object
        :returns: The red value in the RGB colour scale
        """
        return self._red

    @red.setter
    def red(self, red: int):
        """
        Set the red value in the RGB colour scale
        :parameter Colour self: Colour object
        :parameter int red: Value between 0 and 255 representing red number in the RGB colour scale
        :returns: None
        :raises ValueError: if the red value isn't valid
        """
        # If the red value is between 0 and 255 set the red value otherwise throw an error
        if 0 <= red <= RGB_SCALE:
            self._red = red
        else:
            raise ValueError("Green value must be between 0 and 255")

    @property
    def green(self):
        """
        Get the green value in the RGB colour scale
        :parameter Colour self: Colour object
        :returns: The green value in the RGB colour scale
        """
        return self._green

    @green.setter
    def green(self, green: int):
        """
        Set the green value in the RGB colour scale
        :parameter Colour self: Colour object
        :parameter int green: Value between 0 and 255 representing green number in the RGB colour scale
        :returns: None
        :raises ValueError: if the green value isn't valid
        """
        # If the green value is between 0 and 255 set the green value otherwise throw an error
        if 0 <= green <= RGB_SCALE:
            self._green = green
        else:
            raise ValueError("Green value must be between 0 and 255")

    @property
    def blue(self):
        """
        Get the blue value in the RGB colour scale
        :parameter Colour self: Colour object
        :returns: The blue value in the RGB colour scale
        """
        return self._blue

    @blue.setter
    def blue(self, blue: int):
        """
        Set the blue value in the RGB colour scale
        :parameter Colour self: Colour object
        :parameter int blue: Value between 0 and 255 representing blue number in the RGB colour scale
        :returns: None
        :raises ValueError: if the blue value isn't valid
        """
        # If the blue value is between 0 and 255 set the blue value otherwise throw an error
        if 0 <= blue <= RGB_SCALE:
            self._blue = blue
        else:
            raise ValueError("Blue value must be between 0 and 255")
