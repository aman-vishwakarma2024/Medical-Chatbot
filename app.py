# importing all the required libraries
from flask import Flask, render_template, jsonify, request
from src.helper import download_hugging_face_embeddings
from langchain_pinecone import PineconeVectorStore
from langchain_openai import OpenAI
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
# import my prompt
from src.prompt import *
import os

# initiating flask
app = Flask(__name__)

# load api keys from .env file
load_dotenv()

PINECONE_API_KEY=os.environ.get('PINECONE_API_KEY')
OPENAI_API_KEY=os.environ.get('OPENAI_API_KEY')

os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

# download hugging face embeddings
embeddings = download_hugging_face_embeddings()

# create pinecone index
index_name = "medicalbot"

# Embed each chunk and upsert the embeddings into your Pinecone index.
docsearch = PineconeVectorStore.from_existing_index(
    index_name=index_name,
    embedding=embeddings
)

retriever = docsearch.as_retriever(search_type="similarity", search_kwargs={"k":3})

#set my llm model
llm = OpenAI(temperature=0.4, max_tokens=500)
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{input}"),
    ]
)

# create the chain
question_answer_chain = create_stuff_documents_chain(llm, prompt)
rag_chain = create_retrieval_chain(retriever, question_answer_chain)

# setting up two default route
# route 1: shows the chat interface
@app.route("/")
def index():
    return render_template('chat.html')

# route 2: accept the user msg and pass it to llm model
@app.route("/get", methods=["GET", "POST"])
def chat():
    # accept the user msg
    msg = request.form["msg"]
    input = msg
    print(input)
    # pass the user msg to chain
    response = rag_chain.invoke({"input": msg})
    #print the response
    print("Response : ", response["answer"])
    return str(response["answer"])


# main driver function, executing the app will be running in the localhost at port 8080
if __name__ == '__main__':
    app.run(host="0.0.0.0", port= 8080, debug= True)
