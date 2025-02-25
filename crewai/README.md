

**CrewAI**

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


Task: Fetch News

Assigned Agent: News Scrapper Agent

Process:  Step 1 (STart)





