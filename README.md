# Sentiment-Analysis-Stock-Links

This project utilizes Google Gemini's Large Language Model (LLM) and Langchain framework for sentiment analysis. It offers a streamlined web application interface powered by Streamlit. The main functionality of the project involves taking user input as keywords, extracting relevant URLs from the past 1 day, performing sentiment analysis on the content of these URLs, and presenting the overall sentiment as positive or negative.

## Features

- **Keyword Input:** Users can input keywords relevant to the topic they want to analyze.
- **URL Extraction:** The system automatically extracts URLs from the web containing content related to the provided keywords within the past 1 day.
- **Sentiment Analysis:** Google Gemini's LLM and Langchain framework are employed to analyze the sentiment of the content extracted from the URLs.
- **Display Results:** The application displays the overall sentiment analysis result, indicating whether the sentiment is positive or negative.

## Technologies Used

- **Google Gemini LLM:** Leveraging Google's powerful Large Language Model for advanced natural language processing tasks.
- **Langchain Framework:** Providing a framework for integrating language models into various applications.
- **Streamlit:** Used for developing the user-friendly web application interface.
- **Python:** The primary programming language used for development.

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/omkarfirame/Sentiment-Analysis-Stock-Links.git
   ```

2. Navigate to the project directory:

   ```
   cd sentiment_analysis_stock_links
   ```

3. Install dependencies:

   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the Streamlit application:

   ```
   streamlit run app.py
   ```

2. Access the application through the provided URL in your browser.

3. Input keywords relevant to the topic you want to analyze.

4. Wait for the application to process and display the sentiment analysis results.

## Contributing

Contributions are welcome! If you find any bugs or have suggestions for improvements, feel free to open an issue or submit a pull request.

## Acknowledgments

- Thanks to Google for providing Gemini LLM.
- Special thanks to the developers of Langchain framework.
- Streamlit developers for creating an excellent tool for building web applications with Python.
