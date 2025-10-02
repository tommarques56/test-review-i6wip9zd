#!/usr/bin/env python3
"""
File with security vulnerabilities for testing.
"""

import os
import subprocess

def execute_command(user_input):
    """Execute user input as command - SECURITY RISK!"""
    # This is dangerous - should not execute user input directly
    os.system(f"echo {user_input}")  # Shell injection risk
    return "Command executed"

def evaluate_expression(expr):
    """Evaluate mathematical expression - SECURITY RISK!"""
    # eval() is dangerous with user input
    result = eval(expr)  # Code injection risk
    return result

def read_file(filename):
    """Read file without validation."""
    # No input validation
    with open(filename, 'r') as f:
        return f.read()

def main():
    user_input = input("Enter command: ")
    execute_command(user_input)
    
    expr = input("Enter expression: ")
    result = evaluate_expression(expr)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()
