import pybullet as p

class WORLD:
    def __init__(self) -> None:
        p.loadURDF("plane.urdf")
        p.loadSDF("world.sdf")
