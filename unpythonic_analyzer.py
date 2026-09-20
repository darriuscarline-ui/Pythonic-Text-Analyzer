def ReadFile(file_name):
    my_file = open(file_name, "r")
    the_text_content = my_file.read()
    my_file.close()
    my_list = the_text_content.split()

    long_words = []
    for word in my_list:
        if len(word) > 7:
            long_words.append(word)

    print("Long words:")
    for word in long_words:
        print(word)

    print("Number of long words: " + str(len(long_words)))


ReadFile("sample_text.txt")
