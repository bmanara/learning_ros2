import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from interfaces.msg import Measurements

class SubscriberNode(Node):
    def __init__(self):
        super().__init__('subscriber')
        self.subscription = self.create_subscription(
            Measurements, 
            'measurement', 
            self.listener_callback, 
            10)
        
        self.subscription

    def listener_callback(self, msg):
        height = msg.height
        weight = msg.weight 
        self.get_logger().info(f'Received: Height={height} | Weight={weight}' )

def main(args=None):
    rclpy.init()
    subscriber_node = SubscriberNode()
    rclpy.spin(subscriber_node)
    subscriber_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
