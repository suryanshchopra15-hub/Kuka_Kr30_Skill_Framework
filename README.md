# ROS 2 KUKA KR30 Project

A ROS 2 workspace for simulation, control, motion planning, and skill-based task execution for the KUKA KR30 robot.

## Overview

This repository contains a complete ROS 2 project built around KUKA industrial robots, with a focus on the KR30 platform. It combines robot descriptions, motion control, planning, and a modular robot skill framework for developing and testing robotic tasks.

The project includes:

- KUKA robot description packages
- KR30 robot control utilities
- MoveIt and planning-related components
- A custom robot skill framework
- Motion primitives and task execution modules
- ROS 2 interfaces for robot skills and commands

## Repository Structure

```bash
ros2_projects/
└── src/
    ├── kr30_pipeline/
    │   └── kr30_control/
    ├── kuka_robot_descriptions/
    └── robot_skill_framework/
        ├── robot_skill_bringup/
        ├── robot_skill_examples/
        ├── robot_skill_interfaces/
        ├── robot_skill_manager/
        ├── robot_skill_planner/
        ├── robot_skill_primitives/
        └── robot_skill_task_manager/
