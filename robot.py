import pybullet as p

class ROBOT:
    def __init__(self) -> None:
        self.robotId = p.loadURDF("body.urdf")
        self.sensors = {}
        self.motors = {}