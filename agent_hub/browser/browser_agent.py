from browser_use import Agent as BrowserAgent
from agent_hub.agent import Agent as BaseAgent, AgentTask, AgentInput
from pydantic import Field

from langchain_mistralai import ChatMistralAI
from agent_hub.state import State
from agent_hub.plan import TaskStatus
import asyncio

class BrowserUseInput(AgentInput):
    """Input schema for browser operations."""
    query: str = Field(
        description="browser operation to perform"
    )

class BrowserUse(BaseAgent):
    def __init__(self):
        description = """An agent that allows AI agents to browse the web in fast and efficient way just like a human.
        The agent is independent and able to perform browsing tasks.
        It can handle complex queries that require multiple steps to complete. Don't give too granular queries. Give a high level query."""
        name = "BrowserUse"
        task = AgentTask.WEB_BROWSER
        super().__init__(name, description, task)

    async def setup(self):
        """Initialize the browser agent with Mistral LLM."""
        
        print("BrowserUse is ready")

    def __call__(self, state: State):
        browse_input = BrowserUseInput(**state["next_agent_input"])
        print(f"Sync BrowserUse is calling the available agents for the task: {browse_input}")
        try:
            browser_agent = BrowserAgent(
                task=browse_input.query,
                llm=ChatMistralAI(model="pixtral-large-latest")
            )
            
            result = asyncio.run(browser_agent.run())
            return {
            "last_task_status": TaskStatus.SUCCESS,
                "last_task_output": result
            }
        except Exception as e:
            print(f"Error executing task: {browse_input.query}. Error: {e}")
            return {
                "last_task_status": TaskStatus.FAILURE,
                "last_task_output": f"Error executing task: {browse_input.query}. Error: {e}"
            }
        
        

    async def __acall__(self, state: State, **kwargs) -> str:
        browse_input = BrowserUseInput(**state["next_agent_input"])
        print(f"Async BrowserUse is calling the available agents for the task: {browse_input}")
        try:
            browser_agent = BrowserAgent(
                task=browse_input.query,
                llm=ChatMistralAI(model="pixtral-large-latest")
            )
            
            result = await browser_agent.run()
            return {
                "last_task_status": TaskStatus.SUCCESS,
                "last_task_output": result
            }
        except Exception as e:
            print(f"Error executing task: {browse_input.query}. Error: {e}")
            return {
                "last_task_status": TaskStatus.FAILURE,
                "last_task_output": f"Error executing task: {browse_input.query}. Error: {e}"
            }
        
    def define_input_schema(self) -> type[BrowserUseInput]:
        return BrowserUseInput