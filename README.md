# Medical-Chatbot
Techstack used:
- Python
- Langchain
- OpenAI
- Pinecone
- Flask

Steps
 1. Create virtual environments
 2. write and install requirements.txt
 3. create folder structure
 4. Creating setup.py (setting this folder as local package so that I can import src module and files )
 5. Doing notebook experiment in jupyter notebook (see trials.ipynb)
    1. make sure that I am in root directory else I will get path issues error
    2. Uplaod pdf data
    3. convert data into chunks
    4. chunks into vector and store in pinecone database by creating a pincone index
    5. create llm
    6. run query and get answer

6. Now I will perform modular coding 
   1. [helper.py in src]inside helper.py write all the helper function like upload pdf, create chunks, download the huggingfacehubembeddings
   2. write prompt in [prompt.py]
   3. create store_index.py [in future i might need to update my source data, pdf and create vector and then store in knowledgbase]
   4. Now I need to create main function [app.py] for this first need to write htms and css code, flask
      since I am using flask I need to create templates/chat.html and static/style.css and I am coping the frontend code from website
   5. write [app.py] codes, integrate all the functions

