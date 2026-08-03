from robot_skill_primitives.motion.skill_config import get_joint_config, get_pose_config


def test_joint_presets_are_available():
    assert get_joint_config("home") is not None
    assert get_joint_config("ready") is not None
    assert get_joint_config("park") is not None


def test_pose_presets_are_available():
    pose = get_pose_config("pose_1")
    assert pose is not None
    assert len(pose) == 7
    assert get_pose_config("pose_6") is not None
