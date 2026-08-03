from robot_skill_primitives.primitive_base import PrimitiveBase


class MoveHome(PrimitiveBase):

    def __init__(self, planner):

        super().__init__(planner)

    def execute(self):

        joint_names = [
            "joint_1",
            "joint_2",
            "joint_3",
            "joint_4",
            "joint_5",
            "joint_6",
        ]

        joint_positions = [
            0.0,
            -1.5708,
            1.5708,
            0.0,
            0.0,
            0.0,
        ]

        return self._planner.move_to_joint_positions(
            joint_names,
            joint_positions,
        )