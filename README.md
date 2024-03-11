# PDF-GPT
## What is it
PDF-GPT allows you to feed an input of a pdf document and then QA with a GPT-4 model. PDF-GPT outputs the tokens via streaming will only use information in the document or relevant to the information in the document
## How does it work
PDF-GPT is built using Langchain and PyPDFLoader. Using Langchain, we created a chain that contained a prompt, retriver and llm. Moreover, we allowed the user to continuously ask questions to the chat using a while loop until the user is done with the program. 
## Why did I make this 
I made it for my own personal use because I do not have ChatGPT-Plus and I do not think it is worth it for me to pay 20 dollars a month, I also planned to use this to interact with larger textbooks. Furthermore, I was interested in making a project using LangChain and thought this was a great project to start with. 
## What I plan to add
Make it so I can use larger files, probably will use pinecone for vectorstores. Add a better ui instead of just terminal-based, create a more indepth prompt for better results. 
## Example
![image](https://github.com/SabienNguyen/pdf-gpt/assets/32147674/5362a6b4-8049-4d17-aad8-5bad0fb382fb)
## Use
Add .env file with openai api keys
```ex: OPENAI_API_KEY="XXXXXXXXXXXXXXXXX"```

```
python pdf_gpt.py
```

