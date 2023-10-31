
# import the necessary libraries

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string


def text_lowercase(text):
    return text.lower()
 
 # remove punctuation
def remove_punctuation(text):
    translator = str.maketrans('', '', string.punctuation)
    return text.translate(translator)
 
input_str = "Hey, did you know that the summer break is coming? Amazing right !! It's only 5 more days !!"
print(text_lowercase(input_str))

input_str = "Hey, did you know that the summer break is coming? Amazing right !! It's only 5 more days !!"
print(remove_punctuation(input_str))

# remove stopwords function
def remove_stopwords(text):
    stop_words = set(stopwords.words("english"))
    word_tokens = word_tokenize(text)
    filtered_text = [word for word in word_tokens if word not in stop_words]
    return filtered_text
 
example_text = "This is a sample sentence and we are going to remove the stopwords from this."
print(remove_stopwords(example_text))