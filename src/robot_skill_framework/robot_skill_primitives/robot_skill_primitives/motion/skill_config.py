from __future__ import annotations

from typing import Dict, Tuple


JOINT_NAMES = [
    "joint_1",
    "joint_2",
    "joint_3",
    "joint_4",
    "joint_5",
    "joint_6",
]


HOME_JOINTS = [0.0, -1.5708, 1.5708, 0.0, 0.0, 0.0]
READY_JOINTS = [0.2, -0.9, 1.2, -0.3, 0.0, 0.0]
FRONT_JOINTS = [0.0, -0.8, 1.1, 0.0, 0.0, 0.0]
LEFT_JOINTS = [-0.6, -1.0, 1.0, 0.2, 0.0, 0.0]
RIGHT_JOINTS = [0.6, -1.0, 1.0, -0.2, 0.0, 0.0]
PARK_JOINTS = [1.0, -1.2, 0.8, 0.4, 0.0, 0.0]

POSE_1 = (1.10, 0.00, 1.30, 0.0, 1.0, 0.0, 0.0)
POSE_2 = (1.00, 0.25, 1.20, 0.0, 1.0, 0.0, 0.0)
POSE_3 = (0.90, -0.25, 1.20, 0.0, 1.0, 0.0, 0.0)
POSE_4 = (1.00, 0.00, 1.40, 0.0, 1.0, 0.0, 0.0)
POSE_5 = (1.20, 0.20, 1.10, 0.0, 1.0, 0.0, 0.0)
POSE_6 = (1.10, -0.20, 1.10, 0.0, 1.0, 0.0, 0.0)


def get_joint_config(name: str) -> Tuple[str, list[float]] | None:
    presets: Dict[str, list[float]] = {
        "home": HOME_JOINTS,
        "ready": READY_JOINTS,
        "front": FRONT_JOINTS,
        "left": LEFT_JOINTS,
        "right": RIGHT_JOINTS,
        "park": PARK_JOINTS,
    }

    if name not in presets:
        return None

    return JOINT_NAMES, list(presets[name])


def get_pose_config(name: str) -> Tuple[float, float, float, float, float, float, float] | None:
    presets = {
        "pose_1": POSE_1,
        "pose_2": POSE_2,
        "pose_3": POSE_3,
        "pose_4": POSE_4,
        "pose_5": POSE_5,
        "pose_6": POSE_6,
    }

    return presets.get(name)
