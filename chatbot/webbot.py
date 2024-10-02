from utils import store_docs, get_chroma_client, make_chain

store_docs("https://www.anaadi.org/post/teaching-ayurveda-to-children")

vector_store = get_chroma_client()
lis = vector_store.get(include=['embeddings','metadatas','documents'])
print("Number of documents:",len(lis['documents']))
print("Content:\n",lis['documents'][1])
print("\n\nMetadata:", lis['metadatas'][1])
print("\n\nEmbeddings:", "Length:", len(lis['embeddings'][1]),"\nEmbedding Vector:",lis['embeddings'][1])


chat_history = ""
chain = make_chain()
question = input("Enter your question\n")
print(question)
result = chain.invoke({"input": question})

answer = result.get("answer")
print("Answer")
print(answer)

