"""
This module provides CLI commands for performing basic arithmetic operations.

It uses the `typer` library to define commands for addition, subtraction, multiplication,
and division. Each command takes two numbers as input and prints the result to the console.

The module relies on the `core.calculator` module for the actual arithmetic operations.
"""

import typer
from core import calculator
app = typer.Typer()

@app.command()
def add(a: float, b: float):
    """
    Add two numbers.

    Args:
        a (float): The first number to add.
        b (float): The second number to add.

    Returns:
        None: Prints the result of the addition to the console.
    """
    result = calculator.add(a, b)
    typer.echo(f"The result of addition is: {result}")

@app.command()
def subtract(a: float, b: float):
    """
    Subtract two numbers.

    Args:
        a (float): The number to subtract from.
        b (float): The number to subtract.

    Returns:
        None: Prints the result of the subtraction to the console.
    """
    result = calculator.subtract(a, b)
    typer.echo(f"The result of subtraction is: {result}")

@app.command()
def multiply(a: float, b: float):
    """
    Multiply two numbers.

    Args:
        a (float): The first number to multiply.
        b (float): The second number to multiply.

    Returns:
        None: Prints the result of the multiplication to the console.
    """
    result = calculator.multiply(a, b)
    typer.echo(f"The result of multiplication is: {result}")

@app.command()
def divide(a: float, b: float):
    """
    Divide two numbers.

    Args:
        a (float): The numerator.
        b (float): The denominator.

    Returns:
        None: Prints the result of the division to the console. If division by zero occurs, an error message is printed.
    """
    try:
        result = calculator.divide(a, b)
        typer.echo(f"The result of division is: {result}")
    except ValueError as e:
        typer.echo(f"Error: {e}")

