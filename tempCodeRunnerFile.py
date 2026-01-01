import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

# Tokenize the user's input
def tokenize_input(input_text):
    return word_tokenize(input_text)

# Lemmatize the tokens
def lemmatize_tokens(tokens):
    lemmatized_tokens = []
    for token, pos in zip(tokens, nltk.pos_tag(tokens)):
        if pos:
            lemmatized_token = lemmatizer.lemmatize(token, get_pos(pos))
        else:
            lemmatized_token = token
        lemmatized_tokens.append(lemmatized_token)
    return lemmatized_tokens

# Example usage
input_text = "Hello, how are you?"
tokens = tokenize_input(input_text)
lemmatized_tokens = lemmatize_tokens(tokens)
print(lemmatized_tokens)

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
