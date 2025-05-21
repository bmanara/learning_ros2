from setuptools import find_packages, setup

package_name = 'publisher_subscriber'

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
    maintainer='bmanara',
    maintainer_email='bmacraze@gmail.com',
    description='Simple publisher and subscriber nodes to send string messages',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'publisher = publisher_subscriber.PublisherNode:main',
            'subscriber = publisher_subscriber.SubscriberNode:main',
        ],
    },
)
