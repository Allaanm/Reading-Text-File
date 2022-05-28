# Open file
story = open('story.txt')

def read_file_content(story):
    return story.read()

def count_words():
    text = read_file_content(story)

    words = text.split(' ')

    words_dict = dict()

    for word in words:
        if word not in words_dict:
            words_dict[word] = 1
        else:
            words_dict[word] += 1

    return print(words_dict)

count_words()

# Close file
story.close()