**LangGraph is specifically designed for complex work flows:**

1) Branching Logic: Node(if not) -> Next Node(if not) -> Next Node -> Final response
2) FallBack Mechanism: If flow can't answers Users question, It will go to Human agent or next more about users query
3) Multi-Step Decision: In the Workflow, it will do multiple steps before answering question. 

***Main Components:***
1) Node
2) Edge
3) State
4) State Machine : It will choose the path of the workflow based on State after every node responses

**Example**
state = {
"messages" : [{"role": "user", "content": "what are the top products"},
{"role": "db_query_tool", "content": "I couldnt find the products"}
]
}


