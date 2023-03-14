import csv
import re
from langdetect import detect

"""opens the csv datafile data.csv"""


def read_csv_file(csvFilepath):
    rows = []
    with open(csvFilepath, 'r', encoding="utf-8") as csvFile:
        csvreader = csv.reader(csvFile, quoting=csv.QUOTE_NONE, delimiter='\n')
        for row in csvreader:
            if len(row) == 1:
                rows.append(row[0])
    return rows


"""Splits the datafile into conversations based on the fact that each conversation/Topic ends with a line 
surrounded by quotation marks"""


def generate_conversations_quotes(rows, is_test):
    conversations = []
    current_conversation = " "
    if is_test:
        for row in rows:
            if row[0] == '"':
                current_conversation += row
                conversations.append(current_conversation)
                current_conversation = " "
                if len(conversations) == 10:
                    return conversations
            else:
                current_conversation += row
                current_conversation += "\n"

    else:
        for row in rows:
            if row[0] == '"':
                current_conversation += row
                conversations.append(current_conversation)
                current_conversation = " "
            else:
                current_conversation += row
                current_conversation += "\n"

    return conversations


"removes all https links, @mentions and special characters"


def datacleaning(conversations):
    cleaned_conversations = []
    for conversation in conversations:
        cleaned_conversation = remove_links_mentions_specialcharacters(conversation)
        cleaned_conversations.append(cleaned_conversation)
    return cleaned_conversations


def remove_links_mentions_specialcharacters(conversation):
    no_links = re.sub(r"http\S+", r"", conversation)
    no_mentions = re.sub(r"@\S+", r"", no_links)
    no_specialchar = re.sub(r"[^a-zA-Z0-9’]+", r" ", no_mentions)

    return no_specialchar


"""This function filters out all conversations that are not in English"""


def filter_english_conversations(conversations):
    english_conversations = []
    for conversation in conversations:
        try:
            language = detect(conversation)  # Detect the language of the conversation
            if language == "en":  # Check if the language is English
                english_conversations.append(conversation)  # If it's English, add it to the filtered collection
        except:
            pass
    return english_conversations


"""This function writes each conversation to separate text files in the folder 
Data/Conversations"""


def write_conversations_to_textfiles(conversations):
    for conversation in conversations:
        conversation_number = conversations.index(conversation)
        conversation_filepath = "Data/Conversations/conversation" + str(conversation_number) + ".txt"
        print(conversation_filepath)
        with open(conversation_filepath, 'w') as conversationFile:
            for line in conversation:
                conversationFile.write(line)
