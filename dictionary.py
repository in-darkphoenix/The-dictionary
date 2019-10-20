import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def meaning(word) :
    word = word.lower()
    if word in data :
        return data[word]
    elif word.title() in data :  #in case of proper noun ex-Delhi, Amsterdam
        return data[word.title()]
    elif word.upper() in data :  #in case of acronym ex-US, ATM
        return data[word.upper()]
    elif len(get_close_matches(word,data.keys())) > 0 :
        yn = input("Did you mean %s instead? Enter Y if yes and N if no :" % get_close_matches(word,data.keys())[0])
        if yn == "Y" :
            return data[get_close_matches(word,data.keys())[0]]
        elif yn == "N" :
            return "Then, the word doesn't exist, please check your input"
        else :
            return "We didn'r understand your entry!"
    else :
        return "The word doesn't exist, please check the word before entering!!"

word = input("Enter the word to know it's meaning - ")
output = meaning(word)

if type(output) == list :
    for item in output :
        print(item)
else :
    print(output)
