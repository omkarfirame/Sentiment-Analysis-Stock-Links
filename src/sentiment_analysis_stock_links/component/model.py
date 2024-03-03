from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.schema import StrOutputParser
from langchain.schema.prompt_template import format_document
from langchain_core.runnables import RunnablePassthrough
from langchain.document_loaders import WebBaseLoader


class SentimentAnalyzer:
    def __init__(self):
        pass

    def analyze_sentiment():
        """
        function return a chain which can generate sentiment
        """
        
        prompt_template = """
        Given a context and a keyword, analyze the sentiment of the context if it's related to the keyword.
        If the context is irrelevant to the keyword, return 'Irrelevant text'.
        If relevant, determine whether the sentiment is positive or negative.

        Context: \n {context} \n
        Keyword: \n {keyword} \n

        Answer: 

        Note: Answer must be either "Positive" or "Negetive" or ""Irrelevent Text"
        """
        doc_prompt = PromptTemplate.from_template("{page_content}")
        llm_prompt = PromptTemplate.from_template(prompt_template)

        print(llm_prompt)
        llm = ChatGoogleGenerativeAI(model="gemini-pro",
                        temperature=0.7, top_p=0.85)
        

        stuff_chain = (
            # Extract data from the documents and add to the key `text`.
            {
                "context": lambda docs: "\n\n".join(
                    format_document(doc, doc_prompt) for doc in docs
                ),
                "keyword": RunnablePassthrough()

            }
            | llm_prompt         # Prompt for Gemini
            | llm                # Gemini function
            | StrOutputParser()  # output parser
        )

        return stuff_chain