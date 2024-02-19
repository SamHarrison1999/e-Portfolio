from collections import deque
from Main.Utils.Utils import is_null_or_white_space

# A list of supported file formats
file_formats = frozenset(["JPG", "PNG", "TIFF", "GIF", "MP3", "MP4"])


class Camera:
    def __init__(self, pixels: tuple[int, ...:2], frames: deque, file_format: str) -> None:
        """
        Constructor for the camera object
        :parameter Camera self: The camera object
        :parameter tuple[int] pixels: The quality of the camera in pixels
        :parameter deque frames: A list of frames in the recording / photo
        :parameter str file_format: The file format (E.G. MP4)
        :raises ValueError: If the file format is empty or not supported or the pixel quality is a negative number
        :returns: None
        """
        # If camera quality is not set default values is (0x0)
        # If the pixels are negative raise a value error
        # I used a tuple instead of a list because tuples are more memory efficient than the lists
        if pixels:
            if pixels[0] < 0 or pixels[1] < 0:
                raise ValueError("The camera quality must be a positive number")
            self._pixels = pixels
        else:
            self._pixels = (0, 0)
        # If there are no frames are in the frames queue set the list of frames to an empty queue
        if frames:
            self._frames = frames
        else:
            self._frames = deque()
        # If the file format is blank or not supported throw an error
        if is_null_or_white_space(file_format) or file_format not in file_formats:
            raise ValueError("File format is not supported")
        else:
            self._file_format = file_format

    def __str__(self) -> str:
        """
        Returns the camera object as a string
        :parameter Camera self: The camera object
        :returns: The camera object as a string
        """
        return f'Camera Quality: {self._pixels[0]} x {self._pixels[1]}\nFrames:' + f''.join(
            f"\n{frame}" for frame in self._frames) + f'\nFile Name: File.{self._file_format}'

    @property
    def pixels(self) -> tuple:
        """
        Returns the picture quality of the camera in pixels
        :parameter Camera self: The camera object
        :returns: The picture quality of the camera in pixels
        """
        return self._pixels

    @pixels.setter
    def pixels(self, pixels: tuple[int, ...:2]) -> None:
        """
        Set the picture quality of the camera in pixels
        :parameter Camera self: The camera object
        :parameter tuple pixels: The picture quality of the camera in pixels
        :returns: None
        """
        # If the cameras quality is not set the default values is (0x0)
        # If the pixels are negative raise a value error
        # I used a tuple instead of a list because tuples are more memory efficient than the lists
        if pixels:
            if pixels[0] < 0 or pixels[1] < 0:
                raise ValueError("The camera quality must be a positive number")
            self._pixels = pixels
        else:
            self._pixels = (0, 0)

    @property
    def frames(self) -> deque:
        """
        Gets a list of the frames being recorded
        :parameter Camera self: The camera object
        :returns: A list of the frames being recorded
        """
        return self._frames

    @frames.setter
    def frames(self, frames: deque) -> None:
        """
        Sets a list of the frames being recorded
        :parameter Camera self: The camera object
        :parameter deque frames: A list of the frames being recorded
        :returns: None
        """
        # If there are no frames in the frames queue set the list of frames to an empty queue
        if frames:
            self._frames = frames
        else:
            self._frames = deque()

    @property
    def file_format(self) -> str:
        """
        Gets the file format
        :parameter Camera self: The camera object
        :returns: The File Format (E.G. MP4)
        """
        return self._file_format

    @file_format.setter
    def file_format(self, file_format: str) -> None:
        """
        Sets the file format
        :parameter Camera self: The camera object
        :parameter str file_format: The File Format (E.G. MP4)
        :raises ValueError: If the file format is empty or not supported
        :returns: None
        """
        # If the file format is blank or not supported throw an error
        if is_null_or_white_space(file_format) or file_format not in file_formats:
            raise ValueError("File format is not supported")
        else:
            self._file_format = file_format

    def record(self) -> None:
        """
        Adds the next frame to the frames list
        :parameter Camera self: The camera object
        :returns: None
        """
        self._frames.append("Frame " + str(len(self._frames) + 1))
