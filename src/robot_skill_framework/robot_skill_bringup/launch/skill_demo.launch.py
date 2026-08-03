from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription, OpaqueFunction
from launch.substitutions import LaunchConfiguration
from launch.launch_description_sources.python_launch_description_source import (
    PythonLaunchDescriptionSource,
)
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory


def launch_setup(context, *args, **kwargs):
    robot_model = LaunchConfiguration("robot_model")
    robot_family = LaunchConfiguration("robot_family")

    controller_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            [
                get_package_share_directory("kuka_resources"),
                "/launch/fake_hardware_planning_template.launch.py",
            ]
        ),
        launch_arguments={
            "robot_model": robot_model,
            "robot_family": robot_family,
            "dof": "6",
            "moveit_config": "kr",
        }.items(),
    )

    task_manager = Node(
        package="robot_skill_task_manager",
        executable="task_manager",
        name="task_manager",
        output="screen",
    )

    return [controller_launch, task_manager]


def generate_launch_description():
    return LaunchDescription(
        [
            DeclareLaunchArgument("robot_model", default_value="kr30_r2100"),
            DeclareLaunchArgument("robot_family", default_value="iontec"),
            OpaqueFunction(function=launch_setup),
        ]
    )
