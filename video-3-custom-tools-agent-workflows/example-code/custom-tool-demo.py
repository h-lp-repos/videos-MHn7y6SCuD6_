#!/usr/bin/env python3
"""
Demo: Designing and integrating a custom tool in an agent workflow.
"""
import json

def fetch_mock_data(key: str, filepath: str = 'sample-data/mock-data.json') -> str:
    """Custom tool: fetches mock data by key from JSON file."""
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
        return data.get(key, f"No entry found for key: {key}")
    except Exception as e:
        return f"Error fetching data: {e}"

class AgentWithTool:
    def __init__(self, tools: dict):
        self.tools = tools

    def run(self, key: str):
        print("Agent Thought: Fetching data for key:", key)
        result = self.tools['fetch_mock_data'](key)
        print("Agent Action: fetch_mock_data ->", result)
        print("Final Answer:", result)

if __name__ == "__main__":
    tools = {'fetch_mock_data': fetch_mock_data}
    agent = AgentWithTool(tools)
    agent.run("item1")
