#!/usr/bin/env python3

import sys

import rclpy
from rclpy.node import Node

from trajectory_msgs.msg import JointTrajectory
from trajectory_msgs.msg import JointTrajectoryPoint


class KR30JointController(Node):

    def __init__(self, joint_positions):

        super().__init__('kr30_joint_controller')

        self.publisher_ = self.create_publisher(
            JointTrajectory,
            '/joint_trajectory_controller/joint_trajectory',
            10
        )

        self.joint_positions = joint_positions

        self.timer = self.create_timer(
            2.0,
            self.send_trajectory
        )

        self.sent = False

    def send_trajectory(self):

        if self.sent:
            return

        msg = JointTrajectory()

        msg.joint_names = [
            'joint_1',
            'joint_2',
            'joint_3',
            'joint_4',
            'joint_5',
            'joint_6'
        ]

        point = JointTrajectoryPoint()

        point.positions = self.joint_positions

        point.time_from_start.sec = 5

        msg.points.append(point)

        self.publisher_.publish(msg)

        self.get_logger().info(
            f'Trajectory sent: {self.joint_positions}'
        )

        self.sent = True


def main():

    if len(sys.argv) != 7:

        print(
            "\nUsage:\n"
            "ros2 run kr30_control joint_controller "
            "j1 j2 j3 j4 j5 j6\n"
        )

        return

    joint_positions = [
        float(sys.argv[1]),
        float(sys.argv[2]),
        float(sys.argv[3]),
        float(sys.argv[4]),
        float(sys.argv[5]),
        float(sys.argv[6])
    ]

    rclpy.init()

    node = KR30JointController(
        joint_positions
    )

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()
