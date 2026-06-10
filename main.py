# Модель: Власний код (Метод градієнтного спуску)
# Автор: Шарапов Валерій Валерійович, група АІ-235

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Gradient Descent API")

# Визначаємо структуру JSON-запиту
class OptimizationRequest(BaseModel):
    start_x: float
    learning_rate: float = 0.1  # Значення за замовчуванням
    max_iterations: int = 1000  # Значення за замовчуванням

class GradientDescentOptimizer:
    def __init__(self, learning_rate, max_iterations, tolerance=1e-6):
        self.learning_rate = learning_rate
        self.max_iterations = max_iterations
        self.tolerance = tolerance

    def optimize(self, func, grad_func, start_x):
        x = start_x
        history = []

        for i in range(self.max_iterations):
            grad = grad_func(x)
            new_x = x - self.learning_rate * grad

            if abs(new_x - x) < self.tolerance:
                history.append({"iteration": i+1, "x": new_x, "f_x": func(new_x)})
                x = new_x
                break

            x = new_x
            if (i + 1) % 10 == 0:
                history.append({"iteration": i+1, "x": x, "f_x": func(x)})

        return x, history

# Цільова функція f(x) = x^2 - 4x + 4 та її похідна
def objective_function(x): return x**2 - 4*x + 4
def gradient_function(x): return 2*x - 4

# Endpoint для обчислень (використовуємо POST, оскільки варіант непарний)
@app.post("/calculate")
def calculate_minimum(req: OptimizationRequest):
    optimizer = GradientDescentOptimizer(
        learning_rate=req.learning_rate,
        max_iterations=req.max_iterations
    )

    min_x, steps = optimizer.optimize(objective_function, gradient_function, req.start_x)

    return {
        "input_parameters": {
            "start_x": req.start_x,
            "learning_rate": req.learning_rate,
            "max_iterations": req.max_iterations
        },
        "result": {
            "minimum_x": round(min_x, 6),
            "function_value": round(objective_function(min_x), 6),
            "total_saved_steps": len(steps)
        },
        "history": steps
    }

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5000)