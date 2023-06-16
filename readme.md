# TotemAPI

TotemAPI is a Python-based application that provides a solution for converting any book or online text into accessible data through an API. It essentially functions as a library, but in the form of an API, allowing users to seamlessly transform PDFs, text files, or even links into an API without encountering any difficulties.

## CURRENT INFO:

The project is in very ealy stages, currently I'm working on the ingestor. I will be perfecting the ingestor using LLM and other methods, such as directly writing new code for it.

Why is it important to focus on the ingestor? I want to be able to have good quality convesion from text files to the LLM accessible files. For this to happen focusing on the ingestor is key.

You can currently test the ingestor that is just a basic LangChain implementation.

I added a Querry-Chat-to-PDF bot so you can play with the data from the ingestor. Enojoy! 🥹


### 1. Building a Text Ingestor

The first step involves building a text ingestor module. This module is responsible for extracting the content from various sources, such as PDFs, text files, or online links, and converting it into a readable format. This process ensures that the extracted text can be further processed and utilized within the API.

### 2. Build Cell String

The second step focuses on constructing a cell string. A cell string is an intermediate data structure that organizes the extracted text into manageable units, such as paragraphs, chapters, or sections. This step facilitates easy navigation and retrieval of specific information within the API.

### 3. Build the API

The final step is to construct the API itself using FastAPI, a Python web framework designed for building APIs with high performance and simplicity. In this step, the cell string generated in the previous step is used to create endpoints that allow users to access the transformed text data. These endpoints can be utilized to search for specific content, retrieve sections, or perform other desired operations on the text.



