#!/usr/bin/env python3
"""
Demo: Agent reasoning with calculator tool.
"""

def calculator(a: float, b: float, operation: str) -> float:
    """Simple calculator tool supporting add, sub, mul, div."""
    if operation == "add":
        return a + b
    elif operation == "sub":
        return a - b
    elif operation == "mul":
        return a * b
    elif operation == "div":
        return a / b
    else:
        raise ValueError(f"Unsupported operation: {operation}")

class Agent:
    def __init__(self):
        self.history = []

    def reason_and_act(self, question: str):
        print("Agent Reasoning: Determining steps to solve the question.")
        self.history.append("Reasoning: parse question")
        parts = question.strip("?").split()
        a, op_word, b = float(parts[2]), parts[3], float(parts[4])
        op_map = {"plus": "add", "minus": "sub", "times": "mul", "divided": "div"}
        operation = op_map.get(op_word)
        print(f"Agent Action: Invoking calculator({a}, {b}, '{operation}')")
        result = calculator(a, b, operation)
        print(f"Agent Observation: Received result {result}")
        print(f"Final Answer: The result is {result}")

if __name__ == "__main__":
    question = "What is 2 plus 3?"
    Agent().reason_and_act(question)
