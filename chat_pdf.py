from dotenv import load_dotenv
load_dotenv()

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate


#  1) Load PDF
file_path = "./Pritika-Shukla .pdf"
loader = PyPDFLoader(file_path)
document = loader.load()

#  2) Split into chunks
text_splitter = CharacterTextSplitter.from_tiktoken_encoder(
    encoding_name="cl100k_base",
    chunk_size=800,
    chunk_overlap=150
)
texts = text_splitter.split_documents(document)

#  3) Embeddings + Vector DB
embeddings = OpenAIEmbeddings()

vectorstore = Chroma.from_documents(
    documents=texts,
    embedding=embeddings,
    persist_directory="./chroma_db"
)

print("✅ Stored chunks:", vectorstore._collection.count())

# ✅ 4) Prompt + LLM
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a PDF assistant. Answer ONLY using the given context from the PDF. If not found, say: Not mentioned in the PDF."),
    ("human", "Question: {question}\n\nContext:\n{context}")
])

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
chain = prompt | llm


print("\n✅ PDF Live Chat started (type 'exit' to stop)\n")

while True:
    query = input("You: ")
    if query.lower() == "exit":
        break

    docs = vectorstore.similarity_search(query, k=3)
    context = "\n\n".join([d.page_content for d in docs])

    answer = chain.invoke({"question": query, "context": context})

    print("\nBot:", answer.content)
    print()
