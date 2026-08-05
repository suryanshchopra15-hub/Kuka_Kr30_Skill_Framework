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

# Development of a Reusable Skill Framework for Industrial Robot Manipulators Using ROS 2

## Project Description

Industrial robotic applications are often developed as tightly coupled software systems, where motion planning, robot control, and task execution are highly dependent on the underlying hardware and application logic. This makes software difficult to reuse, maintain, and extend when deploying the same application on different robotic platforms or introducing new robotic tasks.

This project addresses this challenge by developing a lightweight and reusable skill framework for industrial robot manipulators using ROS 2. The framework introduces a modular software architecture that separates high level task execution from low level robot control by organizing robot capabilities into reusable skills and motion primitives. Each skill represents a self contained robotic capability that can be independently developed, executed, and combined with other skills to create more complex robotic workflows.

To validate the framework, a complete robotic simulation environment was developed for the KUKA KR30 industrial manipulator. The robot description was created using URDF and Xacro, providing an accurate kinematic model of the robot and its associated tool frames. The robot is simulated in Gazebo Fortress, while ros2_control manages communication between the simulation and the robot controllers. Motion planning is performed using MoveIt 2, which provides inverse kinematics, collision checking, trajectory generation, and execution through the ROS 2 ecosystem. Together, these components form a complete robotics software pipeline that serves as the execution backend for the proposed framework. MoveIt is designed as a manipulation framework built on top of ROS 2, while ros2_control provides standardized controller interfaces for robot hardware and simulation. :contentReference[oaicite:0]{index=0}

The reusable skill framework is implemented as an additional abstraction layer above the robotics middleware. It consists of a Task Manager, Skill Manager, Primitive Library, and Planner Interface. The Task Manager receives high level user requests and decomposes them into executable skills. The Skill Manager coordinates the execution of these skills, monitors their status, and manages transitions between different operations. Each skill is composed of reusable motion primitives such as moving to a predefined home position, executing joint space motion, performing Cartesian pose movement, or waiting for external events. The Planner Interface communicates with MoveIt 2 to generate feasible trajectories before forwarding them to ros2_control for execution.

The modular architecture enables new robotic applications to be created by combining existing skills instead of developing application specific control software from scratch. Because the framework remains independent of the underlying robot implementation, only the robot description, controllers, and planner configuration need to be adapted when integrating another industrial manipulator. This significantly improves software maintainability, scalability, and code reuse while reducing development time for future robotic applications.

The project demonstrates how modern ROS 2 based software architectures can be used to build reusable, extensible, and hardware independent robotic applications suitable for research, industrial automation, and rapid prototyping. The KUKA KR30 simulation serves as the validation platform, while the framework itself is designed to be adaptable to a wide range of industrial robotic manipulators.

## Framework Description

The reusable skill framework provides a modular software architecture for executing robotic operations through reusable motion skills. The framework separates high level task execution from low level robot control, allowing robot capabilities to be developed as independent and reusable software components. A Task Manager receives user requests and forwards them to the Skill Manager, which selects and executes the appropriate skill. Each skill communicates with the Planner Interface, which generates collision free trajectories using MoveIt 2 and executes them through ros2_control in the Gazebo simulation environment. This layered architecture promotes modularity, maintainability, and code reuse, making it easier to extend the framework with additional robotic capabilities in the future. Skill based architectures like this are widely used to improve reusability and flexibility in robotic systems. :contentReference[oaicite:0]{index=0}

### Currently Implemented Skills

The current version of the framework includes the following reusable motion skills:

- **Move Home** – Moves the robot to a predefined home configuration.
- **Move Joint** – Executes motion to specified joint configuration.
- **Move Pose** – Plans and executes motion to a specified end effector pose using MoveIt 2.

These skills demonstrate the core functionality of the framework and serve as reusable building blocks for developing more complex robotic applications. The modular design allows additional skills, such as pick and place, tool operations, or process specific tasks, to be integrated without modifying the overall architecture. :contentReference[oaicite:1]{index=1}
