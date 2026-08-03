from setuptools import find_packages, setup

package_name = 'kr30_control'

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
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
    'console_scripts': [
        'joint_controller = kr30_control.joint_controller:main',
        'motion_test = kr30_control.motion_test:main',
        'ik_solver = kr30_control.ik_solver:main',
    ],
 }, 
)
