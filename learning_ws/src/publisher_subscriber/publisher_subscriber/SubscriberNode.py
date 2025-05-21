import rclpy
from rclpy.node import Node

from std_msgs.msg import String

class SubscriberNode(Node):
    def __init__(self):
        super().__init__('subscriber')
        self.subscription = self.create_subscription(
            String, 
            'comment', 
            self.listener_callback, 
            10)
        
        self.subscription

    def listener_callback(self, msg):
        data = msg.data
        self.get_logger().info(f'Received: %s {data}' )

def main(args=None):
    rclpy.init()
    subscriber_node = SubscriberNode()
    rclpy.spin(subscriber_node)
    subscriber_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
