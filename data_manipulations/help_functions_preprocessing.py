import csv
import re
from langdetect import detect
from typing import List
from pathlib import Path


def read_csv_file(csvfilepath: Path) -> List[str]:
    rows = []
    with open(csvfilepath, 'r', encoding="utf-8") as csvfile:
        csvreader = csv.reader(csvfile, quoting=csv.QUOTE_NONE, delimiter='\n')
        for row in csvreader:
            if len(row) == 1:
                rows.append(row[0])
    return rows


"""Splits the datafile into conversations based on the fact that each conversation/Topic ends with a line 
surrounded by quotation marks"""


def generate_conversations_quotes(rows: List[str], is_test: bool) -> List[str]:
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


def remove_links_mentions_specialcharacters(conversation: str) -> str:
    no_links = re.sub(r"http\S+", r"", conversation)
    no_mentions = re.sub(r"@\S+", r"", no_links)
    no_specialchar = re.sub(r"[^a-zA-Z0-9’]+", r" ", no_mentions)

    return no_specialchar


"""This function filters out all conversations that are not in English"""


def filter_english_conversations(conversations: List[str]) -> List[str]:
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
def write_conversations_to_textfiles(conversations: List[str]) -> None:
    for conversation in conversations:
        conversation_number = conversations.index(conversation)
        conversation_filepath = Path("Data/Conversations/conversation" + str(conversation_number) + ".txt")
        print(conversation_filepath)
        conversation_filepath.write_text(conversation)
