import rclpy

from rclpy.node import Node
from rclpy.publisher import Publisher

from trajectory_msgs.msg import JointTrajectory
from trajectory_msgs.msg import JointTrajectoryPoint

from builtin_interfaces.msg import Duration


class TrajectoryExecutor:

    def __init__(self, node):

        self._node = node

        self._publisher: Publisher = node.create_publisher(
            JointTrajectory,
            "/joint_trajectory_controller/joint_trajectory",
            10,
        )

    def execute(
        self,
        joint_names,
        joint_positions,
        duration=5
    ):

        trajectory = JointTrajectory()

        trajectory.joint_names = list(joint_names)

        point = JointTrajectoryPoint()

        point.positions = list(joint_positions)

        point.time_from_start = Duration(
            sec=duration,
            nanosec=0,
        )

        trajectory.points.append(point)

        self._node.get_logger().info(
            "Publishing trajectory to Gazebo controller..."
        )

        self._publisher.publish(trajectory)

        self._node.get_logger().info(
            "Trajectory published."
        )

        return True
