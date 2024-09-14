# agentic-workflow-langgraph
# LanggraphAgenticWorkflow

## Overview

LanggraphAgenticWorkflow is a project that utilizes Langgraph to build an agentic workflow system. It incorporates various agents to handle tasks such as planning, solving, and providing feedback based on user queries.

## Project Structure


### Agents

- **plan_agent.py**: Contains the `PlanAgent` class that splits a user's query into manageable tasks.
- **tool_agent.py**: Contains the `ToolAgent` class that solves tasks based on predefined solutions.
- **feedback_agent.py**: Contains the `FeedbackAgent` class that provides feedback and refines tasks.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/LanggraphAgenticWorkflow.git
    ```

2. Navigate to the project directory:
    ```bash
    cd LanggraphAgenticWorkflow
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the application:
    ```bash
    streamlit run app.py
    ```

2. Open your browser and navigate to `http://localhost:8501` to interact with the Streamlit app.

## Contributing

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE.md](LICENSE.md) file for details.



