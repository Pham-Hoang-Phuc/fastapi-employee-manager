# Fastapi-employee-manager

**Fastapi-employee-manager** is a lightweight and high-performance RESTful API designed to streamline personnel information management. Built with **FastAPI** and **SQLAlchemy**, it provides a robust backend for handling employee records, fully containerized with **Docker** for seamless deployment.

## Prerequisites

Before you begin, ensure you have met the following requirements:

* **Python 3.11+** installed on your local machine.
* **Docker** and **Docker Compose** (optional, for containerized execution).
* A basic understanding of RESTful APIs and Python virtual environments.

## Installation

Follow these steps to get your development environment set up:

### 1. Local Setup

1. **Clone the repository:**
```bash
git clone https://github.com/username/fastapi-employee-manager.git
cd fastapi-employee-manager
```


2. **Create and activate a virtual environment:**
```bash
python -m venv venv
venv\Scripts\activate
```


3. **Install the required dependencies:**
```bash
pip install -r requirements.txt
```



### 2. Docker Setup

Alternatively, you can run the application using Docker:

1. **Build the Docker image:**
```bash
docker build -t fastapi-employee-manager .
```

2. **Run the container:**
```bash
docker run -d -p 8000:8000 fastapi-employee-manager
```



## Usage

Once the server is running, you can interact with the API:

1. **Start the server (Local):**
```bash
uvicorn main:app --reload
```


2. **Register a New Employee:**
Send a `POST` request to `/register` with the employee details in the JSON body.
3. **View All Employees:**
Send a `GET` request to `/employees` (ensure you have implemented this route in `main.py`).

### API Documentation

You can explore the interactive API documentation at:

* **Swagger UI:** [http://localhost:8000/docs](https://www.google.com/search?q=http://localhost:8000/docs)
* **ReDoc:** [http://localhost:8000/redoc](https://www.google.com/search?q=http://localhost:8000/redoc)

## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project.
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`).
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the Branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

## Contributors

* **Pham Hoang Phuc** - *Initial work* - [Pham Hoang Phuc](https://github.com/Pham-Hoang-Phuc)