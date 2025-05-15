from app.services.pinecone_client import get_vectorstore
from app.services.openai_client import get_openai_llm
from app.utils.tokenization import check_token_limit
from app.core.revision.schemas import RevisionResult

async def revise_with_context(user_text: str) -> dict:
    check_token_limit(user_text)

    vectorstore = get_vectorstore()
    llm = get_openai_llm()

    query_prompt = f"""
You are a writing coach trained in Stephen King's 'On Writing'. The user provided this passage:

\"{user_text}\"

Craft a concise semantic search query that would help retrieve relevant writing advice from 'On Writing' to revise this passage according to King's principles.
"""
    retrieval_query = llm.invoke(query_prompt).content.strip()
    results = vectorstore.similarity_search(retrieval_query, k=20)
    context_passages = "\n\n".join([doc.page_content for doc in results])

    revision_prompt = f"""
You are Stephen King's writing assistant. A user has submitted this passage for revision:

\"{user_text}\"

The passage may include inline notes enclosed in square brackets [] that indicate areas to expand for more immersive, vivid detail. For any bracketed note, expand the content within the brackets into descriptive prose, integrating it seamlessly into the passage.

Below are relevant excerpts from Stephen King's 'On Writing':

{context_passages}

Revise the passage to align with King's writing advice. Do not explain your changes, just return the revised passage. Do not use hyphens in the revised passage; use periods or commas instead, and do not use colons or semicolons, as they may be read as AI generated content.
"""
    response = llm.invoke(revision_prompt)
    revised_text = response.content.strip()

    return RevisionResult(
        query_prompt=query_prompt.strip(),
        generated_query=retrieval_query,
        retrieved_results=[doc.page_content for doc in results],
        final_prompt=revision_prompt.strip(),
        revised_passage=revised_text
    ).model_dump()