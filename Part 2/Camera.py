from collections import deque
from Utils import is_null_or_white_space

# A list of supported file formats
file_formats = ["JPG, PNG, TIFF", "GIF", "MP3", "MP4"]


class Camera:
    def __init__(self, pixels: frozenset[:2], frames: deque, file_format: str):
        """
        Constructor for Camera Object
        Parameters:
            self (Camera): Camera Object
            pixels (frozenset[int]): The quality of the camera in pixels
            frames (deque): A list of frames in the recording / photo
            file_format (str): The file format (E.G. MP4)
        Returns:
            None
        """
        # If pixels not set default values is (0x0)
        if pixels:
            self.__pixels = pixels
        else:
            self.__pixels = frozenset([0, 0])
        # If no frames are in the frames queue set the list of frames to an empty queue
        if frames:
            self.__frames = frames
        else:
            self.__frames = deque()
        # If the file format is blank or not supported throw an error
        if is_null_or_white_space(file_format) or file_format not in file_formats:
            raise ValueError("File format is not supported")
        else:
            self.__file_format = file_format

    def __str__(self):
        """
        Return a Camera object as a string
        Parameters:
            self (Camera): Camera object
        Returns:
            Formatted string of a Camera object
        """
        return f'Camera Quality: {list(self.__pixels)[0]} x {list(self.__pixels)[1]}\nFrames:' + f''.join(
            f"\n{frame}" for frame in self.__frames)

    @property
    def pixels(self):
        """
        Returns the picture quality of the camera in pixels
        Parameters:
            self (Camera): Camera object
        Returns:
             self.__pixels (frozenset[int]): The picture quality of the camera in pixels
        """
        return self.__pixels

    @pixels.setter
    def pixels(self, pixels: frozenset[:2]):
        """
        Set the picture quality of the camera in pixels
        Parameters:
            self (Camera): Camera object
            pixels (frozenset[int]): The picture quality of the camera in pixels
        Returns:
            None
        """
        # If pixels not set default values is (0x0)
        if pixels:
            self.__pixels = pixels
        else:
            self.__pixels = frozenset([0, 0])

    @property
    def frames(self):
        """
        Gets a list of the frames being recorded
        Parameters:
            self (Camera): Camera Object
        Returns:
            self.__frames (list): A list of the frames being recorded
        """
        return self.__frames

    @frames.setter
    def frames(self, frames: deque):
        """
        Sets a list of the frames being recorded
        Parameters:
            self (Camera): Camera object
            frames (list): A list of the frames being recorded
        Returns:
            None
        """
        # If no frames are in the frames queue set the list of frames to an empty queue
        if frames:
            self.__frames = frames
        else:
            self.__frames = deque()

    @property
    def file_format(self):
        """
        Gets the file format
        Parameters:
            self (Camera): Camera Object
        Returns:
            self.__file_format (str): The File Format (E.G. MP4)
        """
        return self.__file_format

    @file_format.setter
    def file_format(self, file_format: str):
        """
        Sets the file format
        Parameters:
            self (Camera): Camera Object
            file_format (str): The File Format (E.G. MP4)
        Returns:
            None
        """
        # If the file format is blank or not supported throw an error
        if is_null_or_white_space(file_format) or file_format not in file_formats:
            raise ValueError("File format is not supported")
        else:
            self.__file_format = file_format

    def record(self):
        """
        Adds the next frame to the frames list
        Parameters:
            self (Camera): Camera Object
        Returns:
            None
        """
        self.__frames.append("Frame " + str(len(self.__frames) + 1))


def main():
    pixels = frozenset([1920, 1080])
    frames = deque()
    frames.append("Frame 1")
    frames.append("Frame 2")
    camera = Camera(pixels, frames, "MP4")
    camera.record()
    print(camera)


if __name__ == "__main__":
    main()
