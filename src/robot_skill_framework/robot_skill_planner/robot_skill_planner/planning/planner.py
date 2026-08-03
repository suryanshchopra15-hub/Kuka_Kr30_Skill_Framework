from robot_skill_planner.planning.ik_solver import IKSolver
from robot_skill_planner.planning.trajectory_executor import (
    TrajectoryExecutor,
)
from robot_skill_planner.planning.robot_state import RobotState


class Planner:

    def __init__(self, node):

        self._node = node

        self._robot_state = RobotState(node)

        self._ik_solver = IKSolver(node)

        self._trajectory_executor = TrajectoryExecutor(node)

    def move_to_pose(
        self,
        x,
        y,
        z,
        qx,
        qy,
        qz,
        qw,
    ):

        result = self._ik_solver.compute_ik(
            x,
            y,
            z,
            qx,
            qy,
            qz,
            qw,
        )

        if result is None:

            self._node.get_logger().error(
                "IK computation failed."
            )

            return False

        joint_names, joint_positions = result

        return self._trajectory_executor.execute(
            joint_names,
            joint_positions,
        )

    def move_to_joint_positions(
        self,
        joint_names,
        joint_positions,
    ):

        return self._trajectory_executor.execute(
            joint_names,
            joint_positions,
        )

    def get_current_joint_state(self):

        return self._robot_state.get_joint_state()

    def get_current_joint_names(self):

        return self._robot_state.get_joint_names()

    def get_current_joint_positions(self):

        return self._robot_state.get_joint_positions()

    def get_current_joint_position(
        self,
        joint_name,
    ):

        return self._robot_state.get_joint_position(
            joint_name
        )

    def has_robot_state(self):

        return self._robot_state.has_state()