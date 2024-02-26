# flask_Wrapper_Custom_RAG_Pipeline_Llama_2
 A Flask-based REST API serves a customized RAG pipeline powered by the Llama 2 LLM model.

# Running this service as a Docker Container
 ## docker run command - 
    sudo docker run -d --runtime=nvidia --gpus all -p 8502:8502 --name {container_name} {image_name}

 ### <b>NOTE:</b> If you have downloaded the Llama 2-7b-chat-hf locally, update the config.py file according to the comments in that script.

# RESTAPI Implementation -
For API implementation, I have used RESTAPI which is implemented using Flask. There are 2 methods exposed -

GET - gives information about the service
POST - takes JSON input in the form of - '{"input_string": "User's Query"}' and gives custom RAG LLM model JSON output in the form of - {"processed_string":Model's ouptut"}
