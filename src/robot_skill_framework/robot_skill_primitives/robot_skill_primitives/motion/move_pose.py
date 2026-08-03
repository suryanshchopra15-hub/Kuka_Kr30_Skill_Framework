from robot_skill_primitives.primitive_base import PrimitiveBase


class MovePose(PrimitiveBase):

    def __init__(self, planner):

        super().__init__(planner)

    def execute(
        self,
        x,
        y,
        z,
        qx,
        qy,
        qz,
        qw,
    ):

        return self._planner.move_to_pose(
            x,
            y,
            z,
            qx,
            qy,
            qz,
            qw,
        )