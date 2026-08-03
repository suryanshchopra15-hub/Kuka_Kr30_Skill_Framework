import rclpy

from rclpy.node import Node

from robot_skill_planner.planning.planner import Planner

from robot_skill_primitives.motion.move_home import MoveHome


class MoveHomeTest(Node):

    def __init__(self):

        super().__init__("move_home_test")

        planner = Planner(self)

        self._move_home = MoveHome(planner)

    def run(self):

        success = self._move_home.execute()

        if success:

            self.get_logger().info(
                "MoveHome successful."
            )

        else:

            self.get_logger().error(
                "MoveHome failed."
            )


def main():

    rclpy.init()

    node = MoveHomeTest()

    node.run()

    node.destroy_node()

    rclpy.shutdown()


if __name__ == "__main__":

    main()