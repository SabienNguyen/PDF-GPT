from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain.chains import RetrievalQA
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv, find_dotenv
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import PyPDFLoader


# Load variables from the .env file
load_dotenv(find_dotenv())
document_input = input("give a pdf file path\n")
loader = PyPDFLoader(document_input)
pages = loader.load_and_split()

vector = FAISS.from_documents(pages, OpenAIEmbeddings())


llm = ChatOpenAI(model='gpt-4', streaming=True, callbacks=[StreamingStdOutCallbackHandler()])
parser = StrOutputParser()
template = """You are a world class teacher. Only answer using the information given in the document or information relevant to the the information in the document, if information is not in document say that information is not present in document.
Context: {context}
Question: {question}
Answer: """
prompt = PromptTemplate(template=template, input_variables=['question'])
chain = prompt | llm | parser
retriever = vector.as_retriever()
qa = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    chain_type_kwargs={"prompt": prompt},
    retriever=retriever,
)

while True: 
    inp = input("ask a question or type \"quit\" to exit program\n")
    if inp == "quit":
        break
    qa.invoke(inp)
    print()