from moveit_msgs.srv import GetPositionIK

from geometry_msgs.msg import PoseStamped

import rclpy


class IKSolver:

    def __init__(self, node):

        self._node = node

        self._client = node.create_client(
            GetPositionIK,
            "/compute_ik"
        )

        while not self._client.wait_for_service(timeout_sec=1.0):
            node.get_logger().info(
                "Waiting for /compute_ik..."
            )

    def compute_ik(
        self,
        x,
        y,
        z,
        qx,
        qy,
        qz,
        qw
    ):

        req = GetPositionIK.Request()

        req.ik_request.group_name = "manipulator"

        req.ik_request.ik_link_name = "tool0"

        pose = PoseStamped()

        pose.header.frame_id = "base_link"

        pose.pose.position.x = x
        pose.pose.position.y = y
        pose.pose.position.z = z

        pose.pose.orientation.x = qx
        pose.pose.orientation.y = qy
        pose.pose.orientation.z = qz
        pose.pose.orientation.w = qw

        req.ik_request.pose_stamped = pose

        req.ik_request.timeout.sec = 5

        req.ik_request.avoid_collisions = False

        future = self._client.call_async(req)

        rclpy.spin_until_future_complete(
            self._node,
            future
        )

        result = future.result()

        if result.error_code.val != 1:

            self._node.get_logger().error(
                "No IK solution found."
            )

            return None

        return (
            result.solution.joint_state.name,
            result.solution.joint_state.position
        )
