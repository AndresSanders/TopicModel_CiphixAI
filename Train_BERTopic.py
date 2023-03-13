from bertopic import BERTopic
import openai
from bertopic.representation import OpenAI

import functions
import pandas as pd
import plotly

"""Read Data"""
openai.api_key = "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"
csvFilepath = "Data/TwitterExport/data.csv"
rows = functions.read_csv_file(csvFilepath)
conversations = functions.generate_conversations_quotes(rows, False)
print(len(conversations))
conversations = conversations[:1000]  # Limit to 100k conversations for testing

"""Data Cleaning"""

cleaned_conversations = functions.datacleaning(conversations)  # Remove links, mentions, specialcharacters, etc.
english_conversations = functions.filter_english_conversations(cleaned_conversations)  # keep only english conversations

"""Topic Modeling"""

topic_model = BERTopic(embedding_model="all-MiniLM-L6-v2", representation_model=OpenAI())
# Bertopic english model
topics, probs = topic_model.fit_transform(english_conversations)
print(topic_model.get_topic_info())
topic_model.save("Data/Models/Test_bertopic&OpenAI_model")
fig = topic_model.visualize_topics()
plotly.offline.plot(fig, filename='topic_model.html')
