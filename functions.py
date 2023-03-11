import csv


"""This fuctions opens the datafile data.csv"""
def read_csv_file(csvFilepath):
    rows = []
    with open(csvFilepath, 'r') as csvFile:
        csvReader = csv.reader(csvFile, quoting=csv.QUOTE_NONE, delimiter='\n')
        for row in csvReader:
            if len(row) == 1:
                rows.append(row[0])
    return rows






"""This function splits the datafile into conversations based on the fact that each conversation ends with a line surrounded by quotation marks"""
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

"""This function writes each conversation in the list conversations to seperate text files in the folder Data/Conversations"""
def write_conversations_to_textfiles(conversations):
    for conversation in conversations:
        conversation_number = conversations.index(conversation)
        conversation_filepath = "Data/Conversations/conversation" + str(conversation_number) + ".txt"
        print(conversation_filepath)
        with open(conversation_filepath, 'w') as conversationFile:
            for line in conversation:
                conversationFile.write(line)




