punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']


def strip_punctuation(str):
    for pun_char in punctuation_chars:
        str = str.replace(pun_char, '')
    return str


# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


def get_pos(str):
    pos_count = 0
    str = strip_punctuation(str).lower().split()
    for word in str:
        if word in positive_words:
            pos_count += 1
    return pos_count


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())


def get_neg(str):
    neg_count = 0
    str = strip_punctuation(str).lower().split()
    for word in str:
        if word in negative_words:
            neg_count += 1
    return neg_count


def write_data_results():
    data_file = open("resulting_data.csv", "w")
    data_file.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score\n")

    with open("project_twitter_data.csv", 'r') as twitter_file:
        lines = twitter_file.readlines()[1:]
        for line in lines:
            line = line.strip().split(',')
            data_file.write("{}, {}, {}, {}, {}\n".format(line[1], line[2], get_pos(line[0]), get_neg(line[0]),
                                                          (get_pos(line[0]) - get_neg(line[0]))))

    data_file.close()


write_data_results()
with open("resulting_data.csv", "r") as result_file:
    for line in result_file:
        print(line)
