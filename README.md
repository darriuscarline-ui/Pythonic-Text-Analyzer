Text Analyzer

Project overview
This project refactors an unpythonic text analyzer into a pythonic cleaner and efficient program. The original program analyzes a text file by counting words, finding the most frequently used words, and counting words that are longer than three characters. The refactored version "text_analyzer.py" applies python's best practices and demonstrates several idiomatic python features
Files
Unpytonic_analyzer.py - The original starter code
Text_analyzer.py - The refactored and improved version of the program
Sample.txt - the text file used to test the analyzer
README.md - Documentation for the project
How to Run the Program
1. Make sure Python 3 is installed on your computer.
2. download this repository.
3. Open the project folder in a terminal.
4. Make sure sample.txt is in the same folder as text_analyzer.py.
5. Run the following command: python3 text_analyzer.py
Refactoring Improvements

PEP 8

The refactored program follows PEP 8 guidelines by using snake_case naming conventions, consistent indentation, appropriate spacing, and descriptive function and variable names. Docstrings were also added to explain the purpose of each function.

Context Manager

The original program manually opened and closed the text file. The refactored program uses a with statement to handle the file: with open(file_path, "r") as file: return file.read()
Using a context manager ensures that the file is properly closed after it is read.

List Comprehension

The original program used a traditional for loop to create the list of long words. The refactored program uses a list comprehension:[word for word in words if len(word) > 3]
This makes the code more pythonic.

Collection Counter

The original program manually counted words using a dictionary and conditional statements. The refactored program uses the Counter from the collections module: from collections import Counter

The Counter efficiently counts the frequencies of each word and also provides the most_common() method for finding the most frequent words.

Modularity

The original program performed most of its work inside a single function. The refactored version separates the program into smaller functions:

read_file() - reads the text file.
get_words() - processes the text into a list of words.
count_words() - counts word frequencies.
find_long_words() - finds words longer than three characters.
display_results() - displays the analysis results.
analyze_text() - coordinates the different functions.

This is breaking the program into smaller functions makes it easier to read, test, maintain, and reuse.

The program will display:

The total number of words.
The number of unique words.
The five most frequently used words.
The total number of words longer than three characters.
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
