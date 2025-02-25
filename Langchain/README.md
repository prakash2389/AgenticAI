Upload Agentic AI files from Langchain


from langchain_community.tools.ddg_search import DuckDuckGoSearchRun

Search_tool = Tool(
    name = "DuckDuckGo Search",
    func=DuckDuckGoSearchRun().run,
    description="useful for when you need to answer questions about current events"
)

agent = initialize_agent(llm=OpenAI(temperature=0, api_key = openai_api_key),
                 tools=[Search_tool],
                 agent="zero-shot-react-description",
                 verbose=True)

response = agent.run("Who won Pak vs India Cricket Match Today(23/2/2025)? What is score of Virat Kohli?")
