
# creates list of 30 common spam words to check in a given email
SPAM_KEYWORDS = [
    "free","urgent","instant","hurry","guaranteed","winner","cash","lottery","bonus","reward",
    "won","jackpot","prize","credit","discount","wire","bank","billing","congrats","save",
    "cheap","approved","income","debt","relief","dollar","dollars","guarantee","offer","limited-time"
]

# Function used for counting the spam words in text
def score_counter(text, words):
    # creates a dictionary to store the found words and count
    found = {}
    score = 0
    # for every letter in the word it will count the letter (making it lowercase)
    # and add it to the count and 'found' words and then to the score
    for w in words:
        c = text.lower().count(w)
        if c > 0:
            found[w] = c
            score += c
    return score, found
