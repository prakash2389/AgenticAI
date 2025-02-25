

**CrewAI**
A crew in crewAI represents a collaborative group of agents working together to achieve a set of tasks. Each crew defines the strategy for task execution, agent collaboration, and the overall workflow.

*Agents:*

**Agentic AI Trip  planner:**

Lets plan trip and do couple of below things
1) Flight Booking Agent
2) Hotel Recommendation Agent
3) Food Suggestion AGnet
4) Sight Seeing Agent
5) Currency Converions Agent

All Agents can be interconnected, and grouped under one agent


1 <---> 2
1 <---> 3
2 <---> 3
1 <---> 4
2 <---> 4 ...............


Once we have all agents, App can guide each agent to give suggest, take decison and also act on it.


**AI Custom CHatbot**

In a office, in chatbot, if user has to redirect the query to respective department, then chatbot can do

1) Operation Agent
2) Insurance Agent
3) HR Agent
4) Security Agent


Each Crew Agent has
1) **Name**
2) **Role**
3) **Goal**
4) **Backstory**
5) **Model(LLM)**
6) **Tools(APIs, Databases)**


**news_scrapper_agent** = Agent (
            
            name = "News_Scrapper",
            
            role = "web crawler",
            
            goal = "Fetch latest news from internet",
            
            backstory = "An expert in web crawling ans retrieving news articles",
            
            llm= ChatOpenAI(model_name="gpt-04"),
            
            tools=[news_scrapper_tool]
            
            )







1) Task: Fetch News
2) Assigned Agent: News Scrapper Agent
3) Process:  Step 1 (STart)



1) **Sequential Execution** of above three steps for each Task
2) **Parallel Execution** of above three steps for each Task



**Knowledge**
What is knowledge in CrewAI and how to use it.

​
**What is Knowledge?**
Knowledge in CrewAI is a powerful system that allows AI agents to access and utilize external information sources during their tasks. Think of it as giving your agents a reference library they can consult while working.



