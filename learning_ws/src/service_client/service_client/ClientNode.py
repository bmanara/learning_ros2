import sys

import rclpy
from rclpy.node import Node

from interfaces.srv import MultiplyThree


class ClientNode(Node):
    def __init__(self):
        super().__init__('client')
        self.get_logger().info('Client node initialized')
        # Initialize the client here
        self.client = self.create_client(MultiplyThree, 'multiply_three')
        self.get_logger().info('Client created')

        # Wait for the service to be available
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Service not available, waiting again...')

        self.req = MultiplyThree.Request()

    def send_request(self, x, y, z):
        self.req.x = x
        self.req.y = y
        self.req.z = z

        return self.client.call_async(self.req)
    
def main(args=None):
    rclpy.init()
    client_node = ClientNode()
    
    x = sys.argv[1]
    y = sys.argv[2]
    z = sys.argv[3]

    future = client_node.send_request(int(x), int(y), int(z))
    rclpy.spin_until_future_complete(client_node, future)
    response = future.result()
    client_node.get_logger().info(f'Result of multiply_three: {response.product}')

    client_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
