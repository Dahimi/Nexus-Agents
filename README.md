

# **Agent Hub: Open-Source Platform for Specialized AI Agents**

Anthropic recently introduced Computer Use - a groundbreaking capability that allows AI to interact with computers just like humans do, through viewing screens, moving cursors, and typing. While this opens up endless possibilities for AI automation, it currently faces some key limitations: high latency in interactions, significant cost due to token usage, and reliability issues especially for specialized tasks.

This is where our solution comes in. Instead of relying on one large model to handle all computer interactions, we're building an open-source ecosystem of specialized, lightweight agents. Each agent excels at one specific task - whether it's manipulating spreadsheets, handling CLI operations, or navigating web interfaces. Some agents are small, fine-tuned LLMs, while others are simply clever software engineering solutions, choosing the most efficient approach for each task rather than defaulting to vision-based interaction.

By making this platform open-source, we're creating a hub where developers can contribute their specialized agents, fostering continuous improvement and evolution. This community-driven approach ensures we're always pushing towards more efficient, reliable, and cost-effective computer automation.


## **Table of Contents**
- [Overview](#overview)
- [Features](#features)
- [How It Works](#how-it-works)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [Evaluation Pipeline](#evaluation-pipeline)
- [Running the Evaluation Locally](#running-the-evaluation-locally)
- [License](#license)

---

## **Overview**

Agent Hub allows developers to submit specialized AI agents that can interact with computers in various ways. These agents can automate tasks such as:

- Web searches
- Code generation
- Command-line operations
- And more...

Once submitted, agents are automatically evaluated based on defined benchmarks and metrics, including accuracy, speed, memory usage, and robustness. The best-performing agents are showcased in a leaderboard, and the community can vote to highlight the most effective solutions for specific tasks.

---

## **Features**

- **Modular Agent System**: Agents are designed to be specialized for different tasks (e.g., web search, CLI).
- **Automatic Evaluation**: Submitted agents are automatically evaluated on predefined benchmarks.
- **Task-Specific Benchmarks**: Predefined datasets and queries for each agent type.
- **Metrics**: Evaluation based on multiple factors, such as accuracy, time-to-complete, memory footprint, and cost.
- **Open-Source**: Fully open-source and community-driven development.
- **Community Voting (Future)**: Vote for the best agents and help others discover the top performers.
- **Leaderboard (Future)**: A dynamic ranking system for agents based on their evaluation results.

---

## **How It Works**
Agent Hub breaks down complex AI interactions into specialized, efficient agents. Rather than relying on a single large model for all computer interactions, we leverage an ecosystem of purpose-built agents orchestrated by an intelligent planning system.

### Key Benefits
- **Efficiency**: Specialized agents are faster and more resource-efficient than general-purpose models
- **Cost-Effective**: Reduced token usage and computational requirements
- **Reliability**: Purpose-built agents excel at specific tasks
- **Extensible**: Community-driven development of new agents

## **Architecture**

### Solution Architecture
![Solution Architecture](docs/solution.png)


### The Orchestrator

At the heart of Agent Hub lies the Orchestrator - an intelligent system that coordinates specialized agents to accomplish complex tasks. The Orchestrator:

1. **Plans**: Breaks down user requests into atomic tasks
2. **Coordinates**: Selects and sequences appropriate agents
3. **Adapts**: Modifies plans based on execution results

Example workflow:
```python
User Query: "Build a React app that displays my photos"

# Orchestrator creates an execution plan:
plan = {
    "tasks": [
        {
            "name": "Code Generation",
            "agent": "CodeGenerator",
            "description": "Create React components for photo display"
        },
        {
            "name": "Project Setup",
            "agent": "CLIAgent",
            "description": "Initialize npm project and install dependencies"
        }
    ]
}
```

### Specialized Agents

Agents are self-contained modules designed for specific tasks:
- **CLI Agents**: Execute terminal commands
- **Code Generators**: Create and modify code
- **Web Agents**: Navigate and interact with websites
- **File System Agents**: Manage files and directories
- **Vision Agents**: Interact with graphical interfaces

Each agent:
- Has a clear, single responsibility
- Implements a standard interface
- Can be simple (function) or complex (containerized service)
- Optimizes for its specific use case

---

## **Project Structure**

```
agent-hub/
├── README.md
├── LICENSE
├── docs/
│   └── ...                    # Documentation files for contributing, using the platform
├── agent_submission/
│   ├── __init__.py
│   ├── agent_validator.py      # Validate agent submissions
│   ├── agent_submission_handler.py  # Manage agent submissions
├── evaluation/
│   ├── pipeline.py            # Main evaluation pipeline logic
│   ├── metrics/               # Metric functions (accuracy, efficiency, etc.)
│   ├── benchmarks/            # Benchmark datasets for different agent tasks
│   ├── evaluator.py           # Integrates evaluation functions and benchmarks
├── hub/
│   ├── leaderboard.py         # Displays top agents based on scores
│   ├── voting.py              # Handles community voting
│   ├── agent_directory.py     # Lists available agents in the hub
├── ci_cd/
│   ├── .github/
│   │   └── workflows/
│   │       └── evaluate-agent.yml  # CI/CD workflow to trigger evaluations
│   └── Dockerfile             # Docker environment setup for evaluations
├── scripts/
│   ├── run_evaluation.py      # Manual evaluation CLI
│   ├── setup_benchmark_data.py # Script for initializing benchmark datasets
├── data/
│   ├── web_search_benchmark.csv   # Web search dataset
│   ├── cli_benchmark.csv          # CLI benchmark dataset
│   ├── codegen_benchmark.csv      # Code generation dataset
└── requirements.txt           # Python dependencies
```

---

## **Evaluation Pipeline**

The evaluation pipeline automatically runs on every new agent submission. Here's how it works (see [detailed documentation](/docs/guidelines.md)):

1. **Agent Validation**: The agent is first validated to ensure that it follows the expected format and dependencies.
2. **Benchmark Testing**: The agent is tested against predefined task-specific benchmarks (e.g., web search queries, code generation tasks).
3. **Metrics Collection**: Several metrics are measured, including:
   - **Accuracy**: How well does the agent perform the task?
   - **Time-to-Complete**: How long does it take for the agent to complete the task?
   - **Memory Usage**: How much memory does the agent consume during execution?
   - **Cost**: If applicable, how much does the agent cost to run (e.g., token usage for LLMs)?
4. **Ranking**: The agent is ranked based on these metrics, and the results are displayed on the leaderboard.

### **Supported Benchmarks:**
- Web Search Agents
- CLI Operation Agents
- Code Generation Agents
- (More benchmarks coming soon...)

---

## **Available Agents**

We've begun populating the hub with our first set of specialized agents! While some are still in development, we're excited to share our progress.

Check out our [Current Agents Overview](docs/AGENTS.md) to:
- See what agents have already landed
- Learn about their capabilities and status
- Discover opportunities for contribution
- Find out which evaluation pipelines are ready

We're just getting started, and we're looking forward to your contributions!

---

## **DEMO**

Below is a demo of a use-case that was solved using Agent Hub.
(video coming soon)

---

## **Running the Evaluation Locally**

You can also run the evaluation pipeline locally if you want to test an agent before submitting it. Here's how to set it up:

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/agent-hub.git
   cd agent-hub
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the evaluation for an agent:
   ```bash
   python scripts/run_evaluation.py --agent <path-to-agent-directory>
   ```

4. View the results:
   The results will be saved in `evaluation/results/`, and you can view the metrics like accuracy, time, memory usage, etc.

---
## **Contributing**

We welcome contributions in several key areas:

### 1. Building and Submitting Agents

The most direct way to contribute is by creating specialized agents:

1. **Choose a Task**: Identify a specific computer interaction task
2. **Implement the Agent**
3. **Test Locally**: Use our evaluation tools
4. **Submit**: Create a pull request with your agent

#### Agent Requirements
- Clear, single responsibility
- Standard input/output interface
- Documentation and examples
- Passes evaluation metrics

For more details, see [guidelines](/docs/guidelines.md).
### 2. Evaluation Infrastructure

Help us improve how we evaluate and benchmark agents:

- **Benchmark Datasets**: Create or enhance task-specific datasets
- **Evaluation Metrics**: Develop new metrics for agent performance
- **Reward Models**: Build and train models that assess agent outputs
- **Testing Frameworks**: Improve our testing infrastructure

### 3. CI/CD Pipeline

Enhance our automation and deployment infrastructure (It's currently in the very early stages):

- **Submission Pipeline**: Improve agent validation and acceptance
- **Evaluation Pipeline**: Automate performance testing
- **Deployment Flow**: Streamline the process of pushing to the hub
- **Integration Tests**: Add comprehensive testing scenarios

Example areas:
```yaml
# GitHub Actions workflow enhancement
name: Agent Evaluation Pipeline
on:
  pull_request:
    paths:
      - 'agents/**'
      - 'evaluation/**'

jobs:
  evaluate:
    runs-on: ubuntu-latest
    steps:
      - name: Run Benchmarks
        uses: ./.github/actions/run-benchmarks
      - name: Analyze Performance
        uses: ./.github/actions/analyze-metrics
      # Your improvements here
```

### 4. Documentation and Examples

- Write tutorials and guides
- Create example implementations
- Document best practices
- Translate documentation

### 5. Core Infrastructure

- Improve the Orchestrator's planning capabilities (It's currently in the very early stages)
- Enhance inter-agent communication
- Optimize resource usage
- Add new features to the hub

### Getting Started with Contributing

1. **Fork the repository**
2. **Choose your focus area** from the above categories
3. **Check existing issues** or create a new one describing your planned contribution
4. **Submit a PR** following our contribution guidelines

### Contribution Guidelines

- Follow our coding standards
- Include tests for new features
- Update relevant documentation
- Add your changes to the CHANGELOG


---
## **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


