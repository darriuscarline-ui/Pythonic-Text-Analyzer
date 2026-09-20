# Pythonic-Text-Analyzer

from collections import Counter

#Create a path to the file in the same folder as this program
def read_file(file_name):
    """Read a text file and return its contents as a string."""
   #The with statement automatically closes the file when finished
    with open(file_name, "r") as file:
        return file.read()

#Convert all words to lowercase and separate them
def get_words(text):
    """Convert text to lowercase and return a list of words."""
    return text.lower().split()

#Counter efficiently counts the frequency of each word
def count_words(words):
    """Count how many times each word appears."""
    return Counter(words)

#Use a list comprehension to find words longer than three characters
def find_long_words(words):
    """Return a list of words with more than three characters."""
    return [word for word in words if len(word) > 3]


def display_results(words, word_counts, long_words):
    """Display the text analysis results."""
    print(f"Total number of words: {len(words)}")
    print(f"Unique words count: {len(word_counts)}")
#Display the five most frequently used words
    print("Most frequent words:")
    for word, count in word_counts.most_common(5):
        print(f"'{word}': {count}")
        
    print(f"Long words (more than 3 characters): {len(long_words)}")

#Read and process the text file
def analyze_text(file_name):
    """Analyze a text file and display word statistics."""
    text = read_file(file_name)
    words = get_words(text)
    #Calculate word frequencies and identify long words
    word_counts = count_words(words)
    long_words = find_long_words(words)
#display the completed analysis
    display_results(words, word_counts, long_words)

#Run the program using sample.txt 
if __name__ == "__main__":
    analyze_text("sample.txt")
