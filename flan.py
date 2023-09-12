#This app is used to taste Google LLM FLAN
pip install langchain

pip install huggingface_hub

import os

os.environ["HUGGINGFACEHUB_API_TOKEN"] = ""

from langchain.llms import HuggingFaceHub

llm = HuggingFaceHub(repo_id = "google/flan-t5-large")

our_query = "How to boot Linux Operating System?"
completion = llm(our_query)

print(completion)

