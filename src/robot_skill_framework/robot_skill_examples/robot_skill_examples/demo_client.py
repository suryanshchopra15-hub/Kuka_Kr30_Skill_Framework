import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient

from robot_skill_interfaces.action import ExecuteTask


class DemoClient(Node):
    """Simple client for triggering the demo tasks."""

    def __init__(self):
        super().__init__("demo_client")
        self._client = ActionClient(self, ExecuteTask, "execute_task")

    def send_task(self, task_name: str):
        self._client.wait_for_server()
        goal = ExecuteTask.Goal(task_name=task_name)
        future = self._client.send_goal_async(goal)
        rclpy.spin_until_future_complete(self, future)
        goal_handle = future.result()
        if not goal_handle.accepted:
            return False
        result_future = goal_handle.get_result_async()
        rclpy.spin_until_future_complete(self, result_future)
        result = result_future.result().result
        return result.success


def main(args=None):
    rclpy.init(args=args)
    node = DemoClient()

    tasks = [
        "move_home",
        "move_joint_home",
        "move_joint_ready",
        "move_joint_front",
        "move_joint_left",
        "move_joint_right",
        "move_joint_park",
        "move_pose_1",
        "move_pose_2",
        "move_pose_3",
        "move_pose_4",
        "move_pose_5",
        "move_pose_6",
    ]

    for task_name in tasks:
        success = node.send_task(task_name)
        node.get_logger().info(f"{task_name} -> {success}")

    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
