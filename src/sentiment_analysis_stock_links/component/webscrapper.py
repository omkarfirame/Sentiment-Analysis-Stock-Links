from duckduckgo_search import DDGS
import json
import html2text
from langchain.document_loaders import AsyncHtmlLoader
from langchain.document_transformers import Html2TextTransformer
import os
import asyncio

class WebScraper:
    def __init__(self):
        pass
    
    async def ddg_search(self, input_text, max_results=None):
        """
        parameter: input_text is a keyword to search
        The function fetch all the url related to given text and saves in json format
        """
        file_path = "ddgs.json"
        if os.path.exists(file_path):
            # Delete the file
            os.remove(file_path)
            print("File deleted successfully.")
        else:
            print("File does not exist.")

        await asyncio.sleep(1)
        with DDGS() as ddg:
            results = [r for r in ddg.text(f"{input_text}", safesearch="off", timelimit="d", max_results=max_results)]
        
        # Write list of dictionaries to JSON file
        with open(file_path, "w") as json_file:
            json.dump(results, json_file)
            print("file created successfully")

    def do_webscraping(self, json_file):
        """
        parameter: it takes json file
        returns a list of dictionaries including page content, title, metadata and clean text of the urls
        """
        with open(f"{json_file}", "r") as json_file:
            data_list = json.load(json_file)

        urls = [x['href'] for x in data_list]

        structured_response = []
        for url in urls:
            try:
                loader = AsyncHtmlLoader(url)
                docs = loader.load()

                html2text_transformer = Html2TextTransformer()
                docs_transformed = html2text_transformer.transform_documents(docs)

                if docs_transformed is not None and len(docs_transformed) > 0:
                    metadata = docs_transformed[0].metadata
                    title = metadata.get('title', '')

                    structured_response.append({
                        'summary': docs_transformed[0].page_content,
                        'title': title,
                        'metadata': metadata,
                        'url': url
                    })
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
                continue
        
        return structured_response

