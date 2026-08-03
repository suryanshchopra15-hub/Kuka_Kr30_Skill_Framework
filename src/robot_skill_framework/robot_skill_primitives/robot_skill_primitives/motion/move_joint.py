from robot_skill_primitives.primitive_base import PrimitiveBase
from robot_skill_primitives.motion.skill_config import get_joint_config


class MoveJoint(PrimitiveBase):
    """Move the robot to one of several predefined joint configurations."""

    def __init__(self, planner):
        super().__init__(planner)

    def execute(self, preset_name: str):
        config = get_joint_config(preset_name)
        if config is None:
            raise ValueError(f"Unknown joint preset: {preset_name}")

        joint_names, joint_positions = config
        return self._planner.move_to_joint_positions(joint_names, joint_positions)
