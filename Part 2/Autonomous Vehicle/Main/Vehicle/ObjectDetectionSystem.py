from Main.Vehicle.Camera import Camera
from Main.Vehicle.Object import Object
from Main.Vehicle.Sensor import Sensor


class ObjectDetectionSystem:

    def __init__(self, cameras: list[Camera], sensors: list[Sensor], objects_detected: list[Object]) -> None:
        """
        Constructor for the object detection system
        :parameter ObjectDetectionSystem self: The object detection system
        :parameter cameras: A list of cameras
        :parameter sensors: A list of sensors
        :parameter objects_detected: A list of detected objects
        :returns: None
        """
        # If there are no cameras set the list of camera to an empty list
        if cameras:
            self._cameras = cameras
        else:
            self._cameras = []
        # If there are no sensors set the list of sensors to an empty list
        if sensors:
            self._sensors = sensors
        else:
            self._sensors = []
        # If there are no objects detected set the list of objects detected to an empty list
        if objects_detected:
            self._objects_detected = objects_detected
        else:
            self._objects_detected = []

    def __str__(self) -> str:
        """
        Returns the object detection system object as a string
        :parameter ObjectDetectionSystem self: The object detection system
        :returns: The object detection system object as a string
        """
        return ("Cameras:\n" + "" + f''.join(f"Camera {camera_number + 1}:\n{camera}\n"
                                             for camera_number, camera in enumerate(self._cameras)) +
                "Sensors:\n" + "" + "".join(f"Sensor {sensor_number + 1}:\n{sensor}\n"
                                            for sensor_number, sensor in enumerate(self._sensors)) +
                "Objects Detected:\n" + "" + "".join(
                    f"Object {object_number + 1}:\n{object_detected}\n"
                    for object_number, object_detected in enumerate(self._objects_detected)))

    @property
    def cameras(self) -> list[Camera]:
        """
        Returns a list of all the cameras
        :parameter ObjectDetectionSystem self: The object detection system
        :returns: A list of cameras
        """
        return self._cameras

    @cameras.setter
    def cameras(self, cameras: list[Camera]) -> None:
        """
        Update the list of cameras
        :parameter ObjectDetectionSystem self: The object detection system
        :parameter cameras: A list of cameras
        :returns: None
        """
        # If there are no cameras set the list of camera to an empty list
        if cameras:
            self._cameras = cameras
        else:
            self._cameras = []

    @property
    def sensors(self) -> list[Sensor]:
        """
        Returns a list of all the sensors
        :parameter ObjectDetectionSystem self: The object detection system
        :returns: A list of sensors
        """
        return self._sensors

    @sensors.setter
    def sensors(self, sensors: list[Sensor]) -> None:
        """
        Update the list of sensors
        :parameter ObjectDetectionSystem self: The object detection system
        :parameter sensors: A list of sensors
        :returns: None
        """
        # If there are no sensors set the list of sensors to an empty list
        if sensors:
            self._sensors = sensors
        else:
            self._sensors = []

    @property
    def objects_detected(self) -> list[Object]:
        """
        Get the list of objects detected
        :parameter ObjectDetectionSystem self: The object detection system
        :returns: A list of detected objects
        """
        return self._objects_detected

    @objects_detected.setter
    def objects_detected(self, objects_detected: list[Object]) -> None:
        """
        Update the list of objects detected
        :parameter ObjectDetectionSystem self: The object detection system
        :parameter objects_detected: A list of detected objects
        :returns: None
        """
        # If there are no objects detected set the list of objects detected to an empty list
        if objects_detected:
            self._objects_detected = objects_detected
        else:
            self._objects_detected = []

    def new_camera(self, camera: Camera) -> None:
        """
        Add a new camera to the list of camera
        :parameter camera: The new camera
        :returns: None
        """
        self._cameras.append(camera)

    def new_sensor(self, sensor: Sensor) -> None:
        """
        Add a new sensor to the list of sensors
        :parameter sensor: The new sensor
        :returns: None
        """
        self._sensors.append(sensor)

    def new_object(self, object_detected: Object) -> None:
        """
        Add a new object to the list of detected objects
        :parameter object_detected: The new object
        :returns: None
        """
        self._objects_detected.append(object_detected)

    def remove_camera(self, camera: Camera) -> None:
        """
        Remove a camera from the list of cameras if it exists
        :parameter camera: The camera to be removed
        :returns: None
        """
        # If camera exists remove camera
        if camera in self._cameras:
            self._cameras.remove(camera)

    def remove_sensor(self, sensor: Sensor) -> None:
        """
        Remove a sensor from the list of sensors if it exists
        :parameter sensor: The sensor being removed
        :returns: None
        """
        # If sensor exists remove sensor
        if sensor in self.sensors:
            self._sensors.remove(sensor)

    def remove_object(self, object_detected: Object) -> None:
        """
        Remove the object from the list of detected objects if it exists
        :parameter object_detected: The object to be removed
        :returns: None
        """
        # If object exists remove object
        if object_detected in self._objects_detected:
            self._objects_detected.remove(object_detected)
