#!/usr/bin/env python3
"""
Demo: ReAct agent with reasoning and tool invocation.
"""

def calculator(a: float, b: float) -> float:
    return a + b

if __name__ == "__main__":
    print("Thought: First, compute the sum of 7 and 5.")
    sum_result = calculator(7, 5)
    print(f"Action: calculator(7, 5) -> {sum_result}")
    print("Observation: Received sum result")
    print("Thought: Next, multiply 3 and the sum result.")
    product = 3 * sum_result
    print(f"Action: multiply 3 and {sum_result} -> {product}")
    print(f"Final Answer: The answer is {product}")
