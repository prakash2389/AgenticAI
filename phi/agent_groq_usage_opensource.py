!pip install phidata
!pip install Groq

from phi.agent import Agent
from phi.model.groq import Groq

agent = Agent(
    # model = Groq(id="llama-3.1-8b-instant", api_key="******************")
    model = Groq(id="deepseek-r1-distill-llama-70b", api_key="******************")
)

res = agent.print_response("Write a Poem on Pawan kalyan and CHiranjeevi?")
