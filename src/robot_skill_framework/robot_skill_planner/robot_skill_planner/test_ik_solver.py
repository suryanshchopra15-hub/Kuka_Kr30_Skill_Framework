import rclpy

from rclpy.node import Node

from robot_skill_planner.planning.ik_solver import IKSolver


class IKTest(Node):

    def __init__(self):

        super().__init__("ik_test")

        self.ik_solver = IKSolver(self)

    def run(self):

        result = self.ik_solver.compute_ik(
            x=1.20,
            y=0.00,
            z=1.50,
            qx=0.0,
            qy=1.0,
            qz=0.0,
            qw=0.0
        )

        if result is None:

            self.get_logger().error(
                "IK computation failed."
            )

            return

        joint_names, joint_positions = result

        self.get_logger().info(
            "IK computation successful."
        )

        self.get_logger().info(
            "Joint Solution:"
        )

        for name, position in zip(
            joint_names,
            joint_positions
        ):

            self.get_logger().info(
                f"{name}: {position:.6f}"
            )


def main():

    rclpy.init()

    node = IKTest()

    node.run()

    node.destroy_node()

    rclpy.shutdown()


if __name__ == "__main__":
    main()
