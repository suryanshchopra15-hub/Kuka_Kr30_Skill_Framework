from sensor_msgs.msg import JointState


class RobotState:

    def __init__(self, node):

        self._node = node

        self._joint_names = []

        self._joint_positions = []

        self._subscription = node.create_subscription(
            JointState,
            "/joint_states",
            self._joint_state_callback,
            10,
        )

    def _joint_state_callback(self, msg):

        self._joint_names = list(msg.name)

        self._joint_positions = list(msg.position)

    def get_joint_names(self):

        return self._joint_names

    def get_joint_positions(self):

        return self._joint_positions

    def get_joint_position(self, joint_name):

        if joint_name in self._joint_names:

            index = self._joint_names.index(joint_name)

            return self._joint_positions[index]

        return None

    def get_joint_state(self):

        return (
            self._joint_names,
            self._joint_positions,
        )

    def has_state(self):

        return len(self._joint_names) > 0