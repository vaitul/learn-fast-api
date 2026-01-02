### FastAPI

## Getting Started

### Prerequisites
- Python 3.7+
- pip

### Installation
1. Clone the repository
2. Create a virtual environment:
    ```bash
    python -m venv .venv
    ```
3. Activate it (macOS/Linux):
    ```bash
    source .venv/bin/activate
    ```
4. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Running the Application
```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

### API Documentation
- Interactive docs: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`