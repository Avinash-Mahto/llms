#This app is used to taste Google LLM FLAN

# Install langChain framework.
pip install langchain

# Install HuggingFace Library.
pip install huggingface_hub

# Define Access_TOKEN.
import os
os.environ["HUGGINGFACEHUB_API_TOKEN"] = ""

# Import HuggingFace Class from llm module and Langchain Library.
from langchain.llms import HuggingFaceHub

# Define the particular LLM class from HuggingFace repo to perform query.
llm = HuggingFaceHub(repo_id = "google/flan-t5-large")

# Take our_query is a prompt "input" and  completion as a "output"
our_query = "How to boot Linux Operating System?"
completion = llm(our_query)

# Print the output
print(completion)

