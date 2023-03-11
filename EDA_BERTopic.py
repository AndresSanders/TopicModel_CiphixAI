from bertopic import BERTopic
import csv
import functions
import pandas as pd

csvFilepath = "Data/TwitterExport/data.csv"
rows = functions.read_csv_file(csvFilepath)
conversations = functions.generate_conversations_quotes(rows, False)
print(len(conversations))

conversations = conversations[:1000]

topic_model = BERTopic(embedding_model="all-MiniLM-L6-v2")
topics, probs = topic_model.fit_transform(conversations)
topic_model.
print(topic_model.get_topic_info())
print(topic_model.)