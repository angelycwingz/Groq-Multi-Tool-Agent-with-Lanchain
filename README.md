# Multi Tool Agent App

This project is a simple and naive implementation of a Groq AI Agent application that uses multiple tools, including a calculator (custom tool), Wikipedia, and Tavily Search. It is built using FastAPI and LangChain for the backend, with a Streamlit-based frontend UI. The application is designed to demonstrate the basic concepts and functionality of integrating multiple tools into a cohesive application. While it is not optimized for production use, it serves as a great starting point for understanding the architecture and workflow of such systems.

## Project Structure

The project is divided into two main components:

1. **Backend**: Contains the core logic and APIs for the application.
   - `agent.py`: Handles the agent logic.
   - `main.py`: Entry point for the backend server.
   - `schemas.py`: Defines the data models and schemas.
   - `tools.py`: Contains utility functions and tools used by the agent.
   - `requirements.txt`: Lists the dependencies for the backend.

2. **Frontend**: Provides a simple user interface for interacting with the backend.
   - `app.py`: The main script for the frontend application.
   - `requirements.txt`: Lists the dependencies for the frontend.

## Features

- Integration of multiple tools: calculator (custom tool), Wikipedia, and Tavily Search.
- Built using FastAPI and LangChain for backend development.
- Streamlit-based frontend UI for user interaction.
- Provides a minimalistic example for learning and experimentation.

## Limitations

- This project is not optimized for scalability or performance.
- It is intended for educational purposes and may lack advanced features.

## Getting Started

### Prerequisites

- Python 3.10 or higher
- pip (Python package manager)

### Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```

2. Navigate to the project directory:
   ```bash
   cd Multi Tool Agent App
   ```

3. Install the dependencies for both backend and frontend:
   ```bash
   pip install -r backend/requirements.txt
   pip install -r frontend/requirements.txt
   ```

### Running the Application

1. Start the backend server:
   ```bash
   cd backend
   python main.py
   ```

2. Start the frontend application:
   ```bash
   cd frontend
   python app.py
   ```

3. Access the application through the provided URLs.

## Contributing

Contributions are welcome! Feel free to fork the repository and submit pull requests.

## License

This project is licensed under the MIT License. See the LICENSE file for details.