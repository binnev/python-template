from fastapi import FastAPI

from .calculator import calculator_router

app = FastAPI()

app.include_router(calculator_router, prefix="/calculator")


if __name__ == "__main__":
    app()
