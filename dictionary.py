#importing th required modules
import json
from difflib import get_close_matches as filterer
#Reading the JSON data
data=json.load(open("data.json"))
#Creating the function
def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data: #if user entered "texas" this will check for "Texas" as well.
        return data[w.title()]
    elif w.upper() in data: #in case user enters words like USA or NATO
        return data[w.upper()]
    elif len(filterer(w, data.keys())) > 0:
        reply = input("Did you mean %s instead? Enter Y if yes, N if no: " % filterer(w, data.keys())[0])
        if reply == "Y":
            return data[filterer(w, data.keys())[0]]
        elif reply == "N":
            return "Given word dosen't exist. Please double check it and then try again"
        else:
            return "Sorry we could not understand what you said please retry"
    else:
        return "Given word dosen't exist. Please double check it and then try again"
#Executing the function
word = input("Enter a word: ")
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
