import streamlit as st
from langchain_core.messages import HumanMessage
from agent_hub.graph import graph
from PIL import Image

st.set_page_config(layout="wide")
# Set up the Streamlit layout with two columns
col1, col2 = st.columns([1, 1])

# Main content area
with col1:
    st.title("Agent Hub Demo")
    
    # Display the mermaid graph visualization
    mermaid_image = Image.open("docs/mermaid_graph.png")
    st.image(mermaid_image, caption="Agent Hub Graph Visualization", use_column_width=True)
    
    # Text input for user query
    user_input = st.text_input("Enter your query:", 
                              "Can you check the weather in Paris (use the web search agent) and then write the results to a file called weather.txt?")
    
    # Button to execute
    if st.button("Run"):
        with st.spinner("Processing..."):
            # Invoke graph with user input
            result = graph.invoke({
                "messages": [HumanMessage(content=user_input)], 
                "user_input": user_input
            })
            st.session_state.result = result
            # Display final output
            st.header("Final Output")
            st.write(result["messages"][-1].content)

# Side panel for logs
with col2:
    st.header("Execution Logs")
    
    # Create an expandable section for full result details
    with st.expander("Full Execution Details", expanded=True):
        if "result" in st.session_state:
            result = st.session_state.result
            plan = result["plan"]
            st.write("### Plan")
            st.json(plan.model_dump())  # Use model_dump() instead of model_dump_json()
            st.markdown("--------------------------------")
            st.write("### Previous Outputs")
            previous_outputs = result.get("previous_outputs", [])
            for output in previous_outputs:
                st.write(output)
            st.write("*" * 50)
