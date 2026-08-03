from setuptools import find_packages, setup

package_name = 'robot_skill_primitives'

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
            "test_move_home = robot_skill_primitives.test_move_home:main",
            "test_move_pose = robot_skill_primitives.test_move_pose:main",     
        ],
    },
)
