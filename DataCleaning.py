import functions



csvFilepath = "Data/TwitterExport/data.csv"
rows = functions.read_csv_file(csvFilepath)
conversations = functions.generate_conversations_quotes(rows, False)
print("Amount of conversations found =", len(conversations))
conversations = conversations[:1000]
cleaned_conversations = functions.datacleaning(conversations)
english_conversations = functions.filter_english_conversations(cleaned_conversations)

functions.write_conversations_to_textfiles(english_conversations[:10])



