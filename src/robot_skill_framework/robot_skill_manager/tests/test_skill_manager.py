from robot_skill_manager.skill_manager import SkillManager
from robot_skill_primitives.motion.skill_config import POSE_1


class DummyPlanner:
    def __init__(self):
        self.calls = []

    def move_to_joint_positions(self, joint_names, joint_positions):
        self.calls.append(("joint", joint_names, joint_positions))
        return True

    def move_to_pose(self, x, y, z, qx, qy, qz, qw):
        self.calls.append(("pose", (x, y, z, qx, qy, qz, qw)))
        return True


def test_move_pose_1_routes_to_pose_preset():
    planner = DummyPlanner()
    manager = SkillManager(planner)

    result = manager.execute("move_pose_1")

    assert result is True
    assert planner.calls[0][0] == "pose"
    assert planner.calls[0][1] == POSE_1


def test_move_joint_ready_routes_to_joint_preset():
    planner = DummyPlanner()
    manager = SkillManager(planner)

    result = manager.execute("move_joint_ready")

    assert result is True
    assert planner.calls[0][0] == "joint"
    assert planner.calls[0][1] == [
        "joint_1",
        "joint_2",
        "joint_3",
        "joint_4",
        "joint_5",
        "joint_6",
    ]
