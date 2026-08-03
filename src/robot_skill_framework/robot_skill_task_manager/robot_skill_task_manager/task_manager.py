import rclpy
from rclpy.action import ActionServer
from rclpy.node import Node

from robot_skill_interfaces.action import ExecuteTask
from robot_skill_manager.skill_manager import SkillManager
from robot_skill_planner.planning.planner import Planner


class TaskManagerNode(Node):
    """Simple action server for the resume demo workflow."""

    def __init__(self):
        super().__init__("task_manager")
        self._planner = Planner(self)
        self._skill_manager = SkillManager(self._planner)
        self._action_server = ActionServer(
            self,
            ExecuteTask,
            "execute_task",
            self._execute_callback,
        )

    def _execute_callback(self, goal_handle):
        task_name = goal_handle.request.task_name
        self.get_logger().info(f"Executing task: {task_name}")

        try:
            success = self._skill_manager.execute(task_name)
        except Exception as exc:  # pragma: no cover - simple demo path
            self.get_logger().error(f"Task failed: {exc}")
            goal_handle.abort()
            return ExecuteTask.Result(success=False, message=str(exc))

        if success:
            goal_handle.succeed()
            return ExecuteTask.Result(success=True, message="Task completed")

        goal_handle.abort()
        return ExecuteTask.Result(success=False, message="Task execution failed")


def main(args=None):
    rclpy.init(args=args)
    node = TaskManagerNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
