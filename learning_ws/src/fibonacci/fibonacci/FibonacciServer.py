import rclpy
from rclpy.action import ActionServer
from rclpy.node import Node

from interfaces.action import Fibonacci

import time


class FibonacciActionServer(Node):
    def __init__(self):
        super().__init__('fibonacci_action_server')
        self._action_server = ActionServer(
            self,
            Fibonacci,
            'fibonacci',
            self.execute_callback
        )
        self.get_logger().info('Fibonacci action server is ready.')

    def execute_callback(self, goal_handle):
        self.get_logger().info("Calculating Fibonacci sequence...")
        feedback_msg = Fibonacci.Feedback()
        feedback_msg.partial_sequence = [0, 1]

        for i in range(2, goal_handle.request.index):
            feedback_msg.partial_sequence.append(feedback_msg.partial_sequence[i - 1] + feedback_msg.partial_sequence[i - 2])
            goal_handle.publish_feedback(feedback_msg)
            time.sleep(0.5)
        
        goal_handle.succeed()
        result = Fibonacci.Result()
        result.sequence = feedback_msg.partial_sequence 
        return result

def main(args=None):
    rclpy.init(args=args)
    fibonacci_action_server = FibonacciActionServer()
    rclpy.spin(fibonacci_action_server)
    fibonacci_action_server.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
