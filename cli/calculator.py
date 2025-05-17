import typer
from core import calculator
app = typer.Typer()

@app.command()
def add(a: float, b: float):
    """Add two numbers."""
    result = calculator.add(a, b)
    typer.echo(f"The result of addition is: {result}")

@app.command()
def subtract(a: float, b: float):
    """Subtract two numbers."""
    result = calculator.subtract(a, b)
    typer.echo(f"The result of subtraction is: {result}")

@app.command()
def multiply(a: float, b: float):
    """Multiply two numbers."""
    result = calculator.multiply(a, b)
    typer.echo(f"The result of multiplication is: {result}")

@app.command()
def divide(a: float, b: float):
    """Divide two numbers."""
    try:
        result = calculator.divide(a, b)
        typer.echo(f"The result of division is: {result}")
    except ValueError as e:
        typer.echo(f"Error: {e}")

