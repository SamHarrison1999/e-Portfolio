import unittest
from collections import deque

from Main.Vehicle.Camera import Camera
from Main.Vehicle.Object import Object
from Main.Vehicle.ObjectDetectionSystem import ObjectDetectionSystem
from Main.Vehicle.Sensor import Sensor


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        # The set-up method is run before each test case is run
        cone_camera = Camera((1920, 1080), deque(["Frame 1", "Frame 2"]), "MP4")
        cone_sensor = Sensor("Cone Sensor")
        cone = Object("Cone", {"length": 5, "width": 5, "height": 10}, 1, 5, 10)
        person_camera = Camera((1920, 1080), deque(["Frame 1"]), "MP4")
        person_sensor = Sensor("Person Sensor")
        person = Object("Person", {"width": 0.5, "height": 2}, 1, 5, 10)
        self._object_detection_system = ObjectDetectionSystem([cone_camera, person_camera],
                                                              [cone_sensor, person_sensor], [cone, person])

    def tearDown(self) -> None:
        self._object_detection_system = None

    def testNoCameras(self):
        """Testing the list of cameras is an empty list if you don't provide a list of cameras """
        with self.subTest("When the list of cameras is none"):
            self._object_detection_system = ObjectDetectionSystem(None, [], [])
            self.assertEqual(self._object_detection_system.cameras, [])
        with self.subTest("When the list of cameras is an empty list"):
            self._object_detection_system = ObjectDetectionSystem([], [], [])
            self.assertEqual(self._object_detection_system.cameras, [])

    def testCamerasGetter(self):
        """Testing the list of cameras is returned when you call the cameras getter"""
        self.assertEqual(str(self._object_detection_system.cameras[0]), "Camera Quality: 1920 x 1080\n"
                                                                        "Frames:\n"
                                                                        "Frame 1\n"
                                                                        "Frame 2\n"
                                                                        "File Name: File.MP4")
        self.assertEqual(str(self._object_detection_system.cameras[1]), "Camera Quality: 1920 x 1080\n"
                                                                        "Frames:\n"
                                                                        "Frame 1\n"
                                                                        "File Name: File.MP4")

    def testCamerasSetter(self):
        """Testing you can update the list of camera by calling the cameras setter"""
        self._object_detection_system.cameras = [Camera((1080, 720), deque(["Frame 1"]), "MP4")]
        self.assertEqual(str(self._object_detection_system.cameras[0]),
                         "Camera Quality: 1080 x 720\n"
                         "Frames:\n"
                         "Frame 1\n"
                         "File Name: File.MP4")

    def testCamerasSetterWithNoCameras(self):
        """Testing the list of cameras is an empty list if you update the list of cameras to none or an empty list"""
        with self.subTest("Setting the list of cameras as none"):
            self._object_detection_system.cameras = None
            self.assertEqual(self._object_detection_system.cameras, [])
        with self.subTest("Setting the list of cameras to an empty list"):
            self._object_detection_system.cameras = []
            self.assertEqual(self._object_detection_system.cameras, [])

    def testNoSensors(self):
        """Testing an empty list is returned when there are no sensors when you call the sensors getter"""
        with self.subTest("When the list of sensors is none"):
            self._object_detection_system = ObjectDetectionSystem([], None, [])
            self.assertEqual(self._object_detection_system.sensors, [])
        with self.subTest("When the list of sensors is an empty list"):
            self._object_detection_system = ObjectDetectionSystem([], [], [])
            self.assertEqual(self._object_detection_system.sensors, [])

    def testSensorsGetter(self):
        """Testing the list of sensors are returned when you call the sensors getter"""
        self.assertEqual(str(self._object_detection_system.sensors[0]),
                         "Sensor: Cone Sensor")
        self.assertEqual(str(self._object_detection_system.sensors[1]),
                         "Sensor: Person Sensor")

    def testSensorsSetter(self):
        """Testing you can update the list of sensors using the sensors setter"""
        self._object_detection_system.sensors = [Sensor("Person Sensor")]
        self.assertEqual(str(self._object_detection_system.sensors[0]),
                         "Sensor: Person Sensor")

    def testSensorsSetterWithNoSensors(self):
        """Testing when there are no sensors"""
        with self.subTest("Empty list of sensors"):
            self._object_detection_system.sensors = []
            self.assertEqual(self._object_detection_system.sensors, [])
        with self.subTest("Sensors list not provided"):
            self._object_detection_system.sensors = None
            self.assertEqual(self._object_detection_system.sensors, [])

    def testNoObjects(self):
        """Testing when there aee no objects detected"""
        with self.subTest("No Objects"):
            self._object_detection_system = ObjectDetectionSystem([], [], None)
            self.assertEqual(self._object_detection_system.objects_detected, [])
        with self.subTest("Empty List Of Objects"):
            self._object_detection_system = ObjectDetectionSystem([], [], [])
            self.assertEqual(self._object_detection_system.objects_detected, [])

    def testObjectsGetter(self):
        """Testing the objects getter returns a list of the objects detected"""
        self.assertEqual(self._object_detection_system.objects_detected[0].name, "Cone")
        self.assertEqual(self._object_detection_system.objects_detected[0].dimensions,
                         {"length": 5, "width": 5, "height": 10})
        self.assertEqual(self._object_detection_system.objects_detected[0].lane_object_is_in, 1)
        self.assertEqual(self._object_detection_system.objects_detected[0].distance_to_object, 5)
        self.assertEqual(self._object_detection_system.objects_detected[0].time_until_impact_with_object, 10)
        self.assertEqual(str(self._object_detection_system.objects_detected[0]),
                         "Object Name: Cone\n"
                         "Object Dimensions:\n"
                         "Length: 5 Meters\n"
                         "Width: 5 Meters\n"
                         "Height: 10 Meters\n"
                         "Object in Lane 1\n"
                         "Distance to object: 5 Meters\n"
                         "Time until impact with object at current speed: 10 Seconds")
        self.assertEqual(self._object_detection_system.objects_detected[1].name, "Person")
        self.assertEqual(self._object_detection_system.objects_detected[1].dimensions,
                         {"width": 0.5, "height": 2})
        self.assertEqual(self._object_detection_system.objects_detected[1].lane_object_is_in, 1)
        self.assertEqual(self._object_detection_system.objects_detected[1].distance_to_object, 5)
        self.assertEqual(self._object_detection_system.objects_detected[1].time_until_impact_with_object, 10)
        self.assertEqual(str(self._object_detection_system.objects_detected[1]),
                         "Object Name: Person\n"
                         "Object Dimensions:\n"
                         "Width: 0.5 Meters\n"
                         "Height: 2 Meters\n"
                         "Object in Lane 1\n"
                         "Distance to object: 5 Meters\n"
                         "Time until impact with object at current speed: 10 Seconds")

    def testObjectsSetter(self):
        """Testing you can update the list of detected objects using the objects setter"""
        self._object_detection_system.objects_detected = [Object("Cone", {"length": 5, "width": 5, "height": 10},
                                                                 1, 5, 10)]
        self.assertEqual(self._object_detection_system.objects_detected[0].name, "Cone")
        self.assertEqual(self._object_detection_system.objects_detected[0].dimensions,
                         {"length": 5, "width": 5, "height": 10})
        self.assertEqual(self._object_detection_system.objects_detected[0].lane_object_is_in, 1)
        self.assertEqual(self._object_detection_system.objects_detected[0].distance_to_object, 5)
        self.assertEqual(self._object_detection_system.objects_detected[0].time_until_impact_with_object, 10)
        self.assertEqual(str(self._object_detection_system.objects_detected[0]), "Object Name: Cone\n"
                                                                                 "Object Dimensions:\n"
                                                                                 "Length: 5 Meters\n"
                                                                                 "Width: 5 Meters\n"
                                                                                 "Height: 10 Meters\n"
                                                                                 "Object in Lane 1\n"
                                                                                 "Distance to object: 5 Meters\n"
                                                                                 "Time until impact with object "
                                                                                 "at current speed: 10 Seconds")

    def testObjectsSetterWithNoObjects(self):
        """Testing the list of objects is an empty list if no objects have been detected"""
        with self.subTest("When no list of objects has been provided"):
            self._object_detection_system.objects_detected = None
            self.assertEqual(self._object_detection_system.objects_detected, [])
        with self.subTest("When the list of objects detected is an empty list"):
            self._object_detection_system.objects_detected = []
            self.assertEqual(self._object_detection_system.objects_detected, [])

    def testNewCamera(self):
        """Testing you can add a camera to the list of cameras"""
        self._object_detection_system.new_camera(Camera((480, 480), deque(["Frame 1"]), "MP4"))
        with self.subTest("Verify Length of list"):
            self.assertEqual(len(self._object_detection_system.cameras), 3)
        with self.subTest("Verify camera in list"):
            self.assertEqual(str(self._object_detection_system.cameras[2]), "Camera Quality: 480 x 480\n"
                                                                            "Frames:\n"
                                                                            "Frame 1\n"
                                                                            "File Name: File.MP4")

    def testNewSensor(self):
        """Testing you can add a sensor to the list of sensors"""
        self._object_detection_system.new_sensor(Sensor("Road Sign Sensor"))
        with self.subTest("Verify Length of list"):
            self.assertEqual(len(self._object_detection_system.sensors), 3)
        with self.subTest("Verify sensor in list"):
            self.assertEqual(str(self._object_detection_system.sensors[2]), "Sensor: Road Sign Sensor")

    def testNewObjectDetected(self):
        """Testing you can add an object to the list of detected objects"""
        self._object_detection_system.new_object(Object("Road Sign", {"height": 2, "width": 0.1}, -1, 0.0, 0.0))
        with self.subTest("Verify Length of list"):
            self.assertEqual(len(self._object_detection_system.objects_detected), 3)
        with self.subTest("Verify camera in list"):
            self.assertEqual(str(self._object_detection_system.objects_detected[2]), "Object Name: Road Sign\n"
                                                                                     "Object Dimensions:\n"
                                                                                     "Height: 2 Meters\n"
                                                                                     "Width: 0.1 Meters\n"
                                                                                     "Object not on road")

    def testCameraRemoved(self):
        """Testing you can remove a camera from the list of cameras"""
        self._object_detection_system.remove_camera(self._object_detection_system.cameras[0])
        with self.subTest("Verify Length of list"):
            self.assertEqual(len(self._object_detection_system.cameras), 1)
        with self.subTest("Verify object in list of objects"):
            self.assertEqual(str(self._object_detection_system.cameras[0]), "Camera Quality: 1920 x 1080\n"
                                                                            "Frames:\n"
                                                                            "Frame 1\n"
                                                                            "File Name: File.MP4")

    def testSensorRemoved(self):
        """Testing you can remove a sensor from the list of sensors"""
        self._object_detection_system.remove_sensor(self._object_detection_system.sensors[0])
        with self.subTest("Verify Length of list"):
            self.assertEqual(len(self._object_detection_system.sensors), 1)
        with self.subTest("Verify object in list of objects"):
            self.assertEqual(str(self._object_detection_system.sensors[0]), "Sensor: Person Sensor")

    def testObjectRemoved(self):
        """Testing you can remove an object from the list of detected objects"""
        self._object_detection_system.remove_object(self._object_detection_system.objects_detected[0])
        with self.subTest("Verify Length of list"):
            self.assertEqual(len(self._object_detection_system.objects_detected), 1)
        with self.subTest("Verify object in list of objects"):
            self.assertEqual(str(self._object_detection_system.objects_detected[0]), "Object Name: Person\n"
                                                                                     "Object Dimensions:\n"
                                                                                     "Width: 0.5 Meters\n"
                                                                                     "Height: 2 Meters\n"
                                                                                     "Object in Lane 1\n"
                                                                                     "Distance to object: 5 Meters\n"
                                                                                     "Time until impact with object "
                                                                                     "at current speed: 10 Seconds")

    def testObjectDetectionSystemObject(self):
        """Testing the object detection system object"""
        self.assertEqual(self._object_detection_system.__str__(), "Cameras:\n"
                                                                  "Camera 1:\n"
                                                                  "Camera Quality: 1920 x 1080\n"
                                                                  "Frames:\n"
                                                                  "Frame 1\n"
                                                                  "Frame 2\n"
                                                                  "File Name: File.MP4\n"
                                                                  "Camera 2:\n"
                                                                  "Camera Quality: 1920 x 1080\n"
                                                                  "Frames:\n"
                                                                  "Frame 1\n"
                                                                  "File Name: File.MP4\n"
                                                                  "Sensors:\n"
                                                                  "Sensor 1:\n"
                                                                  "Sensor: Cone Sensor\n"
                                                                  "Sensor 2:\n"
                                                                  "Sensor: Person Sensor\n"
                                                                  "Objects Detected:\n"
                                                                  "Object 1:\n"
                                                                  "Object Name: Cone\n"
                                                                  "Object Dimensions:\n"
                                                                  "Length: 5 Meters\n"
                                                                  "Width: 5 Meters\n"
                                                                  "Height: 10 Meters\n"
                                                                  "Object in Lane 1\n"
                                                                  "Distance to object: 5 Meters\n"
                                                                  "Time until impact with object at current speed: "
                                                                  "10 Seconds\n"
                                                                  "Object 2:\n"
                                                                  "Object Name: Person\n"
                                                                  "Object Dimensions:\n"
                                                                  "Width: 0.5 Meters\n"
                                                                  "Height: 2 Meters\n"
                                                                  "Object in Lane 1\n"
                                                                  "Distance to object: 5 Meters\n"
                                                                  "Time until impact with object at current speed: "
                                                                  "10 Seconds\n")


if __name__ == '__main__':
    unittest.main()
