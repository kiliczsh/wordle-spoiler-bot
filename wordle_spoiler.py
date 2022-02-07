from datetime import date
import json
import tweepy

TW_API_KEY="***"
TW_API_KEY_SECRET="***"
TW_ACCESS_TOKEN="***"
TW_ACCESS_TOKEN_SECRET="***"


def read_json():
    f = open("answers.json", 'r')
    data = json.load(f)
    f.close()
    return data
    
def get_list_of_words(data):
    list_of_words = []
    words = data[0].split(",")
    for i in range(len(words)):
        list_of_words.append(words[i])
    return list_of_words

def get_day_index():
    delta = date.today() - date(2021, 6, 19) # the base date is the 19th of June 2021
    return delta.days

def get_word_of_the_day():
    all_answers = get_list_of_words(read_json())
    return all_answers[get_day_index()]
    
get_word_of_the_day()

def create_tweet():
    word = get_word_of_the_day()
    index = get_day_index()
    return "Wordle of the day: " + word + " #wordle #wordle_spoiler #wordle_spoiler_bot #Wordle" + str(index)

def tweet():
    auth = tweepy.OAuthHandler(TW_API_KEY, TW_API_KEY_SECRET)
    auth.set_access_token(TW_ACCESS_TOKEN, TW_ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    api.update_status(create_tweet())
    
tweet()



