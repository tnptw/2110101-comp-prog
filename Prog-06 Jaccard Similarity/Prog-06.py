# Prog-06: Jaccard Similarity

from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

STOP_WORDS = stopwords.words('english')
STEMMER = PorterStemmer()

def read_tweets():
    f = open('biden.txt', encoding='utf-8')
    tweets = [line.strip() for line in f.readlines()]
    f.close()
    return tweets

def normalize_text( text ):
    words = []
    for w in word_tokenize(text.lower()):
        if w.isalnum() and w not in STOP_WORDS:
            words.append(STEMMER.stem(w))
    return get_unique( words )

def main():
    tweets = read_tweets()
    norm_tweets = []
    for t in tweets:
        norm_tweets.append( normalize_text(t) )

    print_width = 48
    while True:
        query = input('Query words   : ')
        if query == '': break
        n = int(input('No. of results: '))
        norm_query = normalize_text(query)
        top_n = top_n_similarity(norm_tweets, norm_query, n)
        if len(top_n) == 0:
            print('No matches found.')
        else:
            for tid, jc_coef in top_n:
                show_tweet(tid, tweets[tid], jc_coef, print_width)
        print('-' * print_width)

#--------------------------------------------------------
def get_unique( words ):
    unique_words = []
    for i in words:
        if i not in unique_words:
            unique_words.append(i)
    return unique_words

def jaccard(words_1, words_2):
    x = []
    for i in words_2:
        if i in words_1:
            x.append(i)
    if len(get_unique(words_1+words_2)) != 0:
        jaccard_coef = len(x)/len(get_unique(words_1+words_2))
    return jaccard_coef

def top_n_similarity(norm_tweets, norm_query, n):
    tweet_id = [int(e) for e in range(len(norm_tweets))]; top_reverse = []
    for i in range(len(tweet_id)):
        if jaccard(norm_tweets[i], norm_query) > 0:
            top_reverse.append([-jaccard(norm_tweets[i], norm_query), tweet_id[i]])
    top_reverse.sort(); top = []
    for i in top_reverse:
        top.append([i[1], -i[0]])
    top_n = top[:n]
    return top_n

def show_tweet(tweet_id, tweet_content, jc_coef, print_width):
    print()
    print('#'+str(tweet_id), '('+str(round(jc_coef, 2))+')')
    x = tweet_content.split(' ')
    t = []; m = 0; c = 0
    for i in x:
        if len(i)+m+2 <= print_width:
            t.append(i)
            m += len(i)+1
        elif len(i)+m+2 > print_width:
            t = ' '.join(t); print(' ', t.strip())
            t = []; t.append(i)
            m = 0; m += len(i)+1
        c += 1
        if c == len(x) :
            t = ' '.join(t); print(' ', t.strip())
#--------------------------------------------
main()