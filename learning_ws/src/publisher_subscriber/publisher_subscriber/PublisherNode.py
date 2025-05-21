import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from interfaces.msg import Measurements

class PublisherNode(Node):
    def __init__(self):
        super().__init__('publisher')
        self.publisher_ = self.create_publisher(Measurements, 'measurement', 10)
        timer_period = 1.0
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        # msg = String()
        # msg.data = "This is a comment number: %d" % self.i
        msg = Measurements()
        msg.height = 1.7
        msg.weight = 49.2 + self.i
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: "Height={msg.height} | Weight={msg.weight}"')
        self.i += 1

def main(args=None):
    rclpy.init()
    publisher_node = PublisherNode()
    rclpy.spin(publisher_node)
    publisher_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
