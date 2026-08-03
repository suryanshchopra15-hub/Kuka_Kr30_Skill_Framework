import rclpy

from rclpy.node import Node

from robot_skill_planner.planning.planner import Planner

from robot_skill_primitives.motion.move_pose import MovePose


class MovePoseTest(Node):

    def __init__(self):

        super().__init__("move_pose_test")

        planner = Planner(self)

        self._move_pose = MovePose(planner)

    def run(self):

        success = self._move_pose.execute(
            x=1.20,
            y=0.00,
            z=1.50,
            qx=0.0,
            qy=1.0,
            qz=0.0,
            qw=0.0,
        )

        if success:

            self.get_logger().info(
                "MovePose successful."
            )

        else:

            self.get_logger().error(
                "MovePose failed."
            )


def main():

    rclpy.init()

    node = MovePoseTest()

    node.run()

    node.destroy_node()

    rclpy.shutdown()


if __name__ == "__main__":

    main()
    