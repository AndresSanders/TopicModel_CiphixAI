from bertopic import BERTopic
from bertopic.representation import OpenAI
from bertopic.vectorizers import ClassTfidfTransformer
import openai
import functions
import Constants
import plotly


"""Read Data"""

csvFilepath = "Data/TwitterExport/data.csv"
rows = functions.read_csv_file(csvFilepath)
conversations = functions.generate_conversations_quotes(rows, False)
print(len(conversations))
conversations = conversations[:100000]  # Limit to 100k conversations for testing

"""Data Cleaning"""

cleaned_conversations = functions.datacleaning(conversations)  # Remove links, mentions, specialcharacters, etc.
english_conversations = functions.filter_english_conversations(cleaned_conversations)  # keep only english conversations

"""Topic Modeling"""

openai.api_key = Constants.API_KEY_OpenAI # Set OpenAI API key
ctfidf_model = ClassTfidfTransformer(reduce_frequent_words=True) # Reduce the impact of frequent words
topic_model = BERTopic(embedding_model="all-MiniLM-L6-v2", ctfidf_model=ctfidf_model,representation_model=OpenAI())
topics, probs = topic_model.fit_transform(english_conversations)
print(topic_model.get_topic_info())
topic_model.save("Data/Models/bertopic&OpenAI_model")
fig = topic_model.visualize_topics()
plotly.offline.plot(fig, filename='topic_model.html')
