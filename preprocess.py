import string
class Preprocess:
    def __init__(self):
        self.stopwords = ["and", "the", "is"]



    def preprocess_text(self, text):
        # Convert to lowercase
        text = text.lower()
        # Remove punctuation
        text = text.translate(str.maketrans("", "", string.punctuation))
        # Tokenization
        tokens = text.split()
        
        # Remove stopwords (if needed)
        stopwords = ["and", "the", "is"]
        tokens = [word for word in tokens if word not in stopwords]
        
        # return tokens
        return " ".join(tokens)
