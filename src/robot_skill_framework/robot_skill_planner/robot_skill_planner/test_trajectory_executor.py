import rclpy

from rclpy.node import Node

from robot_skill_planner.planning.trajectory_executor import TrajectoryExecutor


class TrajectoryTest(Node):

    def __init__(self):

        super().__init__("trajectory_test")

        self.trajectory_executor = TrajectoryExecutor(self)

    def run(self):

        joint_names = [
            "joint_1",
            "joint_2",
            "joint_3",
            "joint_4",
            "joint_5",
            "joint_6",
        ]

        joint_positions = [
            2.0,
            -1.57,
            1.39,
            0.0,
            1.74,
            0.0,
        ]

        self.trajectory_executor.execute(
            joint_names,
            joint_positions
        )


def main():

    rclpy.init()

    node = TrajectoryTest()

    node.run()

    node.destroy_node()

    rclpy.shutdown()


if __name__ == "__main__":
    main()
