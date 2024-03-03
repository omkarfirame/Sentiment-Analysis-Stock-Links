import streamlit as st
from sentiment_analysis_stock_links.component.model import SentimentAnalyzer
from sentiment_analysis_stock_links.component.webscrapper import WebScraper
from langchain.document_loaders import WebBaseLoader
import asyncio

async def main():
    st.title("Web Sentiment Analyzer")
    
    input_text = st.text_input("Enter a keyword:")
    if st.button("Analyze Sentiment"):
        web_scraper = WebScraper()
        await web_scraper.ddg_search(input_text=input_text,max_results=5)
        response = web_scraper.do_webscraping(json_file="ddgs.json")

        url_list = [x['url'] for x in response]
        model = SentimentAnalyzer.analyze_sentiment()

        result_list = []
        for url in url_list:
            try:
                loader = WebBaseLoader(url)
                docs = loader.load()
                res = model.invoke(docs)
                result_list.append(res)
            except:
                pass

        final_res = [x for x in result_list if 'irrelevant text' not in x.lower()]

        positive_count = final_res.count('Positive')
        negative_count = final_res.count('Negative')

        # Calculate total count
        total_count = len(final_res)

        # Calculate percentages
        if total_count != 0:
            positive_percentage = (positive_count / total_count) * 100
            negative_percentage = (negative_count / total_count) * 100
        else:
            positive_percentage = 0.0
            negative_percentage = 0.0
            


        st.write("Sentiment analysis results:")

        if positive_percentage == 100.0:
            st.write("The sentiment of the content related to your keyword is predominantly positive.")
        elif negative_percentage == 100.0:
            st.write("The sentiment of the content related to your keyword is predominantly negative.")
        elif (positive_percentage < 100.0) and (negative_percentage < 100.0):
            st.write(f"The sentiment analysis indicates that {positive_percentage}% of the content related to your keyword is positive, while {negative_percentage}% is negative")
        elif (positive_percentage == 0.0) and (negative_percentage == 0.0):
            st.write("No relevant press statement found")
        st.write("---")


if __name__ == "__main__":
    asyncio.run(main())
