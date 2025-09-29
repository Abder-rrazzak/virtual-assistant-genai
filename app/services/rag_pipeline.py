from app.services.llm_client import get_llm
from app.services.vectorstore import get_vectorstore
from app.services.memory import save_message, load_conversation

async def generate_response(session_id: str, query: str):
    llm = get_llm()
    vectorstore = get_vectorstore()

    # Retrieve docs
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
    docs = retriever.get_relevant_documents(query)

    context = "\n".join([d.page_content for d in docs])
    sources = [d.metadata.get("source", "unknown") for d in docs]

    # Format prompt
    prompt = f"""
    You are a helpful AI assistant.
    Context:
    {context}

    User: {query}
    Answer with citations.
    """

    response = llm.predict(prompt)

    save_message(session_id, "user", query)
    save_message(session_id, "assistant", response)

    return response, sources, 0.85  # TODO: compute confidence dynamically
