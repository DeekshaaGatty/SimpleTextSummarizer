
# IMPORTING LIBRARIES:
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize


# READING TEXT TO SUMMARIZE FROM FILE:
file_name=input("ENTER THE FILE NAME TO SUMMARIZE:\n")
file1=open(file_name,"r")
text=file1.read()
print("\n\nBEFORE SUMMARIZING:\n\n"+text+"\n\n\n")

# TOKENIZING THE TEXT:
stop_words = set(stopwords.words("english"))
words = word_tokenize(text)

# CREATING A FREQUENCY TABLE TO KEEP THE SCORE OF EACH WORD:
freq_table = dict()
for word in words:
	word = word.lower()
	if word in stop_words:
		continue
	if word in freq_table:
		freq_table[word] += 1
	else:
		freq_table[word] = 1

# CREATING THE DICTIONARY TO KEEP THE SCORE OF EACH SENTENCE:
sentences = sent_tokenize(text)
sentence_value = dict()

for sentence in sentences:
	for word, freq in freq_table.items():
		if word in sentence.lower():
			if sentence in sentence_value:
				sentence_value[sentence] += freq
			else:
				sentence_value[sentence] = freq



sum_values = 0
for sentence in sentence_value:
	sum_values += sentence_value[sentence]

# AVERAGE VALUE OF A SENTENCE FROM THE ORIGINAL TEXT:
average = int(sum_values / len(sentence_value))

# STORING SENTENCES INTO OUR SUMMARY:
summary = ''
for sentence in sentences:
	if (sentence in sentence_value) and (sentence_value[sentence] > (1.3 * average)):
		summary += " " + sentence
print("AFTER SUMMARIZING:\n\n"+summary)

# CLOSING THE FILE:
file1.close()

