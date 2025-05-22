import rclpy
from rclpy.parameter import Parameter
from rclpy.node import Node

from interfaces.srv import MultiplyThree


class ServiceNode(Node):
    def __init__(self):
        super().__init__('service')
        self.get_logger().info('Service node initialized')
        # Initialize the service here
        self.srv = self.create_service(MultiplyThree, 'multiply_three', self.multiply_three_callback)
        self.get_logger().info('Service created')
        self.declare_parameter('count', 0)

    def multiply_three_callback(self, request, response):
        response.product = request.x * request.y * request.z
        response.count = self.get_parameter('count').value + 1
        updated_count = Parameter('count', Parameter.Type.INTEGER, response.count)
        self.set_parameters([updated_count])
        return response
    
def main(args=None):
    rclpy.init()
    service_node = ServiceNode()
    rclpy.spin(service_node)
    
    service_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
