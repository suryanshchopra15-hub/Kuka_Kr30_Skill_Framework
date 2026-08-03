from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription, OpaqueFunction, TimerAction
from launch.substitutions import LaunchConfiguration
from launch.launch_description_sources.python_launch_description_source import (
    PythonLaunchDescriptionSource,
)
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory


def launch_setup(context, *args, **kwargs):
    robot_model = LaunchConfiguration("robot_model")
    robot_family = LaunchConfiguration("robot_family")

    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            [
                get_package_share_directory("kuka_gazebo"),
                "/launch/gazebo_startup.launch.py",
            ]
        ),
        launch_arguments={
            "robot_model": robot_model,
            "robot_family": robot_family,
            "use_gui": "true",
        }.items(),
    )

    moveit_server = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            [
                get_package_share_directory("kuka_kr_moveit_config"),
                "/launch/moveit_server.launch.py",
            ]
        ),
        launch_arguments={
            "robot_model": robot_model,
            "robot_family": robot_family,
            "use_sim_time": "true",
        }.items(),
    )

    task_manager = Node(
        package="robot_skill_task_manager",
        executable="task_manager",
        name="task_manager",
        output="screen",
    )

    delayed_task_manager = TimerAction(
        period=8.0,
        actions=[task_manager],
    )

    return [gazebo, moveit_server, delayed_task_manager]


def generate_launch_description():
    return LaunchDescription(
        [
            DeclareLaunchArgument("robot_model", default_value="kr30_r2100"),
            DeclareLaunchArgument("robot_family", default_value="iontec"),
            OpaqueFunction(function=launch_setup),
        ]
    )
