#!/usr/bin/env python3

import sys

import rclpy
from rclpy.node import Node

from trajectory_msgs.msg import JointTrajectory
from trajectory_msgs.msg import JointTrajectoryPoint


class KR30MotionTest(Node):

    def __init__(self, position_a, position_b):

        super().__init__('kr30_motion_test')

        self.publisher_ = self.create_publisher(
            JointTrajectory,
            '/joint_trajectory_controller/joint_trajectory',
            10
        )

        self.position_a = position_a
        self.position_b = position_b

        self.position_toggle = False

        self.timer = self.create_timer(
            20.0,
            self.send_trajectory
        )

        self.get_logger().info(
            'KR30 Motion Test Started'
        )

        self.send_trajectory()

    def send_trajectory(self):

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

        if self.position_toggle:

            point.positions = self.position_a

            self.get_logger().info(
                f'Moving to Position A: {self.position_a}'
            )

        else:

            point.positions = self.position_b

            self.get_logger().info(
                f'Moving to Position B: {self.position_b}'
            )

        point.time_from_start.sec = 15
        point.time_from_start.nanosec = 0

        msg.points.append(point)

        self.publisher_.publish(msg)

        self.position_toggle = not self.position_toggle


def main():

    if len(sys.argv) != 13:

        print(
            "\nUsage:\n"
            "ros2 run kr30_control motion_test "
            "A1 A2 A3 A4 A5 A6 "
            "B1 B2 B3 B4 B5 B6\n"
        )

        return

    position_a = [
        float(sys.argv[1]),
        float(sys.argv[2]),
        float(sys.argv[3]),
        float(sys.argv[4]),
        float(sys.argv[5]),
        float(sys.argv[6])
    ]

    position_b = [
        float(sys.argv[7]),
        float(sys.argv[8]),
        float(sys.argv[9]),
        float(sys.argv[10]),
        float(sys.argv[11]),
        float(sys.argv[12])
    ]

    rclpy.init()

    node = KR30MotionTest(
        position_a,
        position_b
    )

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()
