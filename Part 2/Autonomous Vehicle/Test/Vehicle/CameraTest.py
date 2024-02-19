import unittest
from collections import deque

from Main.Vehicle.Camera import Camera


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        # The set-up method is run before each test case
        self._pixels = (1920, 1080)
        self._frames = deque()
        self._frames.append("Frame 1")
        self._frames.append("Frame 2")
        self._camera = Camera(self._pixels, self._frames, "MP4")

    def tearDown(self) -> None:
        self._pixels = None
        self._frames = None
        self._camera = None

    def testValueErrorIsRaisedIfTheFileFormatIsBlank(self):
        """Testing a value error is raised if the file format is empty"""
        with self.assertRaises(ValueError):
            self._camera = Camera(self._pixels, self._frames, "")

    def testValueErrorIsRaisedIfTheFileFormatIsNotSupported(self):
        """Testing a value error is raised if the file format is not supported"""
        with self.assertRaises(ValueError):
            self._camera = Camera(self._pixels, self._frames, "PDF")

    def testValueErrorIsRaisedIfTheCameraQualityIsNegative(self):
        """Testing a value error is raised if the camera quality is a negative number"""
        with self.assertRaises(ValueError):
            self._camera = Camera((-10, -10), self._frames, "MP4")

    def testCameraQualityWhenNoCameraQualityProvided(self):
        """Testing the camera constructor when the camera quality is none"""
        self._camera = Camera(None, self._frames, "MP4")
        self.assertEqual(self._camera.pixels, (0, 0))

    def testFramesBeingRecordedWhenNotProvided(self):
        """Testing the camera constructor when there are no frames being recorded"""
        self._camera = Camera((1920, 1080), None, "MP4")
        self.assertEqual(self._camera.frames, deque())

    def testCameraQualityGetter(self):
        """Testing the camera quality is return when you call the pixels getter"""
        self.assertEqual(self._camera.pixels, (1920, 1080))

    def testCameraQualitySetter(self):
        """Testing if you can update the camera quality by calling the pixels setter"""
        self._camera.pixels = (720, 1080)
        self.assertEqual(self._camera.pixels, (720, 1080))

    def testCameraQualitySetterWithNone(self):
        """Testing update the camera quality to none"""
        self._camera.pixels = None
        self.assertEqual(self._camera.pixels, (0, 0))

    def testValueErrorIsRaisedIfTheCameraQualitySetUsingTheQualitySetterIsNegative(self):
        """Testing a value error is raised if the camera quality set using the pixels setter is a negative number"""
        with self.assertRaises(ValueError):
            self._camera.pixels = (-10, -10)

    def testFramesBeingRecordedGetter(self):
        """Testing if the frames being recorded is returned when you call the frames getter"""
        self.assertEqual(self._camera.frames, deque(["Frame 1", "Frame 2"]))

    def testFramesBeingRecordedSetter(self):
        """Testing if you can update the frames being recorded by calling the frames setter"""
        self._camera.frames = deque(["Frame 1"])
        self.assertEqual(self._camera.frames, deque(["Frame 1"]))

    def testFramesBeingRecordedSetterWithNone(self):
        """Testing what happens when you update the frames being recorded to none"""
        self._camera.frames = None
        self.assertEqual(self._camera.frames, deque())

    def testFileFormatGetter(self):
        """Testing if the file format is returned when you call the file format getter"""
        self.assertEqual(self._camera.file_format, "MP4")

    def testFileFormatSetter(self):
        """Testing if you can update the file format by calling the file format setter"""
        self._camera.file_format = "MP3"
        self.assertEqual(self._camera.file_format, "MP3")

    def testValueErrorIsRaisedIfTheFileFormatSetUsingTheFileFormatSetterIsBlank(self):
        """Testing a value error is raised if the file format set using the file format setter is empty"""
        with self.assertRaises(ValueError):
            self._camera.file_format = ""

    def testValueErrorIsRaisedIfTheFileFormatSetUsingTheFileFormatSetterIsNotSupported(self):
        """Testing a value error is raised if the file format set using the file format setter is not supported"""
        with self.assertRaises(ValueError):
            self._camera.file_format = "PDF"

    def testCameraObject(self):
        """Testing the camera object"""
        with self.subTest("Quality"):
            self.assertEqual(self._camera.pixels, (1920, 1080))
        with self.subTest("Frames"):
            self.assertEqual(self._camera.frames, deque(["Frame 1", "Frame 2"]))
        with self.subTest("File Format"):
            self.assertEqual(self._camera.file_format, "MP4")
        with self.subTest("Camera Object"):
            self.assertEqual(self._camera.__str__(),
                             "Camera Quality: 1920 x 1080\nFrames:\nFrame 1\nFrame 2\nFile Name: File.MP4")

    def testRecord(self):
        """Testing the record function adds a new frame to the list of recorded frames"""
        self._camera.record()
        self.assertEqual(self._camera.frames, deque(["Frame 1", "Frame 2", "Frame 3"]))


if __name__ == '__main__':
    unittest.main()
