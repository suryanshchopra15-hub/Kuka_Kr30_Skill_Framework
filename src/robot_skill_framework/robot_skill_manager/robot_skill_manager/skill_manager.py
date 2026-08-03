from robot_skill_primitives.motion.move_home import MoveHome
from robot_skill_primitives.motion.move_joint import MoveJoint
from robot_skill_primitives.motion.move_pose import MovePose


class SkillManager:
    """Routes a task request to the appropriate motion primitive."""

    def __init__(self, planner):
        self._planner = planner
        self._primitives = {
            "move_home": MoveHome(planner),
            "move_joint": MoveJoint(planner),
            "move_pose": MovePose(planner),
        }

    def execute(self, task_name: str, **kwargs):
        if task_name == "move_home":
            return self._primitives["move_home"].execute()

        if task_name.startswith("move_joint"):
            preset = self._extract_preset(task_name, "move_joint", default="home")
            return self._primitives["move_joint"].execute(preset)

        if task_name.startswith("move_pose"):
            preset = self._extract_preset(task_name, "move_pose", default="pose_1")
            pose = self._get_pose_config(preset)
            if pose is None:
                raise ValueError(f"Unknown pose preset: {preset}")
            return self._primitives["move_pose"].execute(*pose)

        raise ValueError(f"Unsupported task: {task_name}")

    def _extract_preset(self, task_name: str, prefix: str, default: str) -> str:
        if task_name == prefix:
            return default

        suffix = task_name[len(prefix):]
        if suffix.startswith("_"):
            suffix = suffix[1:]

        if not suffix:
            return default

        if prefix == "move_pose":
            if suffix.isdigit():
                return f"pose_{suffix}"
            if suffix.startswith("pose_"):
                return suffix
            return suffix

        if prefix == "move_joint":
            if suffix.isdigit():
                joint_map = {"1": "home", "2": "ready", "3": "front", "4": "left", "5": "right", "6": "park"}
                return joint_map.get(suffix, default)
            return suffix

        return suffix

    def _get_pose_config(self, preset_name: str):
        from robot_skill_primitives.motion.skill_config import get_pose_config

        return get_pose_config(preset_name)


def main(args=None):
    raise SystemExit("SkillManager is a library component and does not expose a standalone CLI.")
