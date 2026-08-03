import rclpy
from rclpy.node import Node

from robot_skill_planner.planning.planner import Planner


class PlannerNode(Node):

    def __init__(self):
        super().__init__("planner_node")

        self.planner = Planner(self)


def main():

    rclpy.init()

    node = PlannerNode()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == "__main__":
    main()
