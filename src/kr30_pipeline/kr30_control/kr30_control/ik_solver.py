import sys

import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient

from moveit_msgs.srv import GetPositionIK

from geometry_msgs.msg import PoseStamped

from control_msgs.action import FollowJointTrajectory

from trajectory_msgs.msg import JointTrajectory
from trajectory_msgs.msg import JointTrajectoryPoint

from builtin_interfaces.msg import Duration


class IKClient(Node):

    def __init__(self, x, y, z, qx, qy, qz, qw):

        super().__init__('ik_client')

        self.x = x
        self.y = y
        self.z = z

        self.qx = qx
        self.qy = qy
        self.qz = qz
        self.qw = qw

        self.ik_client = self.create_client(
            GetPositionIK,
            '/compute_ik'
        )

        while not self.ik_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info(
                'Waiting for /compute_ik...'
            )

        self.trajectory_client = ActionClient(
            self,
            FollowJointTrajectory,
            '/joint_trajectory_controller/follow_joint_trajectory'
        )

    def move_robot(self, joint_names, joint_positions):

        self.get_logger().info(
            "Waiting for trajectory controller..."
        )

        self.trajectory_client.wait_for_server()

        goal_msg = FollowJointTrajectory.Goal()

        trajectory = JointTrajectory()
        trajectory.joint_names = list(joint_names)

        point = JointTrajectoryPoint()
        point.positions = list(joint_positions)

        point.time_from_start = Duration(
            sec=5,
            nanosec=0
        )

        trajectory.points.append(point)

        goal_msg.trajectory = trajectory

        self.get_logger().info(
            "Sending trajectory..."
        )

        send_goal_future = self.trajectory_client.send_goal_async(
            goal_msg
        )

        rclpy.spin_until_future_complete(
            self,
            send_goal_future
        )

        goal_handle = send_goal_future.result()

        if not goal_handle.accepted:

            self.get_logger().error(
                "Goal rejected"
            )

            return

        self.get_logger().info(
            "Goal accepted"
        )

        result_future = goal_handle.get_result_async()

        rclpy.spin_until_future_complete(
            self,
            result_future
        )

        self.get_logger().info(
            "Motion finished"
        )

    def solve(self):

        req = GetPositionIK.Request()

        req.ik_request.group_name = "manipulator"
        req.ik_request.ik_link_name = "tool0"

        pose = PoseStamped()

        pose.header.frame_id = "base_link"

        pose.pose.position.x = self.x
        pose.pose.position.y = self.y
        pose.pose.position.z = self.z

        pose.pose.orientation.x = self.qx
        pose.pose.orientation.y = self.qy
        pose.pose.orientation.z = self.qz
        pose.pose.orientation.w = self.qw

        req.ik_request.pose_stamped = pose

        req.ik_request.timeout.sec = 5

        req.ik_request.avoid_collisions = False

        future = self.ik_client.call_async(req)

        rclpy.spin_until_future_complete(
            self,
            future
        )

        result = future.result()

        print("\nIK Result:")
        print(
            "Error code:",
            result.error_code.val
        )

        names = result.solution.joint_state.name
        positions = result.solution.joint_state.position

        for n, p in zip(names, positions):
            print(f"{n}: {p}")

        if result.error_code.val == 1:

            print(
                "\nIK successful. Moving robot...\n"
            )

            self.move_robot(
                names,
                positions
            )

        else:

            print(
                "\nNo IK solution found."
            )


def main():

    if len(sys.argv) != 8:

        print("\nUsage:")

        print(
            "ros2 run kr30_control ik_solver "
            "x y z qx qy qz qw"
        )

        return

    x = float(sys.argv[1])
    y = float(sys.argv[2])
    z = float(sys.argv[3])

    qx = float(sys.argv[4])
    qy = float(sys.argv[5])
    qz = float(sys.argv[6])
    qw = float(sys.argv[7])

    rclpy.init()

    node = IKClient(
        x,
        y,
        z,
        qx,
        qy,
        qz,
        qw
    )

    node.solve()

    node.destroy_node()

    rclpy.shutdown()


if __name__ == "__main__":
    main()
