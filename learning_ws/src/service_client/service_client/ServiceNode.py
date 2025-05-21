import rclpy
from rclpy.node import Node

from interfaces.srv import MultiplyThree


class ServiceNode(Node):
    def __init__(self):
        super().__init__('service')
        self.get_logger().info('Service node initialized')
        # Initialize the service here
        self.srv = self.create_service(MultiplyThree, 'multiply_three', self.multiply_three_callback)
        self.get_logger().info('Service created')

    def multiply_three_callback(self, request, response):
        response.product = request.x * request.y * request.z
        return response
    
def main(args=None):
    rclpy.init()
    service_node = ServiceNode()
    rclpy.spin(service_node)
    
    service_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
