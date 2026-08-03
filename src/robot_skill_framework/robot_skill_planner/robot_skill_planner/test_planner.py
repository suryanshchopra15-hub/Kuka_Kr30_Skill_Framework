import rclpy

from rclpy.node import Node

from robot_skill_planner.planning.planner import Planner


class PlannerTest(Node):

    def __init__(self):

        super().__init__("planner_test")

        self.planner = Planner(self)

    def run(self):

        success = self.planner.move_to_pose(
            x=0.50,
            y=0.00,
            z=1.50,
            qx=0.0,
            qy=1.0,
            qz=0.0,
            qw=0.0,
        )

        if success:

            self.get_logger().info(
                "Planning successful."
            )

        else:

            self.get_logger().error(
                "Planning failed."
            )


def main():

    rclpy.init()

    node = PlannerTest()

    node.run()

    node.destroy_node()

    rclpy.shutdown()


if __name__ == "__main__":

    main()