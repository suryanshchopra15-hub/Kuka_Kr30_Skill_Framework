from setuptools import find_packages, setup

package_name = 'robot_skill_planner'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='suryansh',
    maintainer_email='suryanshchopra15@gmail.com',
    description='TODO: Package description',
    license='Apache-2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
             'test_planner = robot_skill_planner.test_planner:main',
             'test_ik_solver = robot_skill_planner.test_ik_solver:main',
             'test_trajectory_executor = robot_skill_planner.test_trajectory_executor:main',
        ],
    },
)
