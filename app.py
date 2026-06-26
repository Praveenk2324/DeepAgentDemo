import streamlit as st

code = """test_prompt = 'What is the current stock price of Apple (AAPL) today?'

result = deepagent.invoke({'messages':[{"role":'user', 'content':test_prompt}]})
print(result)"""

st.code(code, language='python')