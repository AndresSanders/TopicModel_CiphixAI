from data_manipulations.help_functions_preprocessing import remove_links_mentions_specialcharacters


def data_cleaning(conversations):
    cleaned_conversations = []
    for conversation in conversations:
        cleaned_conversation = remove_links_mentions_specialcharacters(conversation)
        cleaned_conversations.append(cleaned_conversation)
    return cleaned_conversations
